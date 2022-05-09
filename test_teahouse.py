""" Test the teahouse class."""

import teahouse as t
#, sys

def main():
    
#    print(f'Are you a customer? y or n')
#    user_input1 = input()
    
#    if user
#    print(f'Are you a customer? y or n')
#user_input = input()


# make a couple tea objects list and print them
#self, type, temp = "hot", size = "medium", add_in = None
    tea1 = t.Tea("Oolong")
    tea2 = t.Tea("Jasmine Green", temp = "cold", add_in = "boba") 
    tea3 = t.Tea("Green", size = "large")
    
    tea_list = (tea1, tea2, tea3)
    
    print(tea_list)
    
    