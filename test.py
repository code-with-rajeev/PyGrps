# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:51:02 2020

@author: ACER
"""


#####################################
#    test for reqirements           #
#####################################

import importlib
__requirements__ = ['tkinter','string']
__missing__ = []
for modules in __requirements__:
    try:
        importlib.import_module(modules)
    except ImportError:
        print(f"no such module named : {modules}")
        __missing__.append(modules)
def module_checker():
    return __missing__
import time

print("please wait......    :)")
time.sleep(1)
print("\n \n \nchecking_requirements......")
time.sleep(1)
x = module_checker()
if x == []:
    print("Requirement satisfied____")
    time.sleep(1)
    import interpreter 
else:
    print("Oops! some modules are missing \n can't use as GUI")
    for i in x:
        print(i)
    time.sleep(1)
    from grps import start_normal as start
    
