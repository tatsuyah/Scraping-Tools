from os import path, mkdir
from urllib import urlretrieve
from urllib2 import URLError, HTTPError
from urlparse import urlparse

f = open('./urls.txt')
pageData = f.read()
url_list = pageData.split('\n')

dirName = "./images/"
isExisting = path.exists(dirName)
if isExisting is False:
  mkdir(dirName)

for url in url_list:
  if len(url) < 1:
    continue
  src_url = url
  tgt_path = path.split(urlparse(src_url).path)[-1]
  tgt_path = dirName + tgt_path
  try:
    print(url)
    urlretrieve(src_url, tgt_path)
  except (HTTPError, URLError, IOError) as e:
    print(e)
