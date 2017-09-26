#校验手机号厂商
def verify():
    CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
    CN_union = [130, 131, 132, 155, 156, 185, 145, 176, 1709]
    CN_telecom = [133, 153, 180, 181, 189, 177, 1700]
    num=input("请输入要校验的号码：")
    num=str(num)
    print(num)
    if len(num)!=11:
        print("您输入的号码长度不对！请重新输入")
        return
    elif len(num)==11:
        CN_mobile=str(CN_mobile)
        CN_union=str(CN_union)
        CN_telecom=str(CN_telecom)
        fournum=num[:4]
        print(fournum)
        threenum=num[:3]
        print(threenum)
        if fournum in CN_mobile:
            print('您的号码是中国移动的!')
        elif fournum in CN_union:
            print('您的号码是中国联通的！')
        elif fournum in CN_telecom:
            print('您的号码是中国电信的！')
        elif threenum in CN_mobile:
            print('您的号码是中国移动的！')
        elif threenum in CN_union:
            print('您的号码是中国联通的！')
        elif threenum in CN_telecom:
            print('您的号码是中国电信的！')
        else:
            print("发生未知错误！")
            return

verify()

