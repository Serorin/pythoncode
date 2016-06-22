#_*_coding:utf-8_*_

import MySQLdb

if __name__=="__main__":
    connectar = MySQLdb.connect(host="localhost",db="pydata",user="pi",password="aaa",charset="utf8")

    cousor = connector.cursor()

    sql = u"insert into test_table values('id1',value1')"
    cursor.execute(sql)

    sql = u"insert into test_table value('id2','value2')"
    cursor.execute(sql)

    connector.commit()

    cursor.close()
    connector.close()
