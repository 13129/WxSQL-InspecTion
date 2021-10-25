import psycopg2
import os
import sys


def connectPostgreSQL():
    conn = psycopg2.connect(database="postgres", 
                                user="postgres", 
                                password="8693585", 
                                host="192.168.1.95", 
                                port="5432")
    print('connect successful!')
    return conn