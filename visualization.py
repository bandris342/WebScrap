import psycopg2, time, sys

#try to connect to the database
try:
    conn = psycopg2.connect("dbname='WebScrap' user='postgres' host='localhost' password='kortefa'")
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

cur.execute("SELECT * FROM followers ORDER BY time")
data=cur.fetchall()

for row in data:
    print(time.ctime(row[0]), row[1])

cur.close()
conn.close()
