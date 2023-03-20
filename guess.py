#import random 是一個module(一個python檔，很多個module是一個package) 

#r = random.randint(1,100)
#print(r)

#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對的話 印出"終於猜對了"
#猜錯的話 要告訴他 比答案大/小

import random
ans=random.randint(1,100)
count=0
while True:
	count+=1 #count=count+1
	num = input('請輸入數字 :')
	num = int(num)
	if num==ans : 
		print('恭喜答對')
		print('總共猜了',count,'次')
		break
	else:
		if num < ans:
			print('比答案小')
		elif num >ans:
			print('比答案大')
	print('總共猜了',count,'次')
