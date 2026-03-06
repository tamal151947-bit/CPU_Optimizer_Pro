' CPU Optimizer Pro - Silent Admin Launcher
' This VBScript requests Administrator privileges and launches the app
' Double-click this file to run the app

Set objShell = CreateObject("Shell.Application")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Get the directory where this script is located
strScriptPath = WScript.ScriptFullName
strScriptDir = objFSO.GetParentFolderName(strScriptPath)

' Check if already running as admin (simplified check)
' If not, re-launch with admin privileges
On Error Resume Next
objShell.ShellExecute "python.exe", """" & strScriptDir & "\CPUOptimizer.py""", strScriptDir, "runas", 1
If Err.Number <> 0 Then
    MsgBox "Error: Could not launch CPU Optimizer Pro." & vbCrLf & vbCrLf & _
           "Make sure Python is installed and run:" & vbCrLf & _
           "pip install -r requirements.txt", vbCritical, "CPU Optimizer Pro"
End If
On Error GoTo 0

WScript.Quit
