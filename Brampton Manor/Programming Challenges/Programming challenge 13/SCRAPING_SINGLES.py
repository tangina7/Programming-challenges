import urllib.request
import html


def read_web(url):
    mybytes = fp.read()## read a html file as bytes
    mystr = mybytes.decode("utf-8") ## decode the bytes to a string
    mystr = html.unescape(mystr) ## for special characters
    return mystr

def get_singles(mystr):
    position = mystr.find('<div class="title">') ## looking for the title html track
    position2 = mystr.find('<div class="artist">')
    count = 1
    while position != -1 and count <= 10 and position2 != -1: ## -1 is returned if the html tag is not found
        start = mystr.find(">",position+len('<div class="title">'))+1 ## find the first ">" after the html title tag
        stop = mystr.find("<",start)                                  ## find the first "<" after the html start tag
 
        a = mystr.find(">",position2+len('<div class="artist">'))+1
        b = mystr.find("<",a)
        
        print(f"{count} - {mystr[start:stop]}")
        print(f"{mystr[a:b]}", "\n")
        position = mystr.find('<div class="title">',stop)
        position2 = mystr.find('<div class="artist">',b)
        
        count += 1
        



if __name__ == "__main__":
    fp = urllib.request.urlopen("https://www.officialcharts.com/charts/singles-chart/")
    web_str = read_web(fp)
    get_singles(web_str)
