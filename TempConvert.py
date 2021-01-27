TempStr=input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C=(eval(TempStr[0:-1])-32)/1.8
    print("温度为{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:#使用保留字in判断一个元素是否在列表中
    F=1.8*eval(TempStr[0:-1])+32
    print("温度为{:.2f}F".format(F))
else:
    print("输入错误")
