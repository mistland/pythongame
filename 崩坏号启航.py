print "祝愿舰长补给全保底，舰长副本零掉落。"
import time
shipName = "崩坏号"
captain = "舰长"
locatin = "地球"
password = "脱非入欧"
jiancha = raw_input ("请输入密码：")
while jiancha != password:
    print "舰长不会不知道自己的口令的。"
    jiancha = raw_input ("请输入密码：")
print shipName + "启动，舰长您口令输入正确，祝您航行愉快！"
print ""
print "开始启航！" + shipName + ",正在确定位置，我们在" + locatin + "……"
choice = ""
while choice != "返航":
    print "接下来您想做什么？" + captain
    print ""
    print "是一起洗澡呢？"
    time.sleep (1)
    print "还是，一起吃饭呢？"
    time.sleep (1)
    print "还是，要……"
    time.sleep (3)
    print "启航呢!^_^"
    time.sleep (1)
    print "嘿嘿，要是现在就返航，离开我也是可以的。"
    print ""
    choice = raw_input ("面对崩坏号的问题，你选择：")
    if choice == "一起洗澡":
        print "没想到您是这样的人！那就在大海里好好洗去，别上来了。"
        print "（你被踢下了海）"
        time.sleep (1)
        print "舰长卒，坠海而亡。"
        choice = "返航"
    elif choice == "一起吃饭":
        print "您也喜欢喝汽油，吃煤炭啊！来来来，多吃点。"
        print "（你被塞的满满的）"
        time.sleep (1)
        print "舰长卒，中毒而亡。"
        choice = "返航"
    elif choice == "启航":
        will = raw_input ("您打算去哪？")
        print "正在离开" + locatin
        time.sleep (1)
        print "即将到达" + will
        time.sleep (5)
        print "到达" + will
        locatin == will
        c = raw_input ("还继续么？（Y/N）")
        if c == "Y":
            print "抱歉，燃料不足，准备返航。"
            choice = "返航"
        choice = "返航"
    elif choice == "……":
        print "嘿嘿，逗舰长玩呢，我们继续吧！"
        print "（你被舰娘摸了摸头）"
    else:
        print "请输入有效选项。\n\n"
        
