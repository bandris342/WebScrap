import requests, time, sys
from sqlalchemy import create_engine
from lxml import html


#db_string = "postgres://tnrgoyky:CQ4Wn1y2KRxe-A3FtA5aiYiwf-jvmgRo@horton.elephantsql.com:5432/tnrgoyky"
db_string = "postgres://postgres:kortefa@localhost:5432/WebScrap"

#try to connect to the database
try:
    db = create_engine(db_string)
except:
    print("I am unable to connect to the database!")
    sys.exit(1)


#check if table exists, if not, create it
db.execute("CREATE TABLE IF NOT EXISTS followers (time integer PRIMARY KEY, count integer);")

try:
    while True:
        pagestring = requests.get('https://twitter.com/emmanuelmacron')
        CurrTime=int(time.time())
        htmlpage = html.fromstring(pagestring.content)
        followers = int(htmlpage.xpath("//li[@class='ProfileNav-item ProfileNav-item--followers']//@data-count")[0])
        db.execute("INSERT INTO followers (time, count) VALUES (%s, %s);", (CurrTime, followers))
        print(time.ctime(CurrTime), followers)
        time.sleep(2)
except KeyboardInterrupt:
    pass
