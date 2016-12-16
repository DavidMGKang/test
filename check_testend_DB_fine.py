#!/bin/python

import sqlite3, os, sys

commands_list = \
["delete from RECD_ERRLOG",
"delete from RECD_SSIDBOOK",
#"delete from RECD_TIMEZONE",
"delete from RECORD_ENGINE_JIG_COUNT",
"delete from RECD_LAST_FILAMENT",
"delete from RECD_NOZZLEHISTORY",

"delete from INST_ENGINE_GENERAL",
#"delete from INST_MACHINE",
"delete from INST_LOCALCOUNT",
"delete from INST_MACHINECOUNT",
"delete from INST_PRNTHISTORY",
"delete from INST_POWERDOWNSTATUS",

"delete from HIST_GLOBAL_USED",
"delete from HIST_LOCAL_USED",

"insert into INST_ENGINE_GENERAL values (1,0,0,0,0,0,0,0,0,0,0)",
#"insert into INST_MACHINE values ()",
"insert into INST_LOCALCOUNT values (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0)",
"insert into INST_MACHINECOUNT values (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3000000,0,0,0,0)",
"insert into INST_PRNTHISTORY values (1,0,0)",
"insert into INST_POWERDOWNSTATUS values (1,0,0,0,0,0,0,0,0,0,0,0)",

"insert into HIST_GLOBAL_USED values (0,0,0,0,0)",
"insert into HIST_GLOBAL_USED values (1,0,0,0,0)",
"insert into HIST_GLOBAL_USED values (2,0,0,0,0)",
"insert into HIST_GLOBAL_USED values (3,0,0,0,0)",
"insert into HIST_GLOBAL_USED values (4,0,0,0,0)",
"insert into HIST_GLOBAL_USED values (5,0,0,0,0)",

"insert into HIST_LOCAL_USED values (0,0,0,0,0)",
"insert into HIST_LOCAL_USED values (1,0,0,0,0)",
"insert into HIST_LOCAL_USED values (2,0,0,0,0)",
"insert into HIST_LOCAL_USED values (3,0,0,0,0)",
"insert into HIST_LOCAL_USED values (4,0,0,0,0)",
"insert into HIST_LOCAL_USED values (5,0,0,0,0)",]

check_list = \
["select * from RECD_ERRLOG;",
"select * from RECD_SSIDBOOK;",
# "select * from RECD_TIMEZONE;",
"select * from RECORD_ENGINE_JIG_COUNT;",
"select * from RECD_LAST_FILAMENT;",
"select * from RECD_NOZZLEHISTORY;",
"select * from INST_ENGINE_GENERAL;",
# "select * from INST_MACHINE;",
"select * from INST_LOCALCOUNT;",
"select * from INST_MACHINECOUNT;",
"select * from INST_PRNTHISTORY;",
"select * from INST_POWERDOWNSTATUS;",
"select * from HIST_GLOBAL_USED;",
"select * from HIST_LOCAL_USED;"]

pwd="/home/kangmg/check_Rodin_testend_fine"
dbName='karas2.db'

if len(sys.argv)>1:
	conn = sqlite3.connect(pwd+'/'+sys.argv[1]);
else:
	conn = sqlite3.connect(pwd+'/'+dbName);

cur = conn.cursor()

for i in range(len(commands_list)):
	# print(commands_list[i])
	cur.execute(commands_list[i])


for i in range(len(check_list)):
	cur.execute(check_list[i])
	print(check_list[i])
	names = [description[0] for description in cur.description]
	print(names)
	rows = cur.fetchall()
	for row in rows:
	    print(row)
	print("\n")



with open('./dump.sql', 'w') as f:
    for line in conn.iterdump():
        f.write('%s\n' % line)


conn.close()
