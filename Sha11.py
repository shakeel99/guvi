while True:
	try:
		A1,B1= raw_input().split()
		A1=int(A1)
		B1=int(B1)
		break
	except:
		print("Invalidinput")
		break
D1=1
for y in range(B1):
	D1=D1*A1
print(D1)
