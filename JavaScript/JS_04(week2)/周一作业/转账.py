# 设计一个“转账”程序，模拟"tom"用户给"jerry"转账200元，
# 一旦转账过程发生异常,则提示“系统发生异常，转账失败”，并回滚事务，
# 如果转账成功，则显示“转账成功”，并查看数据库验证是否真的成功。
import pymysql

conn = pymysql.Connect(
    host='192.168.43.88',
    user='root',
    passwd='root',
    port=3306,
    db='bank',
    charset='utf8',
)
cursor = conn.cursor()
try:
    sql1 = "update user set money=money-200 where id=%d"
    sql2 = "update user set money=money+200 where id=%d"
    cursor.execute(sql1 % 1)  # tom
    cursor.execute(sql2 % 2)  # jerry
    conn.commit()
    print('转账成功')
except Exception:
    conn.rollback()
    print('转账失败')
finally:
    cursor.close()
    conn.cursor()
