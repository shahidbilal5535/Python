# def cube (x):
#     return x*x*x

# print(cube(2))

# l = [1,2,4,6,8,5]
# new_l =[]

# for item in l:
#     new_l.append(cube(item))

# new_l = list(map(cube, l))

# print(new_l)

##                        EXAMPLE QUESTIONS

 # 1.  Write a Python program to triple all numbers in a given list of integers. Use Python map
# # Create a tuple named 'nums' containing the numbers 1 through 7
# nums = (1, 2, 3, 4, 5, 6, 7)

# # Print the original list of numbers
# print("Original list: ", nums)

# # Use the map function to apply a lambda function that triples each element in 'nums'
# result = map(lambda x: x + x + x, nums)

# # Print the result of the map operation as a list
# print("\nTriple of said list numbers:")
# print(list(result))





# 2.  Write a  Python program to add three given lists using Python map and lambda.

# # list of three nums: num1 , num2 , num3
# num1 = [9,8,7]
# num2 = [9,8,7]
# num3 = [9,8,7]

# # Print orginal lists
# print("Orginal_list :")
# print(num1)
# print(num2)
# print(num3)

# # Use the map function to apply a lambda function that adds corresponding elements
# # from nums1, nums2, and nums3 and create a new list

# new_lists = map(lambda x, y, z : x + y + z, num1, num2,num3)
# print("\nNew list after adding of above lists :")
# print(list(new_lists))



# 3.   Write a Python program to listify the list of given strings individually using Python map.

# # create a list containing colors name
# colors = ["Red", "Green", "Blue", "White", "Purple"]

# # Print the Orginal list of colors
# print("Orginal_list:")
# print(colors)

# ## Print a message indicating the operation to be performed
# print("\nAfter listfy the list of strings are:")

# # Use the map function to apply the list function to each element of 'color'
# new_list = list(map(list, colors))

# print(new_list)

# def square_num(x):
#     return x * x


#5. Write a Python program to square the elements of a list using the map() function

# # Define a function named square_num that calculates the square of a given number 'n'
# def square_num(n):
#     return n * n
# # Create a list named 'nums' containing integer elements
# nums = [4, 5, 2, 9]

# # Print the original list of numbers
# print("Original List: ", nums)

# # Use the map function to apply the square_num function to each element of 'nums'
# result = map(square_num, nums)

# # Print a message indicating the operation to be performed
# print("Square the elements of the said list using map():")

# # Print the result of the map operation as a list
# print(list(result))
   

#             # we can write this code in LAMBDA function in short way

# nums = [4,5,2,9]
# new_nums = map(lambda x: x * x, nums)
# print(new_nums)



                  # Filter function

#1. Write a Python function that filters out even numbers from a list of integers using the filter function.



# def is_even(x):
#     return x % 2 ==0

# l = [1,2,3,4,5,6,7,8]

# new_line = filter(is_even,l)  ## two arguments a function and a sequence
# print(list(new_line))


#2. Write a  Python program that uses the filter function to extract all uppercase letters from a list of mixed-case string
# mixed_case_strings = ["Hello", "Shahid","Bilal", "University"]

# print("Orginal list of strings :\n" , mixed_case_strings )

# uppercase_strings = list(filter(lambda char : char.isupper(), ''.join(mixed_case_strings)))

# print(list(uppercase_strings))



2.# Write a  Python program that creates a list of names and uses the filter function to extract names
# that start with a vowel (A, E, I, O, U).



# # Define a list of names
# names = ["Elita", "Vitold", "Audovacar", "Kerensa", "Ramana", "Iolanda", "Landyn"]
# print("Original list of names:")
# print(names)
# # Define a function to check if a name starts with a vowel
# def starts_with_vowel(name):
#     return name[0].lower() in ['a', 'e', 'i', 'o', 'u']

# # Use the filter function to extract names starting with a vowel
# vowel_names = list(filter(starts_with_vowel, names))
# print("\nExtract names starting with a vowel:")
# # Print the extracted names
# print(vowel_names)

# names = ["Elite", "Apple", "Vitold", "Kite","Uppercase","Rabbit", "Island","Orange"]
# print("Orginal list of names: ")
# print(names)

# def start_with_vowel(name):
#     return name[0].lower() in ['a','e','i','o','u']
# vowel_names = list(filter(start_with_vowel,names))

# print("\nNames that start with vowels :")
# print(vowel_names)


       # Reduce functions
#Ex 1
# from functools import reduce
# numbers = [1,2,3,4,5]
# result = reduce(lambda x ,y : x + y, numbers )
# print(result)

# Ex2 
# from functools import reduce
# nums = [11,22,33,44,55]
# new_nums = reduce(lambda x, y: x + y, nums)

# print(new_nums)


## Exercise 5 Snake Water Gun
# import random
# def GameWin(comp, You):
#     if comp == You:
#         return False
#     elif comp == "s":
#         if You == "w":
#             return False
#         elif You == "g":
#             return True
#     elif comp == "w":
#         if You == "s":
#             return True
#         elif You == "g":
#             return False
#     elif comp == "g":
#         if You == "w":
#             return True
#         elif You == "s":
#             return False
# print("comp turn : snake (s) water (w) gun(g)")

# RandNo = random.randint(1,3)

# if RandNo == 1:
#     comp = "s"
# elif RandNo == 2:
#     comp = "w"
# elif RandNo == 3:
#     comp = "g"

# You = input("your turn  choose one : s , w, g ???")

# a = GameWin(comp, You)
# print(f"computer choose {comp}")
# print(f"you choose {You}")


# if a == None:
#     print("<<<   TIE   >>>")
# elif  True:
#     print("<<<   YOU WIN   >>>")

# else :
#     print("<<   YOU LOSE   >>>")


     #     class and Object

# class details:
#     name = "Shahid"
#     occupation = "Student"
#     age = 24
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a = details()
# b = details()

# a.name = "Adil"
# a.occupation = "Empolyee"

# b.name = "Shahid"
# b.occupation = "Student"
# # print(a.name , a.occupation)

# a.info()
# b.info()

                               ### questions on class and object
#Define a  Python function student(). Using function attributes display the names of all arguments.
# def student (student_id, student_name, student_class):
#    return f'student ID: {student_id}\nstudent Name: {student_name}\n student Class: {student_class}'
# print(student('S122','Shahid','VI'))



              ## CONSTRUCTOR __init__  <<<  called initilazations

# class Details:
#   def __init__(self, animal, group):
#     self.animal = animal
#     self.group = group

# obj1 = Details("Crabs", "Crustaceans")
# print(obj1.animal , "belongs to the ",obj1.group, "group.")


class Details:
    def __init__(self, gm , group):
        self.animal = gm      
        self.group = group

obj1 = Details("CRICKET ", "OUTDOOR")
print(obj1.gm, "belongs to the" ,obj1.group ,"groups")