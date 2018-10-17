n=input()
flag=0
for f in n:
	if((f=='0') or (f=='1')):
		flag+=1
if(flag==len(n)):
	print("yes")
else:
	print("no")
