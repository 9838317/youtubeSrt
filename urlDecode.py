"""
This program is to transfer a raw url to human readable url.
"""

dicRe = {'+':'%2B',' ':'%20','/':'%2F','?':'%3F','%':'%25','#':'%23','&':'%26','=':'%3D', ':': '%3A',',':'%2C'}
dicIn = {'%25': '%', '%26': '&', '%20': ' ', '%23': '#', '%3F': '?', '%2F': '/', '%3D': '=', '%2B': '+','%3A':':','%2C':','}

def recursionForHttp(URL):
    
    lengthOfLink = len(URL)
    
    i = 0; answer = ''
    
    while i < lengthOfLink:
        if  URL[i]      !=  '%':
                answer      +=  URL[i]
                i           +=  1
        elif URL[i] == '%':
            
            try:
                dicIn.has_key(URL[i:i+3])
                answer  +=  dicIn[URL[i:i+3]]
                i       +=  3
            except:
                pass
            
    if      '%' not in answer:  return answer
        
    elif    '%'     in answer:  return recursionForHttp(answer)
        

