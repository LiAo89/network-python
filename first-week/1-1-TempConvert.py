#TempConvert.py
tempStr = input('请输入带有符号的温度值：')
if tempStr[-1] in ['f','F']:
    C =(eval(tempStr[0:-1])- 32)/1.8
    print('转换后的温度是{:.2f}C'.format(C))
elif tempStr[-1] in ['c','C']:
    F =eval(tempStr[0:-1]) *1.8 +32
    print('转换后的温度是{:.2f}F'.format(F))
else:
    print('请输入格式正确的温度。')
