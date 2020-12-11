def two(input):

	if input > 1:
		for i in range(2, input):
			if (input % i) == 0:
				print("False")
				return False
			else:
				print("True")
				return True
	else:
		print(0)
		return False

two(10)

