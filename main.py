from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Ted.db"))

#creating our first table
class Student(Model):
    stud_name = CharField()
    stud_email = CharField()
    stud_password = CharField()
    class Meta:
        database = db

Student.create_table(fail_silently=True)


class Product(Model):
    prod_price = CharField()
    prod_quantity = CharField()
    prod_description = CharField()
    prod_color = CharField
    class Meta:
        database = db

Product.create_table(fail_silently=True)

class User(Model):
    users_name = CharField()
    users_phone = CharField
    users_email = CharField()
    users_password = CharField()
    class Meta:
        database = db

User.create_table(fail_silently=True)

