# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:25:48 2021

@author: ACER
"""


from my_connector import user
from mysql.connector import connection

user1 = user(connection())