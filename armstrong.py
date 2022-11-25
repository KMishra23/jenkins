#!/usr/bin/python

def order(x):
	n = 0
	while (x != 0):
		n = n+1
		x = int(x/10)
	return n

def isArmstrong(x):
	n = order(x)
	temp = int(x)
	
	sum = 0
	while (temp != 0):
		r = temp % 10
		sum = sum + r**n
		temp = int(temp/10)

	return (sum == x)

# print(isArmstrong(153))
# print(isArmstrong(1634))
# print(isArmstrong(370))
# print(isArmstrong(407))
