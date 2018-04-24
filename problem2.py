num = input("input number:")
num = int(num)
ans = 0
for i in range(1, num+1):
	if(i % 15 == 0):
		ans += 1
	elif(i % 3 == 0 or i % 5 == 0):
		continue
	else:
		ans += 1

print(ans)