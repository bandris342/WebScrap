import requests, time
from lxml import html

try:
    while True:
        pagestring = requests.get('https://twitter.com/emmanuelmacron')
        CurrTime=time.localtime()
        htmlpage = html.fromstring(pagestring.content)
        followers = int(htmlpage.xpath("//li[@class='ProfileNav-item ProfileNav-item--followers']//@data-count")[0])
        print(time.strftime("%Y-%m-%d %H:%M:%S", CurrTime), followers)
        time.sleep(2)
except KeyboardInterrupt:
    pass
