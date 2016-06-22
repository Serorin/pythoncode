# -*- coding: utf-8 -*-

class D6_Car1:
    def __init__(self):
        self.num = 0
        self.gas = 0

    def printdate(self):
        print u"車のナンバーは"+str(self.num)+u"です"
        print u"ガソリン量は"+str(self.gas)+u"です"

if __name__=="__main__":
    car1 = D6_Car1()
    car1.num = input("ナンバー：")#printf+scanfな書き方
    car1.gas = input("")#scanfの書き方
    car1.printdate()


    
