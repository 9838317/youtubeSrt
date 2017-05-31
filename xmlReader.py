def toSecond(arg):
    minute = str(arg/60)
    second = str(arg%60)

    if   len(minute) <   2:
        minute = '0' + minute + ':'
    elif len(minute) ==  2:
        minute = minute + ':'
        
    if len(second) <   2:
        second = '0'+ second

    return '00:' + minute + second + ':000'

def writeSrt(textInXML):
    
    fileHandler = open('sub.srt','w')
    
    for i in range(len(textInXML)):
        
        timeInfo = textInXML[i].items()
        timeInfoFirst = int(float(timeInfo[0][1]))
        
        if len(timeInfo) == 2:
            timeInfoSecond = int(float(timeInfo[0][1]) + float(timeInfo[1][1]))
        elif len(timeInfo) == 1:
            timeInfoSecond = int(float(timeInfo[0][1]))
        
        fileHandler.write(str( i))
        fileHandler.write('\n')
        fileHandler.write(toSecond(timeInfoFirst) + ' --> ' + toSecond(timeInfoSecond))
        fileHandler.write('\n')
        
        try:
            fileHandler.write(textInXML[i].text)
        except:
            print type(textInXML[i].text)      
        fileHandler.write('\n')
        fileHandler.write('\n')
    fileHandler.close()
    
if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    temp = ET.parse('xl.xml')
    result = temp.findall('text')
    writeSrt(result)
