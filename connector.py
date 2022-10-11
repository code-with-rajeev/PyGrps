# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 14:35:15 2021

@author: ACER
"""

import warnings
try:
    from mysql.connector import connect
except Exception as a:
    print(f"mysql.connector is missing")

a = connect(user =  "Rajeev",password ="Rajeevbro420@")



class user:
    def __init__(self,connection):
        self.cursor = connection.cursor()
        self.connection = connection
        self.obj = self.cursor
    def drop(self,name):
        self.obj.execute(f"drop database {name}")
    def create(self,name):
        self.obj.execute(f"create database {name}")
        print(name," databases is created")
    def suggestion(self,suggested):
        return f"SUGGESTION : \n{self.suggestion}"
    def show(self):
        self.obj.execute("show databases")
        self.data = self.fetch()
        for i in  self.data:
            print(i)
        return self.data
    def use(self,name):
        self.obj.execute(f"use {name}")
        print(f"using {name}  ...")
        return DBS(name,self)
    def fetch(self):
        return self.obj.fetchall()
class DBS(user):
    def __init__(self,name,database):
        self.obj = database.obj
        self.name = name 
        self.des = None
        self.exist = False
        self.value = None
    def drop(self,name):
        self.obj.execute(f"drop table {name}")
    def create(self,name,property_):
        try:
            self.obj.execute(f"create table {name}({format_(property_)})")
        except Exception as a:
            print(f"\n__Ops ! Error occoured__ \n{a}")
        print(format_(property_))
        print("created a table")
    def show(self):
        self.obj.execute("show tables")
        print("showing tables")
        self.value = self.fetch()
        print(self.value)
        return self.value
    def item(self):
        return len(self.show())
    def fetch(self):
        return self.obj.fetchall()
    def desc(self,name):
        self.obj.execute(f"desc {name}")
        des = self.fetch()
        print(des)
        return des
    def is_exist(self,table_name):
        try:
            self.desc(table_name)
            self.exist = True
        except  Exception as a:
            print(a)
            self.exist = False 
        return True if self.exist else False

    def get(self,table_name):
        if self.is_exist(table_name):
            return Table(table_name)
        else:
            warnings.warn("___YOU ARE ATTEMTING GET ATTRIBUTES OF AN UNEXSISTED TABLE___")

class Table(DBS):
    def __init__(self,name):
        super().__init__(a)
        self.name = name
        self.value = None
    def property(self):
        self.obj.execute(f'desc {self.name}')
        return f"PROPERTIES {self.fetch()}"
    def item(self):
        return len(self.desc(self.name))
    def insert(self,*property_):
        print(f"inserting into '{self.name}' ")
        try:
            self.obj.execute(f"INSERT into {self.name} Values({(',').join([i for i in property_])})" )
        except Exception as a:
            print(f"\n__Ops ! Error occoured__ \n{a}")
            print(f"\nTRY USING :\n   {self.property()}")
    def get(self,*args):
        item = "*" if not args else (",").join([i for i in args])
        print(self.name)
        print(f"showing {item} from {self.name}")
        try:
            self.obj.execute(f"select {item} from {self.name}")
            self.value = self.fetch() if self.fetch() else print("Empty set in row :( \n try another table")
            print(self.value)
        except Exception as y:
            print(f"\nOps ! Error occoured \n{y}")
    def add(self,property_):
        self.obj.execute(f"ALTER TABLE {self.name} ADD {property_}")
        return self.fetch()
    def drop(self,property_):
        self.obj.execute(f"ALTER TABLE {self.name} DROP {property_}")
        return self.fetch()

class formatter:
    def form(text):
        text,new = text.split(","),[]
        for text in text:
            text = text.replace(" c"," char") 
            text = text.replace(" v"," varchar") 
            text = text.replace(" i"," int")
            new.append(text)
        return (",").join(new)
    
format_ = formatter.form

