import json
print("Select any food item to pick up where it is stored apple, banana, berry, milk, kiwi, coffee,jam")
user_value_1 = input("Provide a vaule from the above list of food items, it will print the correct key associated: ").lower()
  
def general_dict(find_value_1):
    ''' This Funcation will return the key aginst the value given from the preset dictionary '''
    dictionary = {"item1": "apple", "item2": "banana", "item3": "berry", "item4": "milk", "item5": "kiwi", "item6": "coffee", "item7": "jam"}
    with open('food.json', 'w') as json_file:
        json.dump(dictionary, json_file)
        print("JSON file saved on local to use")
    for key, value in dictionary.items(): 
        if food == find_value_1:
            print("User entered " + find_value_1, "it's stored in " + key)
            break
    else:
        print("Something went wrong")

# Function called for testing
general_dict(user_value_1)

user_value = input("Provide a vaule from the above list of food items, it will print the correct key associated: ").lower()

#Below load_json will get the item from food.json file and display the key against the value entered
def load_json(find_value):
    ''' This Funcation will return the key aginst the value given from the json file it's loaded '''
    with open('food.json') as file:
        data_store = json.load(file)
    for key, value in data_store.items():
        if value == find_value:
            print("User entered " + find_value, " it's stored in " + key)
            break
    else:
        print("You entered something wrong") 

load_json(user_value)
