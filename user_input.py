# name = input('Enter your name:')
# age = input("Enter your age: ")
# location = input( "Enter your location: ")

# my_list = []
# my_list.append(10)
# my_list.append(20)
# my_list.append(30)
# my_list.append(40)
# my_list.insert(2,15)

# list2 = [50,60,70]

# my_list.extend(list2)

# my_list.pop()
# my_list.sort()

# index = my_list.index(30)
# print (f"the index of {30} is: {index}") 

# print(my_list)

# my_list.extend(list2)

# my_list.pop()
# my_list.sort()

# index = my_list.index(30)
# print (f"the index of {30} is: {index}") 
# print(my_list)

def calculate_discount(price , discount_percentage):
    if  discount_percentage >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
            return price

 #prompt the user for input

price = float(input("Enter the original price of the item: "))  
discount_percent = float(input("Enter the discount percentage: ")) 

# call the calculate_discount function

final_price = calculate_discount(price , discount_percent)

#print the final price

print(f"The final price after applying the discount is : {final_price: ,2f }")