#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 5 02:20:22 2020
Project : Realistics Data Generation For Address Book Project To Do Load Test
@author: Nilesh Pise

"""

from faker import Faker
from pymysql import connect
from pymysql import cursors
from pymysql.cursors import DictCursor
from datetime import datetime
from datetime import timedelta 
from datetime import date
from random import choice, randint
import pandas as pd
import numpy as np


fake = Faker('en_IN')

host = 'localhost'
user_db = 'root'
password_db = ''
db = 'addressbook'

def phone_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)



def tbl_contacts():
    first_name = fake.first_name()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address()
    contact_no1 = phone_number(10)
    contact_no2 = phone_number(10)
    email_address = first_name + str(phone_number(5)) + "@gmail.com"
    profile_pic = "var/Images/" + last_name + ".jpeg"


    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        cart_queery = "INSERT INTO `tbl_contacts`(`first_name`, `middle_name`, `last_name`, `address`, `contact_no1`, `contact_no2`, `email_address`, `profile_pic`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(cart_queery,(first_name, middle_name, last_name, address, contact_no1, contact_no2, email_address, profile_pic))
        connection.commit()
    except:
        None
        
for i in range(1000):
    tbl_contacts()
    print("{} Records Inserted.".format(i))

