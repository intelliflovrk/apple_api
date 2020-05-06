fruit = ["apple", "banana", "mango"]
vegetable = ['carrot', 'beans', 'potato']
drink = ['milk', 'water', 'juice']


# T1
def what_is_the_item(item):
    """This method accept 1 params (only items from given lists) and prints item's type."""
    if item in fruit:
        print(item + " is a fruit.")
    elif item in drink:
        print(item + "is a drink.")
    elif item in vegetable:
        print(item + "is a vegetable.")
    else:
        print("Item not found. Only enter the items form given lists.")
    return


# T2
def merge_lists(*args):
    """ This method accepts unlimited params (but only lists) and returns
    new_list with all combined items from accepted lists without duplication."""
    new_list = []
    for arg in args:
        if type(arg) == list:
            new_list += arg
        else:
            print("Warning: One or more parameter is not a python list.")
    print("new_list =", list(set(new_list)))
