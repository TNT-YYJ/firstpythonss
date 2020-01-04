import urllib.request,re,json
import urllib.parse

posturl='http://www.iqianyue.com/mypost'
postdata=urllib.parse.urlencode({
    'name':'',
    'pass':''
}).encode('utf-8')
req=urllib.request.Request(posturl,postdata)
