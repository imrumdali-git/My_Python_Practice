'''#Set (Index doesn't exist)
my_set = {'a','b','c','d','a'}  #doesn't repeat 
print (my_set)
print(type(my_set))

#chaning list into set
my_list=['a','b',1,2,'a','b',4,5,'c',4,'c']
my_set=set(my_list)
a=list(my_set)
print(a)

#Add and Update
my_set={'x','y','z'}
my_set.add("Anil")
print(my_set)
my_set.update({1,2,3})
print(my_set)
my_set.remove('Anil')      #removes variable from set
print(my_set)
my_set.remove('a')
print(my_set)
my_set.discard(1)           #remove variable from set but will not ans if their is no variable
print(my_set)
my_set.pop()        #remove last element
print(my_set)
my_set.clear()      #empties the set
print(my_set)
del my_set          #delete set

my_list1=[1,2,3,4,5]
my_list2=[4,5,6,7,8]
my_set1=set(my_list1)
my_set2=set(my_list2)
a=my_set1.intersection(my_set2) #for Intersection
b=list(a)
print(b) '''

list=[1,2,3,4]
a = int(input("enter index"))

print(list[a])





