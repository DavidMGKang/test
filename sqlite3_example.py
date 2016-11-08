import sqlite3
import time
from collections import namedtuple
# from pandas import Series, DataFrame

conn = sqlite3.connect("karas.db")
# Autocommit 사용시:
# conn = sqlite3.connect("test.db", isolation_level=None)

tick = int(time.time())
print(tick)
cur = conn.cursor()
# sql = "insert into customer(name,category,region) values (?, ?, ?)"
# cur.execute(sql, ('홍길동', 1, '서울'))
# sql = 'CREATE TABLE IF NOT EXISTS "RECD_ERRLOG" ("NO" INTEGER PRIMARY KEY NOT NULL, "ErrorType" INTEGER NOT NULL, "ErrorDesc" INTEGER NOT NULL, "SubJobType" INTEGER NOT NULL, "JobID" INTEGER NOT NULL, "Date" INTEGER NOT NULL, "UptimeSec" INTEGER NOT NULL, "PageCount" INTEGER NOT NULL, "PORCount" INTEGER NOT NULL, "IP" TEXT, "Desc" INTEGER NOT NULL, "ScreenShot" BLOB, "LogFileName" TEXT, "ScreenShotSize" INTEGER DEFAULT 0 NOT NULL, "LogTextSize" INTEGER DEFAULT 0 NOT NULL)'


MyStruct = namedtuple("MyStruct",  "No, ErrorType,\
 ErrorDesc,\
 SubJobType,\
 JobID,\
 Date,\
 UptimeSec,\
 PageCount,\
 PORCount,\
 IP,\
 Desc,\
 ScreenShot,\
 LogFileName,\
 ScreenShotSize,\
 LogTextSize")

m=[]


for i in range(10):
    m.append(MyStruct( i, 0x0EFF, 321, 0 , 0,
              int(time.time()), 20, 60, 30, 1 ,
              2, 3, "example1", 70, 20))

# sql = "drop table RECD_ERRLOG"
# sql = "delete from RECD_ERRLOG"
# sql = "select * from RECD_ERRLOG"

for i in range(10):
    print(m[i])
    print(m[i].No)
# print(m[0])
# cur.execute(sql)
#
# rows = cur.fetchall()
# for row in rows:
#     print(row)
#
# with open('./dump.sql', 'w') as f:
#     for line in conn.iterdump():
#         f.write('%s\n' % line)

conn.close()

