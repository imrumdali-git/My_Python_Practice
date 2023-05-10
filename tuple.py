#Unpacking tuple:
my_tuple = ('apple','banana','cat')
(a,b,c) = my_tuple
print(a)

#Multiple values for one variable 
my_tuple = ('Apple','banana','cat','dog','egg','fish','gun')
(a,b,*c) = my_tuple
print(c)
(a,*b,c) = my_tuple
print(a)
print(b)     #Gets multiple values
print(c)


