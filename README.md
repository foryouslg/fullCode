# fullCode
>encode and decode

`$ python fullEncode.py`
```
测试：htmlEncodeHex: &#x6d4b;&#x8bd5;
测试：htmlDecodeHex：&#x6d4b;&#x8bd5;
测试：htmlEncodeDec：&#27979;&#35797;
测试：htmlDecodeDec：&#27979;&#35797;
测试: unicodeToEncode：\u6d4b\u8bd5
测试：unicodeToDecode：\u6d4b\u8bd5
中国：urlEncode：%E4%B8%AD%E5%9B%BD
中国：urlDecode：%e4%b8%ad%e5%9b%bd
测试：StrToBase64：5rWL6K+V
测试：Base64ToStr：5rWL6K+V
```
```
$ fullEncode.py -h
Usage: fullEncode.py -h
           -a        --HtmlToHexE "&#x6d4b;&#x8bd5;"
           -b        --HtmlToHexD  测试
           -c        --HtmlToDecE "&#20013;&#22269;"
           -d        --HtmlToDecD 中国
           -e        --UnToE "\u4e2d\u6587"
           -f        --UnToD 中文
           -g        --UrlToE "%e4%b8%ad"
           -i        --UrlToD 首页
           -j        --StrToB64 加密
           -k        --B64ToStr "5Yqg5a+G"
```
```
$ fullEncode.py -e "\u4e2d\u6587"
中文: unicodeToEncode：\u4e2d\u6587
```
```

$ fullEncode.py --HtmlToHexE "&#x6d4b;&#x8bd5;"
测试：htmlEncodeHex: &#x6d4b;&#x8bd5;

$ fullEncode.py --UnToD 中
中：unicodeToDecode：\u4e2d

$ fullEncode.py --UnToE "\u4e2d"
中: unicodeToEncode：\u4e2d

$ fullEncode.py --UrlToD "首页"
首页：urlDecode：%e9%a6%96%e9%a1%b5

$ fullEncode.py --UrlToE "%e9%a6%96%e9%a1%b5"
首页：urlEncode：%e9%a6%96%e9%a1%b5

$ fullEncode.py --StrToB64 "国"
国：StrToBase64：5Zu9

$ fullEncode.py --B64ToStr 5Zu9
国：Base64ToStr：5Zu9
```
