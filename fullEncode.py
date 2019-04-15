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
    print("           -a        --hToHexE \"&#x6d4b;&#x8bd5;\"")
    print("           -b        --hToHexD  测试")
    print("           -c        --hToDecE \"&#20013;&#22269;\"")
    print("           -d        --hToDecD 中国")
    print("           -e        --uToE \"\\u4e2d\\u6587\"")
    print("           -f        --uToD 中文")
    print("           -g        --urlToE \"%e4%b8%ad\"")
    print("           -i        --urlToD 首页")
    print("           -j        --sToB64 加密")
    print("           -k        --b64ToS \"5Yqg5a+G\"")

def main(argv):
    s = ""
    try:
        opts,args = getopt.getopt(argv,"ha:b:c:d:e:f:g:i:j:k:",["ahToHexE=","bhToHexD=","chToDecE=","dhToDecD=",
                                            "euToE=","fuToD=","gurlToE=","iurlToD=","jsToB64=","kb64ToS="])
    except getopt.GetoptError:
        _h()
        sys.exit(2)

    for opt,arg in opts:
        if opt == "-h":
            _h()
            sys.exit()
            
        elif opt in ("-a","--ahToHexE"):
            print(HtmlHexToEncode(arg))
        elif opt in ("-b","--bhToHexD"):            
            print(HtmlHexToDecode(arg))
        elif opt in ("-c","--chToHexD"): 
            print(HtmlDecToEncode(arg))
        elif opt in ("-d","--dhToHexD"): 
            print(HtmlDecToDecode(arg))
        elif opt in ("-e","--ehToHexD"): 
            print(unicodeToEncode(arg))
        elif opt in ("-f","--fhToHexD"): 
            print(unicodeToDecode(arg))

        elif opt in ("-g","--ghToHexD"): 
            print(UrlToEncode(arg))
        elif opt in ("-i","--ihToHexD"): 
            print(UrlToDecode(arg))
        elif opt in ("-j","--jhToHexD"): 
            print(StrToBase64(arg))
        elif opt in ("-k","--khToHexD"):
            print(Base64ToStr(arg))
    


if __name__ == "__main__":
    main(sys.argv[1:])
    
    

