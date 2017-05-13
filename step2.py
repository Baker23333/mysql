#coding: utf-8
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    # 连接数据库
    conn = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='9090',
        charset = "utf8",
        db='databaseName',
    )

    # 获取数据库执行游标
    cur = conn.cursor()
f1 = open('/home/czx/Downloads/MySQLfiles/homework/university/department.txt','r')
for line in f1.readlines():
    line = line.strip('/n')
    line = line.split(' ')
    cur.execute("insert into department(dept_name,building,budget) values('%s','%s','%s')" %(line[0], line[1], line[2]))
f1.close()

f2 = open('/home/czx/Downloads/MySQLfiles/homework/university/student.txt','r')
for line in f2.readlines():
    line = line.strip('/n')
    line = line.split(' ')
    line[0]=int(line[0])
    line[3]=int(line[3])
    cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name) values('%d','%s','%s','%d'',%s','%s')" %(line[0], line[1], line[2],line[3],line[4],line[5]))
f2.close()

f3 = open('/home/czx/Downloads/MySQLfiles/homework/university/exam.txt','r')
for line in f3.readlines():
    line = line.strip('/n')
    line = line.split(' ')
    line[0]=int(line[0])
    line[2]=int(line[2])
    cur.execute("insert into exam(student_ID,exam_name,grade) values('%d','%s','%d')" %(line[0], line[1], line[2]))
f3.close()

conn.commit()
cur.close()
conn.close()

