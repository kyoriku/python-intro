'''
=      Assigns something from the right to the left
+=     Adds and assigns
-=     Subtracts and assigns
*=     Multiplies and assigns
/=     Divides and assigns
%=     Modulus and assigns
**=    Exponentiates and assigns
'''

number_1 = 14 # Assign 14 to number_1
number_1 = number_1 + 27 # Add 27 to number_1 and assign the result back to number_1
print(number_1)  # Output: 41

number_1 = 14 # Assign 14 to number_1
number_1 += 27 # Add 27 to number_1 using the += operator and assign the result back to number_1
print(number_1)  # Output: 41

number_1 = 14 # Assign 14 to number_1
number_2 = 27 # Assign 27 to number_2
number_1 += number_2 # Add number_2 to number_1 using the += operator and assign the result back to number_1
print(number_1)  # Output: 41
