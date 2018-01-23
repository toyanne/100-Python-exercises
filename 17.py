#题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定
#比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
#ord()函数主要用来返回对应字符的ascii码，
# chr()主要用来表示ascii码对应的字符他的输入时数字，可以用十进制，也可以用十六进制。

for a in range(ord('x'),ord('z') + 1):
    for b in range(ord('x'),ord('z') + 1):
        for c in range(ord('x'), ord('z') + 1):
            if (a != b) and (a != c) and (b != c):
                if (a != ord('x')) and (c != ord('x')) and (c != ord('z')):
                    print('The order is a--%s\tb--%s\tc--%s' % (chr(a),chr(b),chr(c)))