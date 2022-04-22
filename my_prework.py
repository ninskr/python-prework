# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 

def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")

hello_name("jesse")

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for num in range(101):
        if int(num) % 2 != 0:
            print(int(num), end= " ")

first_odds()

# Question 3:
# Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    max_num = sorted(a_list)[-1]
    return max_num

# Question 4:
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(a_year):

    if int(a_year) % 4 == 0 and int(a_year) % 100 != 0 or int(a_year) % 400 == 0:
        return True
    else:
        return False

# Question 5:
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.
def is_consecutive(a_list):
    i = 0
    while i < len(a_list) - 1:
        if int(a_list[i]) + 1 == int(a_list[i + 1]):
            i +=1
            continue
        else:
            return False
            break
    return True