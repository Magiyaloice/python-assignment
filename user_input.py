# name = input('Enter your name:')
# age = input("Enter your age: ")
# location = input( "Enter your location: ")

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(2,15)

list2 = [50,60,70]

my_list.extend(list2)

my_list.pop()
my_list.sort()

index = my_list.index(30)
print (f"the index of {30} is: {index}") 

print(my_list)