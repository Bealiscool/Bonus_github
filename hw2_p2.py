

u = int(input("Input the range number:"))

n = 1
while n <= u:
	i = 1
	sum_list = []
	while i <= n:
		if n % i == 0:
			sum_list.append(i)
		i = i + 1
	if sum(sum_list) / 2 == n:
		print(n)
	n = n + 1
