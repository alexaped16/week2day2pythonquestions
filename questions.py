
#Exercise 1
#Create a list of numbers that are less than ten using l_1 and list comprehension


list = [1,11,14,5,8,9]

# list comprehension
num_list = [y for y in list if y < 11]
print(num_list)


#Should return: 
# [1, 5, 8, 9] 





#Exercise 2
#Using list comprehension, create a list of names of 4 letters or more and capitalize each name

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

names2 = [name.title() for name in names1 if len(name) >= 4]
print(names2)



# Bonus Challenge
names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
['Connor', 'Connor', 'Connor', 'Evan', 'Evan', 'Kevin']

names2 = [name.title() for name in names1 if len(name) >= 4 and names1 is str]



 