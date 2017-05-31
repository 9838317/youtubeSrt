"""
This code is to grab srt of youtube.
"""


import re
import urllib
import xml.etree.ElementTree as ET
import urlDecode
import xmlReader

#1. get URL address
urlAddress = raw_input('input youtube address!')

if urlAddress == '':
    urlAddress ='https://www.youtube.com/watch?v=7ATGN54sSVQ' 
print urlAddress

#2. open socket, return a object of (html source code)
urllibObjecct = urllib.urlopen(urlAddress)


#3. find the aim strings in urllibObjecct
stringsWithTimedtext = []
for i in urllibObjecct:
    if 'caption_tracks' in i:
        stringsWithTimedtext.append(i)
print 'answer gets',len(stringsWithTimedtext),' length'

#4. get link of all subs.
captionLine = stringsWithTimedtext[0]
originAddress = re.findall('"caption_tracks":"(.+?)"', captionLine)
originAddress = originAddress[0]
originAddress = originAddress.split(',')


#5. get link of en.
for i in originAddress:
    if "en\\" in i:
        encodedTracksCluster = i
print 'this is the en srt\n',encodedTracksCluster

#6. get rid of useless strings of #5
encodedTrack    = re.findall('http.+Den', encodedTracksCluster)
result          = encodedTrack
print result

#7. transcodeURL
transcodedURL = urlDecode.recursionForHttp(result)
print 'transcode Address is the address \n',transcodedURL

#8. read XML
aimUrllibObject = urllib.urlopen(transcodedURL)
aimUrllibObjectToXML = aimUrllibObject.read()

#9. write XML
filehandle = open('xl.xml','w')
for i in aimUrllibObjectToXML:
    filehandle.write(i)
filehandle.close()

 

ETObject = ET.parse('xl.xml')
allText = ETObject.findall('text')
xmlReader.writeSrt(allText)


