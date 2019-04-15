from html import unescape,escape
from urllib import parse
import base64
import sys,getopt


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
    uu = u.encode("utf-8")                  #b'\\u4e2d\\u6587'
    uuu = uu.decode("unicode_escape")       #中文
    uTob = u.encode('raw_unicode_escape')   #b'\\u4e2d\\u6587'
    return(uuu + ": unicodeToEncode：" + str(uTob,"utf-8" ))

def unicodeToDecode(s="测试"):
    sBytes = s.encode("unicode_escape")
    return (s + "：unicodeToDecode：" + str(sBytes,"utf-8"))


def UrlToEncode(url="%E6%B5%8B%E8%AF%95"):
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
    byte_s = bytes(s,"utf-8")
    byteBase64 = base64.b64encode(byte_s)
    strBase64 = byteBase64.decode()
    return(s + "：StrToBase64：" + strBase64)

def Base64ToStr(s="5rWL6K+V"):
    utf8S = base64.b64decode(s)
    t = utf8S.decode()
    return(t + "：Base64ToStr：" + s)

def _h():
    print("Usage: fullEncode.py -h")
    print("           -a        --HtmlToHexE \"&#x6d4b;&#x8bd5;\"")
    print("           -b        --HtmlToHexD  测试")
    print("           -c        --HtmlToDecE \"&#20013;&#22269;\"")
    print("           -d        --HtmlToDecD 中国")
    print("           -e        --UnToE \"\\u4e2d\\u6587\"")
    print("           -f        --UnToD 中文")
    print("           -g        --UrlToE \"%e4%b8%ad\"")
    print("           -i        --UrlToD 首页")
    print("           -j        --StrToB64 加密")
    print("           -k        --B64ToStr \"5Yqg5a+G\"")

def main(argv):
    s = ""
    try:
        opts,args = getopt.getopt(argv,"ha:b:c:d:e:f:g:i:j:k:",["HtmlToHexE=","HtmlToHexD=","HtmlToDecE=","HtmlToDecD=",
                                            "UnToE=","UnToD=","UrlToE=","UrlToD=","StrToB64=","B64ToStr="])
    except getopt.GetoptError:
        _h()
        sys.exit(2)

    for opt,arg in opts:
        if opt == "-h":
            _h()
            sys.exit()
            
        elif opt in ("-a","--HtmlToHexE"):
            print(HtmlHexToEncode(arg))
        elif opt in ("-b","--HtmlToHexD"):            
            print(HtmlHexToDecode(arg))
        elif opt in ("-c","--HtmlToDecE"): 
            print(HtmlDecToEncode(arg))
        elif opt in ("-d","--HtmlToDecD"): 
            print(HtmlDecToDecode(arg))
        elif opt in ("-e","--UnToE"): 
            print(unicodeToEncode(arg))
        elif opt in ("-f","--UnToD"): 
            print(unicodeToDecode(arg))

        elif opt in ("-g","--UrlToE"): 
            print(UrlToEncode(arg))
        elif opt in ("-i","--UrlToD"): 
            print(UrlToDecode(arg))
        elif opt in ("-j","--StrToB64"): 
            print(StrToBase64(arg))
        elif opt in ("-k","--B64ToStr"):
            print(Base64ToStr(arg))
    


if __name__ == "__main__":
    main(sys.argv[1:])
    
    

