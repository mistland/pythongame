print "当你进入图书馆，进门就见到图书馆看板娘跟你说话。"
again = "yes"
while again == "yes":
    talk = raw_input ("“欢迎来到培华图书馆！”\n“借书还是还书？^_^”\n")
    if talk == "借书":
        print "两边借还机"
    elif talk == "还书":
        print "你个狗！还书不要来前台，两边借还机就可以借。"
    else:
        print "你个狗！"
    again = raw_input ("你还聊么？（yes/no）")

