prompt = "If you tell us who you are,we can personalize the message you see."
prompt += "\nWhat is your first name?"
print(prompt)
#7-1
car = input("Which kind of cars do you want to rent?")
print(f"Let me see if I can find you a {car}.")
#7-2
number = input("How many persons want to eat together?")
number = int(number)
if number > 8:
    print("No rest desk!")
else:
    print("We have empty desk!")
#7-3
number = input("Please input a number:")
number = int(number)
if number%10 == 0:
    print(f"number {number} can be devided by 10!")
else:
    print(f"The number {number} can not be devided by 10!")
#7-4
prompt = "\nPlease enter the name of a ingredient which can be prepared for pizza:"
prompt += "\n(Enter 'quit' when you are finished.)"
ingredient = ''
while True:
    ingredient = input(prompt)
    if ingredient != 'quit':
        print(f"Okay!We will add {ingredient} into this pizza!")
    else:
        break
#7-5
while True:
    old = input("How old are you?")
    old = int(old)
    if old <= 3:
        print("Free toll")
    elif old <= 12:
        print("A ticket need 10 dollars,thank you!")
    else:
        print("A ticket need 15 dollars,thank you!")
#7-7
while True:
    print(1)
#7-8
sandwich_orders = ['apple','banana','Pastrami','peach','Pastrami','melon','Pastrami']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
for f_sandwich in finished_sandwiches:
    print(f_sandwich)
#7-9
sandwich_orders = ['apple','banana','Pastrami','peach','Pastrami','melon','Pastrami']
print("Pastrami have been sold out!")
active = True
while active:
    if 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')
    else:
        active = False
print(sandwich_orders)

#7-10
responses = {}
polling_active = True
while polling_active:
    name = input("What is your name?")
    response = input("If you could visit one place in the world,where would you go?")
    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes or no)")
    if repeat == 'no':
        polling_active = False

print("\n---Poll Results---")
for name,response in responses.items():
    print(f"{name} would like to visit {response}!")