# -*- coding: utf-8 -*-

class Parson:
    def __init__(self):
        self.name = raw_input("name=")
        self.age = raw_input("age=")

    def printdata(self):
        print self.name
        print self.age

    def henkou(self,name,age):
        self.name = name
        self.age = age


serori = Parson()
serori.printdata()

aaa = Parson()
aaa.printdata()
serori.printdata()
