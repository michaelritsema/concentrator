<?xml version="1.0" encoding="UTF-8"?>
<module>
    <name>Collect Available Wireless Networks</name>
    <description>Get a list Wireless Networks available to the endpoint</description>
    <platforms>
	<!-- 1-OS X; 2-windows; 3-Linux -->
        <platform>2</platform>
    </platforms>
    <parameters>
	<!-- No Parameters on this script -->
    </parameters>
	<!-- Output Description: 
		eventID: 100301
		tag0:	"BSSID",			#18:64:72:72:27:f2
		tag1:	"Channel",			#1
		tag2:	"Signal",			#56
		tag3:	"Encryption",		#CCMP
		tag4:	"Authentication",	#WPA2-Personal
		tag5:	"SSID",				#Ziften-Private
		tag6:	"RadioType",		#802.11n
		tag7:	"InterfaceName",	#Wireless Network Connection
	-->
	<!-- Add no spaces or line breaks between <extension> and <![CDATA[ or any content after.  
	     It will break the scripts because of parsing issues -->
    <extension><![CDATA[# -=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=
#     Script name : wlanscan 
#          Author : Kris Cieslak
#
#     Parameters  : None
#   Requirements  : Windows Vista or higher
#                   Wireless network card
#

# -=-=-=-=-=- translation -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# If netsh is in a different language you have to change following values:
# (use "netsh wlan show network mode=bssid" command to check your translation)

$eventID = 100301

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

$interface_name_text = "Interface name";
$ssid_text           = "SSID";
$network_type_text   = "Network type";
$Authentication_text = "Authentication";
$encryption_text     = "Encryption";
$bssid_text          = "BSSID";
$signal_text         = "Signal";
$radio_type_text     = "Radio type";
$channel_text        = "Channel";
$basic_rates_text    = "Basic rates";
$other_rates_text    = "Other rates";

function getValueByName ( $inputText, $nameString, [ref]$var ) {
	$found = $FALSE
	if ([regex]::IsMatch($inputText,"\b$nameString\b","IgnoreCase")) {
	    $var.Value = ([regex]::Replace($inputText,"^[^:]*: ",""))
		$var.Value = $var.Value.Trim()
		$found = $TRUE
	}
	return $found;
}

Function ScanNetworks
{
	$interfaceName = "";
	$ssid=""
	$NetworkType=""
	$Authentication=""
	$Encryption=""
	$BSSID=""
	$Signal=""
	$Channel=""
	$RadioType=""
	$BasicRates=""
	$OtherRates=""
	$namedValue = ""
	
	$resultSet = CreateResultSet

	netsh wlan show network mode=bssid | % {
		
		if (getValueByName $_ $interface_name_text ([ref]$namedValue)) {
			$interfaceName = $namedValue;
		}
		
		if (getValueByName $_ $ssid_text ([ref]$namedValue)) {
			if ($ssid.Length -gt 0) {
				$row = CreateResultSetRow
				AddRowItem $row $BSSID
				AddRowItem $row $Channel
				AddRowItem $row $Signal
				AddRowItem $row $Encryption
				AddRowItem $row $Authentication
				AddRowItem $row $SSID
				AddRowItem $row $RadioType
				AddRowItem $row $InterfaceName
				AddRowItem $row $NetworkType
				AddRow $resultSet $row
			}
			$ssid = $namedValue
			$NetworkType=""
			$Authentication=""
			$Encryption=""
			$BSSID=""
			$Signal=""
			$Channel=""
			$RadioType=""
			$BasicRates=""
			$OtherRates=""
		}
		if (getValueByName $_ $bssid_text ([ref]$namedValue)) {
			if ($BSSID.Length -gt 0) {
				$row = CreateResultSetRow
				AddRowItem $row $BSSID
				AddRowItem $row $Channel
				AddRowItem $row $Signal
				AddRowItem $row $Encryption
				AddRowItem $row $Authentication
				AddRowItem $row $SSID
				AddRowItem $row $RadioType
				AddRowItem $row $InterfaceName
				AddRowItem $row $NetworkType
				AddRow $resultSet $row
				$Signal=""
				$RadioType=""
				$Channel=""
				$BasicRates=""
				$OtherRates=""
			}
			$BSSID = $namedValue;
		}
		if (getValueByName $_ $network_type_text ([ref]$namedValue)) {
			$NetworkType = $namedValue;
		}
		if (getValueByName $_ $authentication_text ([ref]$namedValue)) {
			$Authentication = $namedValue;
		}
		if (getValueByName $_ $encryption_text ([ref]$namedValue)) {
			$Encryption = $namedValue;
		}
		if (getValueByName $_ $signal_text ([ref]$namedValue)) {
			$Signal = $namedValue;
		}
		if (getValueByName $_ $channel_text ([ref]$namedValue)) {
			$Channel = $namedValue;
		}
		if (getValueByName $_ $radio_type_text ([ref]$namedValue)) {
			  $RadioType = $namedValue;
		}
		if (getValueByName $_ $basic_rates_text ([ref]$namedValue)) {
			  $BasicRates = $namedValue;
		}
		if (getValueByName $_ $other_rates_text ([ref]$namedValue)) {
			  $OtherRates = $namedValue;
		}
	};
	if ($ssid.Length -gt 0) {
		$row = CreateResultSetRow
		AddRowItem $row $BSSID
		AddRowItem $row $Channel
		AddRowItem $row $Signal
		AddRowItem $row $Encryption
		AddRowItem $row $Authentication
		AddRowItem $row $SSID
		AddRowItem $row $RadioType
		AddRowItem $row $InterfaceName
		AddRowItem $row $NetworkType
		AddRow $resultSet $row
	}
	if ($ssid.Length -gt 0) {
		EmitExtensionResults $eventID $resultSet
	}
}

if  ((gwmi win32_operatingsystem).Version.Split(".")[0] -lt 6) {
    "This script works on Windows Vista or higher."
	Exit 1
}

if ((gsv "wlansvc").Status -ne "Running" ) {
    "WLAN AutoConfig must be running."
	Exit 2
}

$gehret = GetEventHandlesForPersistentMode
if ( -not $gehret[0] )
{
	"we are not in 'persistent' mode"
	ScanNetworks
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
		ScanNetworks
	}
 
	"Leaving script"
	Exit 0
}

# SIG # Begin signature block
# MIITXQYJKoZIhvcNAQcCoIITTjCCE0oCAQExCzAJBgUrDgMCGgUAMGkGCisGAQQB
# gjcCAQSgWzBZMDQGCisGAQQBgjcCAR4wJgIDAQAABBAfzDtgWUsITrck0sYpfvNR
# AgEAAgEAAgEAAgEAAgEAMCEwCQYFKw4DAhoFAAQUvASyOYZ5UARcDGCz29AMKdv9
# bGagghBcMIIE0zCCA7ugAwIBAgIQGNrRniZ96LtKIVjNzGs7SjANBgkqhkiG9w0B
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
# hvcNAQkEMRYEFDqC5H3iZhxCJ2Mzm8RQM0siRD8BMA0GCSqGSIb3DQEBAQUABIIB
# AEWnQ3r4mg1k4P84Y+xjLyYHuxl4aJfMio2IXM4WFYHPdJTEAMXBohI3xIkWNdyR
# fv+ED36vGlegfFsDxsdfFWNqvfwqKBqiUzVhBSGSjPKCK+Dzhz9xg+jNozAnH/l6
# 1XEwI0VvN8yarz8EG8mELaSBKqMYyIB3l/V9v3eOgnz8gPDP1ctIIqXIEoptm551
# TyAAmLdscOweI2XNIdf+v1o1qt7wNXbqXJp3qFPA9Am8wfVlbWDiH56s7L71gCSP
# 2n0dF+ipBAOA4/oT4Z7L/V/R73weEOEcK1bEK5UBaI1RUE1TsrJBv+ix5TIifoS/
# N5eNdveznePAbKu2TdDpQWs=
# SIG # End signature block
]]></extension>
</module>