# =============TASK 01=======
# operator = int(input('''1. Addision (+), 
# 2. Subtraction (-),
# 3. Multiplication (*),
# 4. Division (/),
# 5. Modulus (%) 
# Enter the operator (1-5) : '''))

# if (operator in range(1,6)):
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))
#     if operator == 1:
#         print("Result : ", num1 + num2)
#     elif operator == 2:
#         print("Result : ", num1 - num2)
#     elif operator == 3:
#         print("Result : ", num1 * num2)
#     elif operator == 3:
#         print("Result : ", num1 / num2)
#     elif operator == 5:
#         print("Result : ", num1 % num2)
#     else: 
#         print('Invalid Inputs')
# else: 
#     print('Invalid Operator')

# =========TASK 02======
# set1 = {2,4,6,7,8,9,0}
# set2 = {1,3,5,6,7,8,9}

# unionSet = set1.union(set2)
# intersectoinSet = set1.intersection(set2)
# difference1 = set1.difference(set2)
# difference2 = set2.difference(set1)

# print ('Set 1 : ', set1)
# print ('Set 2 : ', set2)
# print ('Union : ', unionSet)
# print ('Intersection : ', intersectoinSet)
# print ('Difference : ', difference1)
# print ('Difference : ', difference2)

# ========TASK 03========

import calendar
print ('Calender of March of 2024')
print(calendar.month(2024, 3))