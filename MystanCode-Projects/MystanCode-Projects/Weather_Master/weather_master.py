"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -1


def main():
	"""
	1.Print("StanCode Weather Master 4.0")
	2.Check whether n is EXIT or not.
	3.IF Yes, print("No temperatures were entered."). If not, declare variable
		(1) highest and lowest: record the highest and lowest temperature
		(2) total: sum all temperature
		(3) t: record the number of temperature
		(4) coldday: record the days of temperature < 16
	4.Input the new "n".
	5.If new "n" is higher than previous "n", redefine "highest" as new "n".
	6.If new "n" is lower than previous "n", redefine "lowest" as new "n".
	7.If new "n" is lower than 16, redefine "coldday" as coldday + 1.
	8.Redefine "total" and "t".
	9.Repeat step 4~8 until n = EXIT, and print "highest", "lowest", "average (total/t)" and coldday.
	"""
	print("StanCode \"Weather Master 4.0\"")
	n = int(input("Next Temperature: (or "+str(EXIT)+" to quit)? "))
	if n == EXIT:
		print("No temperatures were entered.")
	else:
		highest = n
		lowest = n
		total = n
		t = 1
		coldday = 0
		while True:
			if n < 16:
				coldday += 1
			n = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
			if n == EXIT:
				print("Highest Temperature = "+str(highest))
				print("Lowest Temperature = "+str(lowest))
				print("Average Temperature = "+str(total/t))
				print(str(coldday)+" cold day(s)")
				break
			elif n > highest:
				highest = n
			elif n < lowest:
				lowest = n
			total += n
			t += 1


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
