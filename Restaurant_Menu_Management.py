def adding(add_item):
    initial_menu.append(add_item)
def removing(remove_item):
    initial_menu.remove(remove_item)

def checking_menu(check_item):
    if check_item in initial_menu:
        print(f'Availability: "{check_item} is available"')
    else:
        print("Not Available")

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"
adding(add_item)
removing(remove_item)
print("Updated menu:",initial_menu)
checking_menu(check_item)
