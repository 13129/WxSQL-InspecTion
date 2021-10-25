"""
参数1：字段
参数2：表
参数3：条件
"""

import os
import sys
import psycopg2
from pg_conn import connectPostgreSQL


def connectSQL(conn,SQL):
    cursor = conn.cursor()
    search_com = """{}""".format(SQL)

    cursor.execute(search_com)
    # conn.commit()
    data = cursor.fetchone()
    print(data)

if __name__=='__main__':
    connectSQL(connectPostgreSQL(),"select * from get_serve_page")