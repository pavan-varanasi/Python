import sys

assert len(sys.argv) == 3, "Need exactly 2 arguments"

first_arg, second_arg =  int(sys.argv[1]), int(sys.argv[2])

if first_arg > second_arg:
	print("First argument - " + str(first_arg) + " is greater than Second argument - " + str(second_arg))
else:
	print("Second argument - " + str(second_arg) + " is greater than First argument - " + str(first_arg))
