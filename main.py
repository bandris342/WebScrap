import requests
from lxml import html
pagestring = requests.get('https://twitter.com/emmanuelmacron')
htmlpage = html.fromstring(pagestring.content)
followers = int(htmlpage.xpath("//li[@class='ProfileNav-item ProfileNav-item--followers']//@data-count")[0])
print(followers)
