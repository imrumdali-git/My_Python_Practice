'''
print (range(5))

for i in range(5):  #vertical print
    print (i)

for i in range(15):
    print (i,end=" ")  #horizantal print
    
for i in range(3,10):
    print (i)  
for i in range(1,10,2):
    print (i)
for i in range(1,10,3):  #range(20,5,-1)
    print (i)

#range(starting,ending,increment/decrement)


for i in range(20,1,-3):
    print (i)    #gapping 3 digit
    



fruits_list = ['apple','banana','cherry',4]
fruits_tuple = ('apple','banana','cherry',3)

for x in fruits_tuple:
    print(x)


#Nested loop                      loop froms loop
adj=["red","big","tasty"]
fruits_list = ['apple','banana','cherry']
for x in adj:
    for y in fruits_list:
        print(x,y)
'''
num = int(input('Enter your number'))
for i in range(2,num):
    print (i)