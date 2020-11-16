import pywhatkit as kit
import sqlite3
import time

conn = sqlite3.connect("new_db.sqlite")
cur = conn.cursor()
sqlstat = "SELECT * FROM contacts;"
cur.execute(sqlstat)
data = cur.fetchall()
for contact in data:
    msg = "Happy Diwali " + contact[1] + "<3"
    num = "+91" + contact[0]
    t = time.localtime()
    msg_time = [int(time.strftime("%H",t)), int(time.strftime("%M",t)) + 1]
    kit.sendwhatmsg(num,msg,msg_time[0],msg_time[1])
