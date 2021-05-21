###############################
# Author: Ben Swinford
# Program: leapyear.py
# Date: 5/22/21
###############################


def leapYears():
	year = input("Please enter a year: ")
	year = int(year)
	output = []
	output.append(year)
	fourYears = year%4
	hunYears = year%100
	fohunYears = year%400
	if fourYears == 0 and hunYears != 0 or fohunYears == 0:
		output.append(1)
	else:
		output.append(0)
	return output


#if __name__ == '__main__':
#	main()
