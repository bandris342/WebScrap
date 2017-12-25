import psycopg2, time, sys

#try to connect to the database
try:
#   conn = psycopg2.connect("dbname='WebScrap' user='postgres' host='localhost' password='kortefa'")
    conn = psycopg2.connect("dbname='tnrgoyky' user='tnrgoyky' host='horton.elephantsql.com' password='CQ4Wn1y2KRxe-A3FtA5aiYiwf-jvmgRo'")
except:
    print("I am unable to connect to the database!")
    sys.exit(1)

cur = conn.cursor()

#check if table exists, if not create it
try:
    cur.execute("SELECT EXISTS (SELECT * FROM followers)")
except:
    print("Followers table not exists!")
    sys.exit(1)

CurrTime = int(time.time())
cur.execute("SELECT * FROM followers WHERE time > %s ORDER BY time", (CurrTime-60,))
data=cur.fetchall()

for row in data:
    print(time.ctime(row[0]), row[1])

cur.close()
conn.close()
