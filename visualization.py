import psycopg2, time

try:
    conn = psycopg2.connect("dbname='WebScrap' user='postgres' host='localhost' password='kortefa'")
except:
    print("I am unable to connect to the database!")
    sys.exit(1)

cur = conn.cursor()

cur.execute("SELECT * FROM followers ORDER BY time")
data=cur.fetchall()

for row in data:
    print(time.ctime(row[0]), row[1])

cur.close()
conn.close()