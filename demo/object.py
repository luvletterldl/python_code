# file=open("C:/Users/ldl/Desktop/1.txt","w")
# file.write("Hello Python!")
# def gtokg():
#     ing=input("请输入你需要转换的物体的质量是多少g？")
#     outkg=int(ing)/1000
#     return str(outkg)+'kg'
#
# s=gtokg()
# print(s)

# def triangle():
#     a=input("输入a：")
#     b=input("输入b：")
#     a=int(a)
#     b=int(b)
#     # if a<=0:
#     #     print("sorry,para worry")
#     #     return
#     # elif b<=0:
#     #     print("sorry,para worry")
#     if a<=0 or b<=0:
#         print("sorry,para worry")
#         return
#     else:
#         c=a*a+b*b
#         C=c**0.5
#         return C
#
# C=triangle()
# print(C)

# def tixing(b_up,b_down,height):
#     print(1/2*height*(b_down+b_up))
#
# tixing(b_down=5,height=3,b_up=4)

# print(bool('0'))
# 增光='sb'
# print('增光是一个：'+增光)

# for i in range(1,10):
#     for j in range(1,10):
#         print('{} X {} = {}'.format(i,j,i*j))
# for i in range(1,11):
#     file=open("C:/Users/ldl/Desktop/createfile/{}.txt".format(i),'w')

# for i in range(1,101):
#     if (i%2==0):
#         print(i)
# 时间函数
# import datetime
# now = datetime.datetime.now()
# nt=now.strftime('%Y-%m-%d %H:%M:%S')
# print(nt)
#  自己写的
# import random
# def Bs():
#     a=input("请玩家输入您压的注（大或小）：")
#     p=random.randrange(1,7)
#     p1=random.randrange(1,7)
#     p2=random.randrange(1,7)
#     sump=p+p1+p2
#     print(sump)
#     if a == "大" and 11<=sump<=18:
#         print('Lucky! 大 You win！！！')
#     elif a == "小" and 3<=sump<=10:
#         print('Lucky! 小 You win！！！')
#     else:
#         print('您输了！')
#         Bs()
# Bs()

# 答案 更具模块化 更优
import random
def roll_dice(numbers=3,points=None):
    print("<<<ROLL THE DICE!>>>")
    if points is None:
        points = []
    while numbers > 0:
        point=random.randrange(1,7)
        points.append(point)
        numbers=numbers-1
    return points
def roll_result(total):
    isBig=11<= total <=18
    isSmall=3<= total <=10
    if isBig:
        return 'Big'
    if isSmall:
        return 'Small'
def start_game():
    print("<<<<<< GAME STARTS! >>>>>>")
    choices=['Big','Small']
    your_choice=input('Big or Small:')
    if your_choice in choices:
        points=roll_dice()
        total=sum(points)
        youWin=your_choice==roll_result(total)
        if youWin:
            print("The points are",points,'You win!')
        else:
            print("The points are",points,'You lose!')
    else:
        print("Invalid Words")
        start_game()

start_game()