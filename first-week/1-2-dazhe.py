#jingdong
'''
设计一个强制输入第一个为价格必须为数值，
件数必须为整数
增加计算每ml多少钱，对比相同体积，谁划算
'''

jiaGe = input('请输入该饮料的价格(1件6瓶装)：')
num = input('请输入购买的件数：')
zongShu = int(num) * 6
money = float(jiaGe) * float(num)
if int(money) > 199:
    money = money - 100
    danJia = float(money)/float(zongShu)
else:
    money = money
    danJia = money / float(zongShu)
print("需要支付的{:.2f}".format(money))
print('总数{:.1f}：'.format(zongShu))
print("单价{:.2f}".format(danJia))
print("单价{:.2f}".format(danJia))