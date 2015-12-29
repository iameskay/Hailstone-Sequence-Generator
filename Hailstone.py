def hailstone(n):
	x = n
	ans = 1
	print n,
	while(n > 1):
		if ans == 10:
			print " "
		if n % 2 == 0:
			n = n/2
			ans = ans + 1
			print n,
		else:
			n = (n*3) + 1
			ans = ans + 1
			print n,
	print " "
	print "There are %s numbers in the sequence starting at %s." %(ans,x)
