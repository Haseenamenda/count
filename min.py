def smallest(arr,c):
	min=arr[0]
	for i in range(1,c):
                  if arr[i]<min:
                      	min=arr[i]
	return min
arr=[5, 4, 3, 2, 1, 7, 6, 10, 8, 9]
c=len(arr)
Ans=smallest(arr,c)
print(Ans)
