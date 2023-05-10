try: 
    #code you have
    a=int(input('Enter the first num: '))
    b=int(input('Enter the second num: '))
    print(a/b)

    mylist =[1,2,3,4]
    print(mylist[5])

except ZeroDivisionError:
    #exception produced by the code                     #Once exception gives the value it doesn't return another value.
    print('A number cannot be divided by zero!')

except IndexError:
    #index exception produced by the code
    print('List is not long enough!')

finally:
    print('Program Ends')

#function
def sum_of_two(a,b):     #real function which is long process but by lambda function we can run code in one line called lambda function
    return a+b

sum_of_two = lambda a,b:a+b
#name_of_function = lamda parameters:operation 

print(sum_of_two(3,4))   #sum = sum_of_two(3,4)
                         #print(sum)          #this is optional
                         