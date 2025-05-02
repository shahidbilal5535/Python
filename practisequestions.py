# f = open("myfile.txt", "r")
# i = 0
# while True:
#     i = i +1
#     line = f.readline()
#     print(line)
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student {i} in Maths is : {m1*2}")
#     print(f"Marks of student {i} in Eng is :   {m2*2}")
#     print(f"Marks of student {i} in SST is :   {m3*2}")

#     print(line)


                           # writeline() method

# f = open("myfile.txt","a")

# f.writelines(["See you soon!\n","Over and out\n"])
# f.close()

# f = open("myfile.txt","r")
# print(f.read()) 


                    ###seek () function

# with open('myfile.txt', 'r') as f:
#     print(type(f))
#     # Move to 10th byte in the file
#     f.seek(10)

#     # Read the next 5 bytes
#     print(f.tell())
#     data = f.read(5)
#     print(data)



              ## tell() function  it tells us on which position we have seek
# with open('myfile.txt', 'r') as f:
#     # read the first 10 bytes
#     data = f.read(10)

# # save the current position 
# current_position = f.tell()

# # seek to the saved position
# f.seek(current_position)



                             ## truncatae() function

# with open('myfile.txt', 'w') as f:
#     f.write('Hello World!')
#     f.truncate(5)

#     with open("myfile.txt", "r") as f:
#         print(f.read()) 



                             ## LAMBDA FUNCION
#EX

# # Function to double the input 
# def function(x):
#     return x * 2

# # Lambda function to double the input
# lambda x : x * 2

#  EX
# double = lambda x: x * 3
# cube = lambda x: x*x*x
# modules = lambda x: x % 4



# print(double(4))
# print(cube(6))
# print(modules(10))


# def appl(fx, value):
#     return 6 + fx(value)
# double  = lambda x :x * 2
# cube = lambda x : x * x * x
# avg =  lambda x, y, z:(x + y + z) / 3

# print(double(5))
# print(cube(5))
# print(avg(3, 5, 10))
# print(appl(lambda x: x * x *x , 2))


my_string="Hello" 
split_text = my_string.split(",")
print(split_text)