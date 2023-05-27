from datetime import date

name=input("Enter Your Name:")
current_age=int(input("Enter Your Age:"))
today=date.today()
age_diff=100-current_age
hunyear=today.year+age_diff
print("haii {0}...you will turn 100 years at {1}".format(name,hunyear))


