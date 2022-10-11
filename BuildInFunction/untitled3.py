# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:40:07 2020

@author: ACER
"""


from mysql.connector import connect
print(connect)
y = connect(user = "Rajeev", password = "Rajeevbro420@",host = "127.0.0.1",database = "hello")
x = y.cursor()
x.execute("show tables")
x.execute("")
print(x.fetchall())
