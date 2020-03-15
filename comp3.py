import sys

assert len(sys.argv) == 4, "Need exactly 3 arguments"

x, y, z =  int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

if x > y and x > z :
	print("First argument - " + str(x) + " is greater than Second argument and third - " + str(y) + srt(z))
elif y > x and y > z:
	print("Second argument - " + str(y) + " is greater than First argument and third - " + str(x) + str(z))

elif z > x and z > y:
	print("third argument - " + str(z) + " is greater than second and first " + str(y) + str(x))

