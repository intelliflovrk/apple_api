print("########################################")
print("Select a fruit 'apple','banana','mango' or ")
print("Select a drink 'milk', 'water', 'juice' or ")
print("Select a veg 'carrot','beans','potato' ")
print("########################################")
user_need = input("What do you like from the above list: ")

fruits = ["apple", "banana", "mango"]
vegs = ['carrot', 'beans', 'potato']
drinks = ['milk', 'water', 'juice']

def what_is_the_item(item):
    if item in fruits:
        print(item + " It's a fruit")
    elif item in drinks:
        print(item + " It's a drink")
    elif item in vegs:
        print(item + " It's a veg")
    else:
        print("Choose the wrong option from the list")

what_is_the_item(user_need)


def merge_list(*no_of_list):
#    full_list = list1 + list2 + list3
    full_list1 = no_of_list[0] + no_of_list[1] + no_of_list[2]
    print("This is the full list: ", full_list1)

merge_list(fruits, vegs, drinks)


