import time, sys
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import numpy

fig = plt.figure()
ax = fig.add_subplot(111)

#db_string = "postgres://tnrgoyky:CQ4Wn1y2KRxe-A3FtA5aiYiwf-jvmgRo@horton.elephantsql.com:5432/tnrgoyky"
db_string = "postgres://postgres:kortefa@localhost:5432/WebScrap"

#try to connect to the database
try:
    db = create_engine(db_string)
except:
    print("I am unable to connect to the database!")
    sys.exit(1)



#check if table exists, if not create it
try:
    db.execute("SELECT EXISTS (SELECT * FROM followers)")
except:
    print("Followers table not exists!")
    sys.exit(1)

NbRows=db.execute("SELECT COUNT(*) FROM followers;").fetchone()

FirstTime=db.execute("SELECT time FROM followers ORDER BY time ASC LIMIT 1").fetchone()

LastTime=db.execute("SELECT time FROM followers ORDER BY time DESC LIMIT 1").fetchone()

print("There are %d rows in the database. Data have been collected between %s and %s" % (NbRows[0], time.ctime(FirstTime[0]), time.ctime(LastTime[0])))
print(NbRows)

Tback=int(input("Give me a time in minutes (dTime) to visualize data collected between T-dTime and T:"))*60

result=db.execute("SELECT * FROM followers WHERE time > %s ORDER BY time", LastTime[0] - Tback).fetchall()


#Data plot

data = []
xTickMarks = []

for row in result:
   data.append(int(row[1]))
   xTickMarks.append(time.strftime("%D %H:%M:%S", time.localtime(row[0])))

#necessary variables
ind = numpy.arange(len(data))     #the x locations for XTickers
width = 0.35                      #the width of the bars

#plot the bars
ax.bar(ind, data, width, color='black')


#set axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(min(data)-1, max(data)+1)


ax.set_ylabel('Number of followers')
ax.set_xlabel('Data number')
ax.set_title('Data collected between \n %s and %s\n' % (xTickMarks[0], xTickMarks[len(data)-1]))

#ax.set_xticks(ind+width)
#xtickNames = ax.set_xticklabels(xTickMarks)
#plt.setp(xtickNames, rotation=45, fontsize=10)

plt.show()

