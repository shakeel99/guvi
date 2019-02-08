a11,b11=raw_input().split()
a11=int(a11)
b11=int(b11)
for num1 in range(a11,b11+1):
	if num1 >1:
		for j in range(2,num1):
			if(num1 %j)==0:
				break
		else:
		  print num1,
