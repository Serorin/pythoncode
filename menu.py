# -*- coding: utf-8 -*-
while 1:
    print u"注文したいメニューを選択してください"
    print u"1:ポテト 2:ナゲット 3:ハンバーガー 4:チーズバーガー"
    a = input()
    if a == 1:
        print u"Sサイズ150円、Mサイズ270円、Lサイズ310円です"
        break
    elif a == 2:
        print u"5ピース２００円、１５ピース５７０円です"
        break
    elif a == 3:
        print u"100円です"
        break
    elif a == 4:
        print u"130円です"
        break
    else:
        continue
