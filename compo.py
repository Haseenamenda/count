m=int(input())
f=0
for i in range(2,m//2):
	if m%i==0:
		f=1
		break
if f==1:
	print('yes')
else :
	print('no')
