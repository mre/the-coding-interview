n=int(input("number: "))
if n==1:
	print n
if n<0:
	print("sorry..factorial does not exist")
elif n==0:
	print ("the factorial of 0 is 1")
else:
	for i in range(1,n):
		n=n*i
	print n	
