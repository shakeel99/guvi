def main():
	num=int(input())
	sum10=0
	temp=num
	while temp>0:
		digit = temp%10
		sum10 +=digit**3
		temp //=10
	if num ==sum10:
		print("yes")
	else:
		print("no")
if __name__ == '__main__':
		main()
