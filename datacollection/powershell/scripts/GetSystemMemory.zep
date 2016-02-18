<?xml version="1.0" encoding="UTF-8"?>
<module>
    <name>Get System Memory</name>
    <description>Scan Agent Systems for number of memory slots and installed memory</description>
    <platforms>
	<!-- 1-OS X; 2-windows; 3-Linux -->
        <platform>2</platform>
    </platforms>
    <parameters>
	<!-- None -->
    </parameters>
	<!-- Output:
		EventID: 100302 Computer Memory Information
		tag0 "MaxCapacity"				#33554432
		tag1 "TotMemPopulated"			#17179869184
		tag2 "MemoryDevices"			#4
		tag3 "SlotsFilled"				#4
		tag4 "SlotsEmpty"				#0
		tag5 "MemoryErrorCorrection"	#3

		EventID: 100303 Individual Memory Slot Information
		tag0 "BankLabel"				#BANK 0
		tag1 "DeviceLocator"			#DIMM3
		tag2 "Capacity"					#4294967296
		tag3 "Manufacturer"				#Hynix/Hyundai
		tag4 "PartNumber"				#HMT351U6CFR8C-PB
		tag5 "Speed"					#1600
	-->
	<!-- Add no spaces or line breaks between <extension> and <![CDATA[ or any content after.  
	     It will break the scripts because of parsing issues -->
    <extension><![CDATA[# Script name: getmem.ps1
# Author: Jeff Mason aka tnjman aka bitdoctor - Aug 9, 2013
# ORIGINAL CREDIT for base script to Jesse Hamrick at: http://www.powershellpro.com/dimm-witt/200/
# I modified & enhanced it, including correcting the 'ForEach' methods and cleaner formatting with blank lines + summary info
# PowerShell script to list Memory Slot Information & Detailed and Summary Memory Information for a remote computer, 
# including:
# 1) Total # of memory slots in the system
# 2) Each non-empty Memory Slot ID, along with Amount of Memory in the slot (in GB)
# [I added cleaner formatting via write-host "" (blank lines), plus output Computer name (strComputer) in various output]
# [I added all the items under #3]
# 3) Summary of Memory Slots populated, 
#   a) # of Total Slots remaining Available (open/unused)
#   b) # of Total Slots Filled (Used/unavailable)
#   c) Total Memory Populated/Installed (in GB)

$eventIDSystem = 100302
$eventIDMemorySlot = 100303

#Fix output to NOT put line breaks in the output (ok, after 4k columns it will)
if( $Host -and $Host.UI -and $Host.UI.RawUI ) {
	$rawUI = $Host.UI.RawUI
	$oldSize = $rawUI.BufferSize
	$typeName = $oldSize.GetType( ).FullName
	$newSize = New-Object $typeName (4096, $oldSize.Height)
	$rawUI.BufferSize = $newSize
}

##########################################################################
#these are utility methods for doing common tasks for Ziften extension scripts
#powershell version (only works for 2 and up)
$psversion = $PSVersionTable.PSVersion
#get the name of this script, serves as base for things
$scriptName = split-path -Leaf $MyInvocation.MyCommand.Definition
#get the directory of this script, which could be used for temp files
$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition
#get the name of the 'begin' and 'end' events, which are used when running 'persistent'ly (only)
$beginEventName = ( "Global\" + $scriptName + ".begin" )
$endEventName = ( "Global\" + $scriptName + ".end" )

#standard method of emitting extension results
function EmitExtensionResults
{
	param (
		[int]$eventCode, #the required lucasian event code
		[System.Collections.ArrayList]$resultSet #the optional set of multi-valued data
	)
 
	Write-Output "==== BEGIN EXTENSION RESULTS ===="
	Write-Output $eventCode

	if ($resultSet -ne $null) #absurd
	{
		foreach ( $row in $resultset )
		{
			if ($row -ne $null) #preposterous
            {
                [string]$rowtext = ""
                foreach ( $field in $row )
                {
                    #field sep if not first item
                    if ( 0 -ne $rowtext.length )
                    {
                        $rowtext += "|"
                    }
                    if ($field -eq $null) #conceivable
                    {
                        #null objects just translate to the empty field
                    }
                    else
                    {
                        #escape field
                        [string]$fieldtext = $field
                        $fieldtext = $fieldtext -replace '[\\]','\\'
                        $fieldtext = $fieldtext -replace '[\|]', '\|'
                        $fieldtext = $fieldtext -replace '[\r]', "\`r"
                        $fieldtext = $fieldtext -replace '[\n]', "\`n"
                        $rowtext += $fieldtext
                    }
                }
                Write-Output $rowtext
            }
        }
    }
    Write-Output "==== END EXTENSION RESULTS ===="
    return
}


#these trivial helpers are here mostly for documentation; obviously they are trivial
#create result set
function CreateResultSet
{
    New-Object System.Collections.ArrayList
}
#create result set row
function CreateResultSetRow
{
    New-Object System.Collections.ArrayList
}
#add row item
function AddRowItem ( [System.Collections.ArrayList]$row, [string]$item )
{
    [void]$row.Add( $item )
}
#add row
function AddRow ( [System.Collections.ArrayList]$resultset, [System.Collections.ArrayList]$row )
{
    [void]$resultset.Add( $row )
}
 
#in 'persistent' mode, our process is expected to live a long while, producing
#multiple result sets. In this mode, the host process (i.e. the Agent) will
#use events to convey to us: a) time to run (maybe generating a result set),
#and b) time to terminate.
#get our begin and end event handles, if possible (i.e., only if we are being run 'persistently')
function GetEventHandlesForPersistentMode
{
    $evtBegin = $null
    try { $evtBegin = [System.Threading.EventWaitHandle]::OpenExisting($beginEventName) }
    catch { }
    $evtEnd = $null
    try { $evtEnd = [System.Threading.EventWaitHandle]::OpenExisting($endEventName) }
    catch { }
    
    if ( ( $evtBegin -ne $null ) -and ( $evtEnd -ne $null ) )
    {
        $true
        $evtBegin
        $evtEnd
    }
    else
    {
        $false
        $null
        $null
    }
}

#in 'persistent' mode, our process is expected to live a long while, producing
#multiple result sets. In this mode, the host process (i.e. the Agent) will
#use events to convey to us: a) time to run (maybe generating a result set),
#and b) time to terminate.
#get our begin and end event handles, if possible (i.e., only if we are being run 'persistently')
function GetEventHandlesForPersistentMode
{
    $evtBegin = $null
    try { $evtBegin = [System.Threading.EventWaitHandle]::OpenExisting($beginEventName) }
    catch { }
    $evtEnd = $null
    try { $evtEnd = [System.Threading.EventWaitHandle]::OpenExisting($endEventName) }
    catch { }
    
    if ( ( $evtBegin -ne $null ) -and ( $evtEnd -ne $null ) )
    {
        $true
        $evtBegin
        $evtEnd
    }
    else
    {
        $false
        $null
        $null
    }
}

Function ScanMemory
{
	#Get the two interfaces
	$colSlots = Get-WmiObject -Class "win32_PhysicalMemoryArray" -namespace "root\CIMV2"
	$colRAM = Get-WmiObject -Class "win32_PhysicalMemory" -namespace "root\CIMV2"
	#Initialize variables
	$NumSlots = 0
	$SlotsFilled = 0
	$SlotsEmpty = 0
	$TotMemPopulated = 0
	#Count the slots, filled and empty, and total memory
	$colRAM | ForEach {
		if ($_.Capacity -eq 0) {
			$SlotsEmpty = $SlotsEmpty + 1
		} else {
			$TotMemPopulated = $TotMemPopulated + $_.Capacity
			$SlotsFilled = $SlotsFilled + 1
		}
	}

	$resultSetSystem = CreateResultSet
	$colSlots | ForEach {
		$row = CreateResultSetRow
		$maxMemory = $_.MaxCapacity * 1024
		AddRowItem $row $maxMemory
		AddRowItem $row $_.MemoryDevices
		AddRowItem $row $SlotsFilled
		AddRowItem $row $SlotsEmpty
		AddRowItem $row $_.MemoryErrorCorrection
		AddRow $resultSetSystem $row
	}
	EmitExtensionResults $eventIDSystem $resultSetSystem

	$resultSetMemory = CreateResultSet
	$colRAM | ForEach {
		if ($_.Capacity -gt 0) {
			$row = CreateResultSetRow
			AddRowItem $row $_.BankLabel
			AddRowItem $row $_.Capacity
			AddRowItem $row $_.DataWidth
			AddRowItem $row $_.DeviceLocator
			AddRowItem $row $_.Manufacturer
			AddRowItem $row $_.PartNumber
			AddRowItem $row $_.Speed
			AddRow $resultSetMemory $row
		}
	}
	EmitExtensionResults $eventIDMemorySlot $resultSetMemory
}

$gehret = GetEventHandlesForPersistentMode
if ( -not $gehret[0] )
{
	"we are not in 'persistent' mode"
	ScanMemory
	"Leaving script"
	Exit 0
}
else
{
	"we are in persistent mode"
	#example of a PERSISTENT run scenario
	#(we already called GetEventHandlesForPersistentMode above)
	$evtBegin = $gehret[1] #(just for readability)
	$evtEnd = $gehret[2] #(just for readability)
 
	"wait for our 'begin' event, which means it is time to run"
	while ( $evtBegin.WaitOne() )
	{
		if ( $evtEnd.WaitOne(0) ) { break; }
		ScanMemory
	}
 
	"Leaving script"
	Exit 0
}

# SIG # Begin signature block
# MIITXQYJKoZIhvcNAQcCoIITTjCCE0oCAQExCzAJBgUrDgMCGgUAMGkGCisGAQQB
# gjcCAQSgWzBZMDQGCisGAQQBgjcCAR4wJgIDAQAABBAfzDtgWUsITrck0sYpfvNR
# AgEAAgEAAgEAAgEAAgEAMCEwCQYFKw4DAhoFAAQUeTS/4s7teTPwL8Mq9zyJQBSc
# nQigghBcMIIE0zCCA7ugAwIBAgIQGNrRniZ96LtKIVjNzGs7SjANBgkqhkiG9w0B
# AQUFADCByjELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8w
# HQYDVQQLExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAw
# NiBWZXJpU2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYD
# VQQDEzxWZXJpU2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRp
# b24gQXV0aG9yaXR5IC0gRzUwHhcNMDYxMTA4MDAwMDAwWhcNMzYwNzE2MjM1OTU5
# WjCByjELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYD
# VQQLExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAwNiBW
# ZXJpU2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQD
# EzxWZXJpU2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24g
# QXV0aG9yaXR5IC0gRzUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCv
# JAgIKXo1nmAMqudLO07cfLw8RRy7K+D+KQL5VwijZIUVJ/XxrcgxiV0i6CqqpkKz
# j/i5Vbext0uz/o9+B1fs70PbZmIVYc9gDaTY3vjgw2IIPVQT60nKWVSFJuUrjxuf
# 6/WhkcIzSdhDY2pSS9KP6HBRTdGJaXvHcPaz3BJ023tdS1bTlr8Vd6Gw9KIl8q8c
# kmcY5fQGBO+QueQA5N06tRn/Arr0PO7gi+s3i+z016zy9vA9r911kTMZHRxAy3Qk
# GSGT2RT+rCpSx4/VBEnkjWNHiDxpg8v+R70rfk/Fla4OndTRQ8Bnc+MUCH7lP59z
# uDMKz10/NIeWiu5T6CUVAgMBAAGjgbIwga8wDwYDVR0TAQH/BAUwAwEB/zAOBgNV
# HQ8BAf8EBAMCAQYwbQYIKwYBBQUHAQwEYTBfoV2gWzBZMFcwVRYJaW1hZ2UvZ2lm
# MCEwHzAHBgUrDgMCGgQUj+XTGoasjY5rw8+AatRIGCx7GS4wJRYjaHR0cDovL2xv
# Z28udmVyaXNpZ24uY29tL3ZzbG9nby5naWYwHQYDVR0OBBYEFH/TZafC3ey78DAJ
# 80M5+gKvMzEzMA0GCSqGSIb3DQEBBQUAA4IBAQCTJEowX2LP2BqYLz3q3JktvXf2
# pXkiOOzEp6B4Eq1iDkVwZMXnl2YtmAl+X6/WzChl8gGqCBpH3vn5fJJaCGkgDdk+
# bW48DW7Y5gaRQBi5+MHt39tBquCWIMnNZBU4gcmU7qKEKQsTb47bDN0lAtukixlE
# 0kF6BWlKWE9gyn6CagsCqiUXObXbf+eEZSqVir2G3l6BFoMtEMze/aiCKm0oHw0L
# xOXnGiYZ4fQRbxC1lfznQgUy286dUV4otp6F01vvpX1FQHKOtw5rDgb7MzVIcbid
# J4vEZV8NhnacRHr2lVz2XTIIM6RUthg/aFzyQkqFOFSDX9HoLPKsEdao7WNqMIIF
# czCCBFugAwIBAgIQMSRcVqdMfpfUudH39AL+AjANBgkqhkiG9w0BAQUFADCBtDEL
# MAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQLExZW
# ZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTswOQYDVQQLEzJUZXJtcyBvZiB1c2UgYXQg
# aHR0cHM6Ly93d3cudmVyaXNpZ24uY29tL3JwYSAoYykxMDEuMCwGA1UEAxMlVmVy
# aVNpZ24gQ2xhc3MgMyBDb2RlIFNpZ25pbmcgMjAxMCBDQTAeFw0xNDAzMjUwMDAw
# MDBaFw0xNjA0MjMyMzU5NTlaMIG2MQswCQYDVQQGEwJVUzEOMAwGA1UECBMFVGV4
# YXMxDzANBgNVBAcTBkF1c3RpbjEiMCAGA1UEChQZWmlmdGVuIFRlY2hub2xvZ2ll
# cywgSW5jLjE+MDwGA1UECxM1RGlnaXRhbCBJRCBDbGFzcyAzIC0gTWljcm9zb2Z0
# IFNvZnR3YXJlIFZhbGlkYXRpb24gdjIxIjAgBgNVBAMUGVppZnRlbiBUZWNobm9s
# b2dpZXMsIEluYy4wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC6MlCk
# Cs0pVy0kWmXE7LhgMuwEAcT2IxG6fzrLPzOThpR7GPAJYKG0Ts7Gx0VYr1H21Vqm
# zFhcmt5/A4fOleD3ryV/viIKLFxwBqT4I/TEIPBt6TOClOJpgasALZh+sFM6Ctph
# zohGX4Aku5Jc3uvSUUCinGIUhRWa1rUQKt133YFEAvCz+EM9FUQx3q309yPZ3RHu
# DZftsV+b1hTyO9gNRJTZ1YlvaZvRrHrDZEJ+D7s9WgU8xhK3h7BD/MOzAYU9NHcr
# G6f4t9+2ERsl0upbIu+LxpKIo58Ia6GLKVtYWWDCyeqx62/odO4zPypDRcZhvG8/
# gG28uaNp5a/oQTDNAgMBAAGjggF7MIIBdzAJBgNVHRMEAjAAMA4GA1UdDwEB/wQE
# AwIHgDBABgNVHR8EOTA3MDWgM6Axhi9odHRwOi8vY3NjMy0yMDEwLWNybC52ZXJp
# c2lnbi5jb20vQ1NDMy0yMDEwLmNybDBEBgNVHSAEPTA7MDkGC2CGSAGG+EUBBxcD
# MCowKAYIKwYBBQUHAgEWHGh0dHBzOi8vd3d3LnZlcmlzaWduLmNvbS9ycGEwEwYD
# VR0lBAwwCgYIKwYBBQUHAwMwcQYIKwYBBQUHAQEEZTBjMCQGCCsGAQUFBzABhhho
# dHRwOi8vb2NzcC52ZXJpc2lnbi5jb20wOwYIKwYBBQUHMAKGL2h0dHA6Ly9jc2Mz
# LTIwMTAtYWlhLnZlcmlzaWduLmNvbS9DU0MzLTIwMTAuY2VyMB8GA1UdIwQYMBaA
# FM+Zqep7JvRLyY6P1/AFJu/j0qedMBEGCWCGSAGG+EIBAQQEAwIEEDAWBgorBgEE
# AYI3AgEbBAgwBgEBAAEB/zANBgkqhkiG9w0BAQUFAAOCAQEAUXs17nHNwE0Oz9/s
# jEb5S3AT9Zz+sQvtMhvZVx3yiqxFW7k/kReSrYRC8fgW4+po4q2M4rauPd983ZeJ
# ta8/jlhbowfNFfi22dbEaMODgZBVvhqEQnYUTKeGDrYKH2XWpSx4vFjZKLYZHRKx
# NdfflbgvwgL3XBdzPMRM+iYWOsZUHFdNNlfk2EtQbypuKI0uwbsWsvNTfBiyHPU3
# oZAfX6nnYXRTO3TkYjx8gHi6RYuElquVpw59blJZyj1IlnAcJvEAkEvVlIB5OPrQ
# vUpEaSDi3ATdIkJhYl/6G/suvLSxrq/pN7sqVIqq4l0/Sqnxtcitla1wK9yoAi3o
# ZuJU5zCCBgowggTyoAMCAQICEFIA5aolVvwahu2WydRLM8cwDQYJKoZIhvcNAQEF
# BQAwgcoxCzAJBgNVBAYTAlVTMRcwFQYDVQQKEw5WZXJpU2lnbiwgSW5jLjEfMB0G
# A1UECxMWVmVyaVNpZ24gVHJ1c3QgTmV0d29yazE6MDgGA1UECxMxKGMpIDIwMDYg
# VmVyaVNpZ24sIEluYy4gLSBGb3IgYXV0aG9yaXplZCB1c2Ugb25seTFFMEMGA1UE
# AxM8VmVyaVNpZ24gQ2xhc3MgMyBQdWJsaWMgUHJpbWFyeSBDZXJ0aWZpY2F0aW9u
# IEF1dGhvcml0eSAtIEc1MB4XDTEwMDIwODAwMDAwMFoXDTIwMDIwNzIzNTk1OVow
# gbQxCzAJBgNVBAYTAlVTMRcwFQYDVQQKEw5WZXJpU2lnbiwgSW5jLjEfMB0GA1UE
# CxMWVmVyaVNpZ24gVHJ1c3QgTmV0d29yazE7MDkGA1UECxMyVGVybXMgb2YgdXNl
# IGF0IGh0dHBzOi8vd3d3LnZlcmlzaWduLmNvbS9ycGEgKGMpMTAxLjAsBgNVBAMT
# JVZlcmlTaWduIENsYXNzIDMgQ29kZSBTaWduaW5nIDIwMTAgQ0EwggEiMA0GCSqG
# SIb3DQEBAQUAA4IBDwAwggEKAoIBAQD1I0tepdeKuzLp1Ff37+THJn6tGZj+qJ19
# lPY2axDXdYEwfwRof8srdR7NHQiM32mUpzejnHuA4Jnh7jdNX847FO6G1ND1JzW8
# JQs4p4xjnRejCKWrsPvNamKCTNUh2hvZ8eOEO4oqT4VbkAFPyad2EH8nA3y+rn59
# wd35BbwbSJxp58CkPDxBAD7fluXF5JRx1lUBxwAmSkA8taEmqQynbYCOkCV7z78/
# HOsvlvrlh3fGtVayejtUMFMb32I0/x7R9FqTKIXlTBdOflv9pJOZf9/N76R17+8V
# 9kfn+Bly2C40Gqa0p0x+vbtPDD1X8TDWpjaO1oB21xkupc1+NC2JAgMBAAGjggH+
# MIIB+jASBgNVHRMBAf8ECDAGAQH/AgEAMHAGA1UdIARpMGcwZQYLYIZIAYb4RQEH
# FwMwVjAoBggrBgEFBQcCARYcaHR0cHM6Ly93d3cudmVyaXNpZ24uY29tL2NwczAq
# BggrBgEFBQcCAjAeGhxodHRwczovL3d3dy52ZXJpc2lnbi5jb20vcnBhMA4GA1Ud
# DwEB/wQEAwIBBjBtBggrBgEFBQcBDARhMF+hXaBbMFkwVzBVFglpbWFnZS9naWYw
# ITAfMAcGBSsOAwIaBBSP5dMahqyNjmvDz4Bq1EgYLHsZLjAlFiNodHRwOi8vbG9n
# by52ZXJpc2lnbi5jb20vdnNsb2dvLmdpZjA0BgNVHR8ELTArMCmgJ6AlhiNodHRw
# Oi8vY3JsLnZlcmlzaWduLmNvbS9wY2EzLWc1LmNybDA0BggrBgEFBQcBAQQoMCYw
# JAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLnZlcmlzaWduLmNvbTAdBgNVHSUEFjAU
# BggrBgEFBQcDAgYIKwYBBQUHAwMwKAYDVR0RBCEwH6QdMBsxGTAXBgNVBAMTEFZl
# cmlTaWduTVBLSS0yLTgwHQYDVR0OBBYEFM+Zqep7JvRLyY6P1/AFJu/j0qedMB8G
# A1UdIwQYMBaAFH/TZafC3ey78DAJ80M5+gKvMzEzMA0GCSqGSIb3DQEBBQUAA4IB
# AQBWIuY0pMRhy0i5Aa1WqGQP2YyRxLvMDOWteqAif99HOEotbNF/cRp87HCpsfBP
# 5A8MU/oVXv50mEkkhYEmHJEUR7BMY4y7oTTUxkXoDYUmcwPQqYxkbdxxkuZFBWAV
# WVE5/FgUa/7UpO15awgMQXLnNyIGCb4j6T9Emh7pYZ3MsZBc/D3SjaxCPWU21LQ9
# QCiPmxDPIybMSyDLkB9djEw0yjzY5TfWb6UgvTTrJtmuDefFmvehtCGRM2+G6Fi7
# JXx0Dlj+dRtjP84xfJuPG5aexVN2hFucrZH6rO2Tul3IIVPCglNjrxINUIcRGz1U
# UpaKLJw9khoImgUux5OlSJHTMYICazCCAmcCAQEwgckwgbQxCzAJBgNVBAYTAlVT
# MRcwFQYDVQQKEw5WZXJpU2lnbiwgSW5jLjEfMB0GA1UECxMWVmVyaVNpZ24gVHJ1
# c3QgTmV0d29yazE7MDkGA1UECxMyVGVybXMgb2YgdXNlIGF0IGh0dHBzOi8vd3d3
# LnZlcmlzaWduLmNvbS9ycGEgKGMpMTAxLjAsBgNVBAMTJVZlcmlTaWduIENsYXNz
# IDMgQ29kZSBTaWduaW5nIDIwMTAgQ0ECEDEkXFanTH6X1LnR9/QC/gIwCQYFKw4D
# AhoFAKB4MBgGCisGAQQBgjcCAQwxCjAIoAKAAKECgAAwGQYJKoZIhvcNAQkDMQwG
# CisGAQQBgjcCAQQwHAYKKwYBBAGCNwIBCzEOMAwGCisGAQQBgjcCARUwIwYJKoZI
# hvcNAQkEMRYEFL/2oxawnsQD1jHp5u3jKhgNrIfvMA0GCSqGSIb3DQEBAQUABIIB
# AE2BmbJwculY3haZL4czHu1FURzy6hv98+6bKKFcv9Hf2CmPXlhCE0m9OzRBakX0
# 12Ff0RY33rd9WFA7QOpq3NDu+6SM2Tz9WcN+oH6Qmko92QbEA1cE3henzbbYtSgM
# HsDevYI+GebNWiaZrAT5QKm2xnp/pOGqU5UFNEMLwpR/ge43m/019DRRbe/vtpKF
# sEoNqAL4SYqLy1VgRqPNhgW90FrLO3a9jNYNj1sJeMpDHXYXlyFKC5cFXcSqia46
# e8OmOwRsuWCTP38vqYJ3SI7/dNiC3pF0a4AkxJljZ64MtT3zJgK12HT+2iPdSus0
# 41rXq9owcm15PnaDq2hUcw8=
# SIG # End signature block
]]></extension>
</module>