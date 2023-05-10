'''#enumerate
for i in enumerate("Hello"):
    print (i)  '''


languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# convert enumerate object to list
print(list(enumerate_prime))

# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

Name=["Anil","Rose","Sabin"]

for i in enumerate(Name):
    print(i)

for count,i in enumerate(Name):
    print(count, i)

for count,i in enumerate(Name,100):
    print(count, i)