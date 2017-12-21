import requests
from lxml import html
pagestring = requests.get('https://twitter.com/emmanuelmacron')
htmlpage = html.fromstring(pagestring.content)
followers = htmlpage.xpath("//@data-count")
print(followers[2])
