'''
猜数字游戏：程序随机生成一个[1,1000]以内的整数，用户输入猜测的数字，猜对则游戏成功结束。
猜测不正确时提示用户猜小了或猜大了 输入0表示退出游戏
'''
import random
rand_num = int(random.random()*1000)+1
# print(rand_num)
while True:
	num = int(input('请输入您猜的数字(1~1000),0表示退出\n'))
	if num == 0:
		print('下次再挑战吧')
		break
	elif num < rand_num:
		print('猜小了')
	elif num > rand_num:
		print('猜大了')
	else:
		print('恭喜你，猜对了')
		break