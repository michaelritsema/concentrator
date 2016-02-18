<?xml version="1.0" encoding="UTF-8"?>
<module>
    <name>Collect Certificate Information</name>
    <description>Get a list of installed certificates on client systems</description>
    <platforms>
	<!-- 1-OS X; 2-windows; 3-Linux -->
        <platform>2</platform>
    </platforms>
    <parameters>
	<!-- No Parameters on this script -->
    </parameters>
	<!-- Output Description:
		eventID: 100101
		tag0:	"StoreLocation",#LocalMachine
		tag1:	"Store",		#Root
		tag2:	"Subject",		#CN=thawte Primary Root CA - G3, OU="(c) 2008 thawte, Inc. - For authorized use only", OU=Certification Services Division, O="thawte, Inc.", C=US
		tag3:	"SerialNumber",	#600197B746A7EAB4B49AD64B2FF790FB
		tag4:	"Thumbprint",	#F18B538D1BE903B6A6F056435B171589CAF36BF2
		tag5:	"NotBefore",	#4/01/2008 19:00:00
		tag6:	"NotAfter",		#12/01/2037 17:59:59
		tag7:	"Issuer",		#CN=thawte Primary Root CA - G3, OU="(c) 2008 thawte, Inc. - For authorized use only", OU=Certification Services Division, O="thawte, Inc.", C=US
		tag8:	"FriendlyName"	#thawte Primary Root CA - G3
	-->
	<!-- Add no spaces or line breaks between <extension> and <![CDATA[ or any content after.
	     It will break the scripts because of parsing issues -->
    <extension><![CDATA[<#
.SYNOPSIS
    Retrieves all root level certificates on the system
.DESCRIPTION
    This script retrieves all root level certificates on the system
	and output's them to the console for the agent to send to the server.

	This script is used to collect all the items from the CERT: drive, which is the users
	certificate library.  They can have System and User certificates.  The return from
	Get-ChildItem cert:\ is a mixed collection of Store locations, Stores and Certificates.
	I store the name of the store location and store for the output of each certificate
	it contains.

.NOTES
Name: GetCertificateInfo
Author: David Stidolph
DateCreated: 6/3/2015

OUTPUT
======
100101 #Event ID
# the following would be on one line with '|' seperating them
LocalMachine #StoreLocation
Root #Store
CN=thawte Primary Root CA - G3, OU="(c) 2008 thawte, Inc. - For authorized use only", OU=Certification Services Division, O="thawte, Inc.", C=US # Subject
600197B746A7EAB4B49AD64B2FF790FB #SerialNumber
F18B538D1BE903B6A6F056435B171589CAF36BF2 #Thumbprint
4/01/2008 19:00:00 #NotBefore
12/01/2037 17:59:59 #NotAfter
CN=thawte Primary Root CA - G3, OU="(c) 2008 thawte, Inc. - For authorized use only", OU=Certification Services Division, O="thawte, Inc.", C=US #Issuer
thawte Primary Root CA - G3 #FriendlyName

#>
$eventID = 100101

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

Function ScanCertificates
{
	$storeLocation = ""
	$store = ""
	$resultSet = CreateResultSet
	$thumbprints = @()
	$allCertInfo = Get-ChildItem -Recurse cert:\
	# We have the collection, so walk through it
	foreach ($cert in $allCertInfo)
	{
		# Use the type of object and get appropriate information
		if ($cert.GetType().FullName -eq "Microsoft.PowerShell.Commands.X509StoreLocation")
		{
			$storeLocation = $cert.LocationName
		}
		elseif ($cert.GetType().FullName -eq "System.Security.Cryptography.X509Certificates.X509Store")
		{
			$store = $cert.Name
		}
		elseif ($cert.GetType().FullName -eq "System.Security.Cryptography.X509Certificates.X509Certificate2")
		{
			if ($thumbprints -match $cert.Thumbprint) {
			} else {
				$row = CreateResultSetRow
				AddRowItem $row $storeLocation
				AddRowItem $row $store
				AddRowItem $row $cert.Subject
				AddRowItem $row $cert.SerialNumber
				AddRowItem $row $cert.Thumbprint
				AddRowItem $row $cert.NotBefore
				AddRowItem $row $cert.NotAfter
				AddRowItem $row $cert.Issuer
				AddRowItem $row $cert.FriendlyName
				AddRow $resultSet $row
				$thumbprints += $cert.Thumbprint
			}
		}
		else
		{
			"Unknown Type in cert collection: $($cert.GetType().FullName)"
		}
	}
	"now we are going to output the result set"
	EmitExtensionResults $eventID $resultSet
}

$gehret = GetEventHandlesForPersistentMode
if ( -not $gehret[0] )
{
	"we are not in 'persistent' mode"
	ScanCertificates
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
		ScanCertificates
	}

	"Leaving script"
	Exit 0
}

# SIG # Begin signature block
# MIITXQYJKoZIhvcNAQcCoIITTjCCE0oCAQExCzAJBgUrDgMCGgUAMGkGCisGAQQB
# gjcCAQSgWzBZMDQGCisGAQQBgjcCAR4wJgIDAQAABBAfzDtgWUsITrck0sYpfvNR
# AgEAAgEAAgEAAgEAAgEAMCEwCQYFKw4DAhoFAAQUsSL4FeLb+sHNyIvmVvVCk1Av
# NlCgghBcMIIE0zCCA7ugAwIBAgIQGNrRniZ96LtKIVjNzGs7SjANBgkqhkiG9w0B
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
# hvcNAQkEMRYEFDoAEmelgGFBJyDnbR6zI6SDQtw3MA0GCSqGSIb3DQEBAQUABIIB
# AG76tz+llLMfHZGUWGXfIzlc/tXOzbSU1Z5MSHWHJYn/puNoZGQJAa2q4Cl82vMC
# BnRtLxBujcT5LxNORTb5TX8PAwcg+f4QmJKenXcFLkthqg0ebMNUPsGTsL2N1wE0
# VYXoci48xcQzw8B83VTxKhD2zIyXxKOHTWMI4JzSL2dCixqQx58aj1tGYrVS6YW4
# eo9H1Dm+6usCo8E68nYwOyYFdaNb6jN4m3P2hLg+ggLfojOsgTtVPQ+//XCjmi9X
# kqbCsOMxHwXBXeIAYDOYU9IYBs0KTDkqtB+sSdprVu7ehr6my6nMCREL77bhFk64
# zzMzIG4K/hogGhdhBpnJDfE=
# SIG # End signature block
]]></extension>
</module>