def getWays(n):
	memo = {}
	memo[1] = 1
	memo[2] = 2
	if n in memo:  # if the recurssion already done before first take a look-up in the look-up table
			return memo[n]
	else:  # Store the recurssion function in the look-up table and reuturn the stored look-up table function
			memo[n] = getWays(n - 1) + getWays(n - 2)
			return memo[n]

	return climb(n)


n=3
ways = getWays(n)
print(ways)