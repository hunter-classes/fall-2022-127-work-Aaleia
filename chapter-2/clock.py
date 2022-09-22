## If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the clock when the alarm goes off.

current_time = input("What is the current time?")
passing_time = input("How many hours will pass?")
current_time_int = int(current_time)
passing_time_int = int(passing_time)

total_hours = current_time_int + passing_time_int

final_time = total_hours % 24

print(final_time)