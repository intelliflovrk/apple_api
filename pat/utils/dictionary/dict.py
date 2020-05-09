import json
print("Select any food item to pick up where it is stored apple, banana, berry, milk, kiwi, coffee,jam")
search_food_1 = input("Provide a vaule from the above list of food items, it will print the correct key associated: ")

#This funcation is has a preset dictionary, asking user to enter the value from the list and will print the key  
def general_dict(food_name):
    dictionary = {"item1": "apple", "item2": "banana", "item3": "berry", "item4": "milk", "item5": "kiwi", "item6": "coffee", "item7": "jam"}
    with open('food.json', 'w') as json_file:
        json.dump(dictionary, json_file)
        print("JSON file saved on local to use")
    for item, food in dictionary.items(): 
        if food == food_name:
            print(item)

# Function called for testing
general_dict(search_food_1)

search_food_2 = input("Provide a vaule from the above list of food items, it will print the correct key associated: ")

# #Below load_json will get the item from food.json file and display the key against the value entered
def load_json(some_value):
    with open('food.json') as file:
        data_store = json.load(file)
        print(data_store)
        for item, food in data_store.items(): 
            if food == some_value:
                print(item)        

load_json(search_food_2)