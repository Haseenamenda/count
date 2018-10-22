s=input()
v=('a','e','i','o','u','A','E','I','O','U')
for i in s:
	if i in v:
		print("yes")
		break
else:
	print("no")
