<?xml version="1.0" encoding="UTF-8"?>
<module>
    <name>Monitor Startup Points</name>
    <description>Watch for changes in Startup sequences</description>
    <platforms>
	<!-- 1-OS X; 2-windows; 3-Linux -->
        <platform>2</platform>
    </platforms>
    <parameters>
	<!-- None -->
    </parameters>
	<!-- Output:
         EventID: 100310                                       #event ID
         tag0: "Registry"                                      #Registry or File
         tag1: "SOFTWARE\Microsoft\Windows\CurrentVersion\Run" #Registry Key or File Path that had the modification
         tag2: "Add"                                           #Add or Remove
         tag3: "googletalk"                                    #Name of Item
         tag4: "Value"                                         #Command added
	-->
	<!-- Add no spaces or line breaks between <extension> and <![CDATA[ or any content after.  
	     It will break the scripts because of parsing issues -->
<extension><![CDATA[<#PERSISTENT
.SYNOPSIS
    Watch for startup changes in the registry and file system
.DESCRIPTION
    This script reads startup registry keys and file directories and monitors
    for changes while it runs.

	The script emits a record if it detects a change.
	
.NOTES
Name: WatchStartups
Author: David Stidolph
DateCreated: 12/14/2015

OUTPUT
======
100310 #Event ID
# the following would be on one line with '|' seperating them
Registry                                      #Registry or File
SOFTWARE\Microsoft\Windows\CurrentVersion\Run #Registry Key or File Path that had the modification
Add                                           #Add or Remove
Name                                          #Name of Item
Value                                         #Command added
#>

$eventID = 100310

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

function Get-RegKeyValues
{
    Param([Parameter(Mandatory=$true)] [string]$path)
    Push-Location
    Set-Location -Path $path
    Get-Item . |
    Select-Object -ExpandProperty property |
    ForEach-Object {
        New-Object psobject -Property @{"property"=$_;
        "Value" = (Get-ItemProperty -Path . -Name $_).$_}
    }
    Pop-Location
}

function Get-RegKeys
{
    Param([Parameter(Mandatory=$true)] [string]$path)
    Push-Location
    Set-Location -Path $path
    Get-Item . |
    Select-Object -ExpandProperty property |
    ForEach-Object {
        New-Object psobject -Property @{"property"=$_;
        "Value" = (Get-ItemProperty -Path . -Name $_).$_}
    }
    Pop-Location
}

function HandleEvent($event)
{
	Write-Host "Inside HandleEvent: ComputerName: $($event.ComputerName)"
	Write-Host "Inside HandleEvent: EventIdentifier: $($event.EventIdentifier)"
	Write-Host "Inside HandleEvent: RunspaceId: $($event.RunspaceId)"
	Write-Host "Inside HandleEvent: Sender: $($event.Sender)"
	Write-Host "Inside HandleEvent: SourceArgs: $($event.SourceArgs)"
	Write-Host "Inside HandleEvent: SourceEventArgs: $($event.SourceEventArgs)"
	Write-Host "Inside HandleEvent: SourceIdentifier: $($event.SourceIdentifier)"
	Write-Host "Inside HandleEvent: TimeGenerated: $($event.TimeGenerated)"
    $data = $event.MessageData
    $keyPath = $data[0]
    $query = $data[1]
    Write-Host "Event Name: $keyPath"
    $originalScan = $data[2]
    Write-Host "OriginalScan: $originalScan"
	$currentScan = Get-RegKeyValues -path "hklm:\$keyPath"
    Write-Host "CurrentScan: $currentScan"
    
    if ($currentScan -eq $null) {
        Write-Host "CurrentScan is null"
        if ($originalScan -ne $null) {
            Write-Host "OriginalScan is non-null"
            foreach ($item in $originalScan) {
                $resultSet = CreateResultSet
                $row = CreateResultSetRow
                AddRowItem $row "Registry"
                AddRowItem $row $keyPath
                AddRowItem $row "Remove"
                AddRowItem $row $item.property
                AddRowItem $row $item.value
                AddRow $resultSet $row
                EmitExtensionResults $eventID $resultSet
            }
        }
    }
    elseif ($originalScan -eq $null) {
        // Already know $currentScan is NOT null or previous
        Write-Host "OriginalScan was null, CurrentScan is non-null"
        foreach ($item in $currentScan) {
            $resultSet = CreateResultSet
            $row = CreateResultSetRow
            AddRowItem $row "Registry"
            AddRowItem $row $keyPath
            AddRowItem $row "Add"
            AddRowItem $row $item.property
            AddRowItem $row $item.value
            AddRow $resultSet $row
            EmitExtensionResults $eventID $resultSet
        }
    }
    else {
    	compare-object -ReferenceObject $originalScan -DifferenceObject $currentScan | ForEach {
            Write-Host "Inside compare-object"
            if ($_.SideIndicator -eq "<=") {
                Write-Host "$($_.InputObject.property) has been removed"
                $resultSet = CreateResultSet
                $row = CreateResultSetRow
                AddRowItem $row "Registry"
                AddRowItem $row $keyPath
                AddRowItem $row "Remove"
                AddRowItem $row $_.InputObject.property
                AddRowItem $row $_.InputObject.value
                AddRow $resultSet $row
                EmitExtensionResults $eventID $resultSet
            }
            if ($_.SideIndicator -eq "=>") {
                Write-Host "$($_.InputObject.property) has been added"
                $resultSet = CreateResultSet
                $row = CreateResultSetRow
                AddRowItem $row "Registry"
                AddRowItem $row $keyPath
                AddRowItem $row "Add"
                AddRowItem $row $_.InputObject.property
                AddRowItem $row $_.InputObject.value
                AddRow $resultSet $row
                EmitExtensionResults $eventID $resultSet
            }
        }
    }
    $sourceName = $event.SourceIdentifier
    $newData = @($keyPath, $query, $currentScan)
    Remove-Event -SourceIdentifier $sourceName -ErrorAction SilentlyContinue
    Unregister-Event -SourceIdentifier $sourceName
    Register-WmiEvent -Query $query -SourceIdentifier $sourceName -Namespace 'root\default' -MessageData $newData
}

function AddValueMonitoring( [string]$sourceName, [string] $wideKeyPath)
{
	$keyPath = $wideKeyPath.Replace("\\","\")
	$query = "Select * from RegistryKeyChangeEvent where Hive='HKEY_LOCAL_MACHINE' AND KeyPath='$wideKeyPath'"
    if (Test-Path "hklm:\$keyPath") {
        Write-Host "Path $keyPath is being monitored for changes"
    	$currentKeyValues = Get-RegKeyValues "hklm:\$keyPath"
        if ($currentKeyValues -eq $null) {
            Write-Host "Get-RegKeyValues for $keyPath is NULL"
        }
        $data = @($keyPath, $query, $currentKeyValues)
        Register-WmiEvent -Query $query -SourceIdentifier $sourceName -Namespace 'root\default' -MessageData $data
    }
    else {
        Write-Host "Path $keyPath not found, cannot monitor for changes"
    }
}

function AddKeyMonitoring( [string]$sourceName, [string] $wideKeyPath)
{
	$keyPath = $wideKeyPath.Replace("\\","\")
	$query = "Select * from RegistryTreeChangeEvent where Hive='HKEY_LOCAL_MACHINE' AND KeyPath='$wideKeyPath'"
    if (Test-Path "hklm:\$keyPath") {
        Write-Host "Path $keyPath is being monitored for changes"
    	$currentKeyValues = Get-RegKeys "hklm:\$keyPath"
        if ($currentKeyValues -eq $null) {
            Write-Host "Get-RegKeyValues for $keyPath is NULL"
        }
        $data = @($keyPath, $query, $currentKeyValues)
        Register-WmiEvent -Query $query -SourceIdentifier $sourceName -Namespace 'root\default' -MessageData $data
    }
    else {
        Write-Host "Path $keyPath not found, cannot monitor for changes"
    }
}

Function CheckForChanges
{
	$myevent = wait-event -Timeout 1
	if ($null -ne $myevent) {
        if ($myevent.count) {
            Write-Host "Multiple events: $($myevent.count)"
            foreach($e in $myevent)
            {
                if (($e.TimeGenerated -ne $lastEventTimeGenerated) -or
                    ($e.EventIdentifier -ne $lastEventIdentifier) -or
                    ($e.SourceIdentifier -ne $lastEventSourceIdentifier))
                {
                    if ($e.TimeGenerated -ne $lastEventTimeGenerated) {
                        Write-Host "TimeGenerated is different"
                    }
                    if ($e.EventIdentifier -ne $lastEventIdentifier) {
                        Write-Host "EventIdentifier is different"
                    }
                    if ($e.SourceIdentifier -ne $lastEventSourceIdentifier) {
                        Write-Host "SourceIdentifier is different"
                    }
                        
                    HandleEvent($e);
                    $lastEventIdentifier = $e.EventIdentifier
                    $lastEventSourceIdentifier = $e.SourceIdentifier
                    $lastEventTimeGenerated = $e.TimeGenerated
                }
                else {
                    Write-Host "Skipping multiple single event"
                }
            }
        }
        else 
        {
            Write-Host "Single Event"
            if (($myevent.TimeGenerated -ne $lastEventTimeGenerated) -or
                ($myevent.EventIdentifier -ne $lastEventIdentifier) -or
                ($myevent.SourceIdentifier -ne $lastEventSourceIdentifier))
            {
                if ($e.TimeGenerated -ne $lastEventTimeGenerated) {
                    Write-Host "TimeGenerated is different"
                }
                if ($e.EventIdentifier -ne $lastEventIdentifier) {
                    Write-Host "EventIdentifier is different"
                }
                if ($e.SourceIdentifier -ne $lastEventSourceIdentifier) {
                    Write-Host "SourceIdentifier is different"
                }
                HandleEvent($myEvent)
                $lastEventIdentifier = $myevent.EventIdentifier
                $lastEventSourceIdentifier = $myevent.SourceIdentifier
                $lastEventTimeGenerated = $myevent.TimeGenerated
            }
            else {
                Write-Host "Skipping duplicate single event"
            }
        }
    }
}

Get-Event | Remove-Event
Get-EventSubscriber | Unregister-Event 

AddValueMonitoring "SimpleRun32" "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run"
AddValueMonitoring "SimpleRun64" "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
#AddValueMonitoring "PoliciesExplorer" "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run"
#AddValueMonitoring "RunServices64" "Software\\Microsoft\\Windows\\CurrentVersion\\RunServices"
#$AddValueMonitoring "RunServices32" "Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunServices"
#AddValueMonitoring "TerminalStartup" "System\\CurrentControlSet\\Control\\Terminal Server\\Wds\\rdpwd\\StartupPrograms"
#AddValueMonitoring "SimpleRunTerminal" "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
AddValueMonitoring "RunOnce64" "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce"
AddValueMonitoring "RunOnce32" "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnce"
AddValueMonitoring "RunOnceTerminal" "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Runonce"
#AddValueMonitoring "InstalledComponents64" "SOFTWARE\\Microsoft\\Active Setup\\Installed Components"
#AddValueMonitoring "InstalledComponents32" "SOFTWARE\\Wow6432Node\\Microsoft\\Active Setup\\Installed Components"
#AddValueMonitoring "ProtocolFilter" "SOFTWARE\\Classes\\Protocols\\Filter"
#AddValueMonitoring "ProtocolHandler" "SOFTWARE\\Classes\\Protocols\\Handler"
#AddValueMonitoring "ShellServiceObjects64" "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellServiceObjects"
#AddValueMonitoring "ShellServiceObjects32" "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellServiceObjects"
AddValueMonitoring "WinLogon" "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon"
AddValueMonitoring "ShellExecuteHooks64" "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellExecuteHooks"
AddValueMonitoring "ShellExecuteHooks32" "Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellExecuteHooks"
AddValueMonitoring "Drivers64" "Software\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32"
AddValueMonitoring "Drivers32" "Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32"
#AddValueMonitoring "ImageFileExeOptions64" "Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options"
#AddValueMonitoring "ImageFileExeOptions32" "Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options"

$gehret = GetEventHandlesForPersistentMode
if ( -not $gehret[0] )
{
    Write-Host "Monitoring set up, waiting for modification event signal, or end"
    Write-Host "Press 'q' to exit"
    while ($true) {
        CheckForChanges
        if ($Host.UI.RawUI.KeyAvailable -and ("q" -eq $Host.UI.RawUI.ReadKey("IncludeKeyUp,NoEcho").Character)) {
            Write-Host "Exiting now, don't try to stop me...." -Background DarkRed
            break;
        }
    }
}
else
{
    Write-Host "Running in context of Agent, wait for Begin Event"
	$evtBegin = $gehret[1] #(just for readability)
	$evtEnd = $gehret[2] #(just for readability)
	if ( $evtBegin.WaitOne() )
	{
        Write-Host "Begin Event Set"
        while (!$evtEnd.WaitOne(1000) )
        {
            CheckForChanges
        }
    }
    Write-Host "End Event set - exiting"
}

Unregister-Event -SourceIdentifier "SimpleRun32"
Unregister-Event -SourceIdentifier "SimpleRun64"
#Unregister-Event -SourceIdentifier "PoliciesExplorer"
#Unregister-Event -SourceIdentifier "RunServices64"
#Unregister-Event -SourceIdentifier "RunServices32"
#Unregister-Event -SourceIdentifier "TerminalStartup"
#Unregister-Event -SourceIdentifier "SimpleRunTerminal"
Unregister-Event -SourceIdentifier "RunOnce64"
Unregister-Event -SourceIdentifier "RunOnce32"
Unregister-Event -SourceIdentifier "RunOnceTerminal"
#Unregister-Event -SourceIdentifier "InstalledComponents64"
#Unregister-Event -SourceIdentifier "InstalledComponents32"
#Unregister-Event -SourceIdentifier "ProtocolFilter"
#Unregister-Event -SourceIdentifier "ProtocolHandler"
#Unregister-Event -SourceIdentifier "ShellServiceObjects64"
#Unregister-Event -SourceIdentifier "ShellServiceObjects32"
Unregister-Event -SourceIdentifier "WinLogon"
Unregister-Event -SourceIdentifier "ShellExecuteHooks64"
Unregister-Event -SourceIdentifier "ShellExecuteHooks32"
Unregister-Event -SourceIdentifier "Drivers64"
Unregister-Event -SourceIdentifier "Drivers32"
#Unregister-Event -SourceIdentifier "ImageFileExeOptions64"
#Unregister-Event -SourceIdentifier "ImageFileExeOptions32"


# SIG # Begin signature block
# MIITXQYJKoZIhvcNAQcCoIITTjCCE0oCAQExCzAJBgUrDgMCGgUAMGkGCisGAQQB
# gjcCAQSgWzBZMDQGCisGAQQBgjcCAR4wJgIDAQAABBAfzDtgWUsITrck0sYpfvNR
# AgEAAgEAAgEAAgEAAgEAMCEwCQYFKw4DAhoFAAQUAZox1Rifk2oZQZvcWXqRELK5
# 3LWgghBcMIIE0zCCA7ugAwIBAgIQGNrRniZ96LtKIVjNzGs7SjANBgkqhkiG9w0B
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
# hvcNAQkEMRYEFPux7hFRRzgryX4wLYDXtryuBz4LMA0GCSqGSIb3DQEBAQUABIIB
# ADFfpa1JbteAawlvfQNKPG0BUWYCfiy+FZDVvSgQOKTjpPEwPJ/hUnDSqcRkcNvN
# OvDTluAo1VFdb0wX1gEbNXA8ekOArtlVTByEeEWvGyvDVqyY1s9ch35iX2dMK952
# 04SlC3wIAZSWoP09rWHs217ivLC1VvkY7+RnYesCR1Nuvzp2QRNZYXsLJP2Xtcyh
# Q/PAoFyjlMSoZX3c+WMxg/TlWeOBb1Oss9XIvimCHzXvQyicdrymRtPCxKdc+718
# 5T2WS1nSyZkKiIO9dkt+qIedcIBnR0+KVaqLSHre93qcjIi3UGBkVvcCIX6gMxrz
# n/Yw6dwpAeo08CExLJo5V1Q=
# SIG # End signature block
]]></extension>
</module>