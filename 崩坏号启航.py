print "ףԸ��������ȫ���ף�������������䡣"
import time
shipName = "������"
captain = "����"
locatin = "����"
password = "�ѷ���ŷ"
jiancha = raw_input ("���������룺")
while jiancha != password:
    print "�������᲻֪���Լ��Ŀ���ġ�"
    jiancha = raw_input ("���������룺")
print shipName + "����������������������ȷ��ף��������죡"
print ""
print "��ʼ������" + shipName + ",����ȷ��λ�ã�������" + locatin + "����"
choice = ""
while choice != "����":
    print "������������ʲô��" + captain
    print ""
    print "��һ��ϴ���أ�"
    time.sleep (1)
    print "���ǣ�һ��Է��أ�"
    time.sleep (1)
    print "���ǣ�Ҫ����"
    time.sleep (3)
    print "������!^_^"
    time.sleep (1)
    print "�ٺ٣�Ҫ�����ھͷ������뿪��Ҳ�ǿ��Եġ�"
    print ""
    choice = raw_input ("��Ա����ŵ����⣬��ѡ��")
    if choice == "һ��ϴ��":
        print "û�뵽�����������ˣ��Ǿ��ڴ���ú�ϴȥ���������ˡ�"
        print "���㱻�����˺���"
        time.sleep (1)
        print "�����䣬׹��������"
        choice = "����"
    elif choice == "һ��Է�":
        print "��Ҳϲ�������ͣ���ú̿��������������Ե㡣"
        print "���㱻���������ģ�"
        time.sleep (1)
        print "�����䣬�ж�������"
        choice = "����"
    elif choice == "����":
        will = raw_input ("������ȥ�ģ�")
        print "�����뿪" + locatin
        time.sleep (1)
        print "��������" + will
        time.sleep (5)
        print "����" + will
        locatin == will
        c = raw_input ("������ô����Y/N��")
        if c == "Y":
            print "��Ǹ��ȼ�ϲ��㣬׼��������"
            choice = "����"
        choice = "����"
    elif choice == "����":
        print "�ٺ٣����������أ����Ǽ����ɣ�"
        print "���㱻����������ͷ��"
    else:
        print "��������Чѡ�\n\n"
        
