from html import unescape,escape
from urllib import parse
import base64


def _unicodeToDecode(s="测试"):
    sBytes = s.encode("unicode_escape")
    return (sBytes)

def HtmlHexToEncode(s="&#x6d4b;&#x8bd5;"):
    #html encode hex
    htmlEncodeHex = unescape(s)
    return(htmlEncodeHex + "：htmlEncodeHex: " + s)

def HtmlHexToDecode(s="测试"):
    unicodeS = _unicodeToDecode(s)
    byteS = unicodeS.replace(b"\\u",b";&#x")
    newS = byteS[1:]
    return(s + "：htmlDecodeHex：" + str(newS,"utf-8") + ";")

def HtmlDecToEncode(s="&#27979;&#35797;"):
    #html encode dec
    htmlEncodeDec = unescape(s)
    return(htmlEncodeDec + "：htmlEncodeDec：" + s)

def HtmlDecToDecode(s="测试"):
    unicodeS = _unicodeToDecode(s)
    byteS = unicodeS.split(b"\\u")
    resultS = ""
    for i in byteS[1:]:
        dec = int(b"0x" + i,16)
        decS = str(dec)
        resultS += "&#" + decS + ";"
    
    return(s + "：htmlDecodeDec：" + resultS)


def unicodeToEncode(u="\u6d4b\u8bd5"):
    #print((u.encode()))
    # unicode to byte and raw
    uTob = u.encode('raw_unicode_escape')
    return(u + ": unicodeToEncode：" + str(uTob,"utf-8" ))

def unicodeToDecode(s="测试"):
    sBytes = s.encode("unicode_escape")
    return (s + "：unicodeToDecode：" + str(sBytes,"utf-8"))


def UrlToEncode(url="%E6%B5%8B%E8%AF%95"):
    #url encode and decode
    #url = "%E6%B5%8B%E8%AF%95"
    return(parse.unquote(url) + "：urlEncode：" + url)



def UrlToDecode(s="测试"):
    a = ""
    unicodeToHex = s.encode().hex()
    for i in range(len(unicodeToHex)):
        if i%2 == 0:
            a += "%"
        a += unicodeToHex[i]
    return(s + "：urlDecode：" + a)

def StrToBase64(s="测试"):
    #s = "测试"
    byte_s = bytes(s,"utf-8")
    byteBase64 = base64.b64encode(byte_s)
    strBase64 = byteBase64.decode()
    return(s + "：StrToBase64：" + strBase64)

def Base64ToStr(s="5rWL6K+V"):
    utf8S = base64.b64decode(s)
    t = utf8S.decode()
    return(t + "：Base64ToStr：" + s)




if __name__ == "__main__":
    htmlHex = "&#x4e2d;&#x56fd;"
    print(HtmlHexToEncode())
    print(HtmlHexToDecode())
    
    htmlDex = ""
    print(HtmlDecToEncode())
    print(HtmlDecToDecode())
    
    print(unicodeToEncode())
    print(unicodeToDecode())
    
    url = "%E4%B8%AD%E5%9B%BD"
    print(UrlToEncode())
    s = "中国"
    print(UrlToDecode())
    
    print(StrToBase64())
    #print(_unicodeToDecode())
    print(Base64ToStr())
    
    
    

