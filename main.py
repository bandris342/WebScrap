import requests, time, psycopg2, sys
from lxml import html

def connectdb():
    global conn, cur
    #try to connect to the database
    try:
#       conn = psycopg2.connect("dbname='WebScrap' user='postgres' host='localhost' password='kortefa'")
        conn = psycopg2.connect("dbname='tnrgoyky' user='tnrgoyky' host='horton.elephantsql.com' password='CQ4Wn1y2KRxe-A3FtA5aiYiwf-jvmgRo'")
    except:
        print("I am unable to connect to the database!")
        sys.exit(1)
    cur = conn.cursor()

connectdb()

#check if table exists, if not, create it
cur.execute("CREATE TABLE IF NOT EXISTS followers (time integer PRIMARY KEY, count integer);")

try:
    while True:
        pagestring = requests.get('https://twitter.com/emmanuelmacron')
        CurrTime=int(time.time())
        htmlpage = html.fromstring(pagestring.content)
        followers = int(htmlpage.xpath("//li[@class='ProfileNav-item ProfileNav-item--followers']//@data-count")[0])
        cur.execute("INSERT INTO followers (time, count) VALUES (%s, %s);", (CurrTime, followers))
        conn.commit()
        print(time.ctime(CurrTime), followers)
        time.sleep(2)
except KeyboardInterrupt:
    cur.close()
    conn.close()
    pass
