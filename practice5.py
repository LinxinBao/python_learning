car = 'subaru'
print("Is car =='subaru'?I predict True.")
print(car == 'subaru')

print("\nIs car == 'sudi'? I predict False.")
print(car == 'audi')

cars = ['audi','toyota','subaru','bmw']
if 'audi' in cars:
    print("Yes")
alien_color = 'green'
if alien_color == 'green':
    print("The player win 5 scores")
elif alien_color == 'yellow':
    print("The player win 10 scores")
elif alien_color == 'red':
    print("The player win 15 scores")
names = ['John','mike','amy','Adam','admin']
for name in names:
    if name == 'admin':
        print(f"Hello {name},would you like to see a status report?")
    else:
        print(f"Hello {name.title()},thank you for logging in again")
current_users = ['john','adam','dam','amy','li']
new_users = ['john','amy','guo','lin','xue']
for new_user in new_users:
    if new_user in current_users:
        print(f"You need a new name to change this name:{new_user}!")
    else:
        print("This name can be used to play this game!")
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number==3:
        print("3rd")
    else:
        print(f"{number}th")