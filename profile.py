# this script is here to demo profiling with PyCharm and ...

def factorial(n):
	
		if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

def doubleSqrt(n):
	return math.sqrt(math.sqrt(n))



def main():
	for x in range(0, 100000):
		fact = factorial(x)
		print(fact)
		root = doubleSqrt(x)
		print(root)


if __name__ == "__main__":
	main()
