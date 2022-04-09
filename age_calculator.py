from datetime import date, timedelta


def get_dob():
    # write code here
	year = input("Enter year of birth: ")
	month = input("Enter month of birth: ")
	day = input("Enter day of birth: ")

	dob = date(int(year),int(month),int(day))

	return dob



def get_age(dob):
    # write code here
	today = date.today()

	if(dob > today):
		print("Dob is invalid")
		return
	else:
		td = today - dob
		days = td.days
		age = int(days/365.25)
		print(f"You are {age} years old.")

		# for test to pass
		return age
		

	
def main():
	# write code here
	dob = get_dob()
	get_age(dob)


if __name__ == '__main__':
    main()


