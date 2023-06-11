def display_message():
    print("Hanshu")

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# favorite_book('Alice in Wonderland')
#8-3
def make_shirt(size,message = 'Hello world!'):
    print(f'This shirt is {size} and a juzi "{message}"')
# make_shirt('xs','Thank you!')

#8-5
def describe_city(city_name,country):
    print(f"{city_name.title()} is in {country}")

# describe_city('Beijing','China')
# describe_city('New york','US')
# describe_city('london','UK')

#8-6
def city_country(city,country):
    city_country = f"{city}, {country}"
    return city_country
# a = city_country('Beijing','China')
# b = city_country('Nanjing','China')
# c = city_country('London','UK')
# print(a)
# print(b)
# print(c)

#8-7
def make_album(singer_name,album_name,sing_number = None):
    dic = {'singer_name':singer_name,'album_name':album_name}
    if sing_number:
        dic['sing_number'] = sing_number
    return dic
# a = make_album('Jay','fantasy')
# print(a)
# b = make_album('Jay','fantasy',10)
# print(b)

#8-8
def show_message(list):
    for message in list:
        print(message)

def send_message(list,sent_messages):
    while list:
        message = list.pop()
        sent_messages.append(message)
# sent_messages = []
# messages = ['a','b','c','d']
# show_message(messages)
# send_message(messages,sent_messages)
# print(sent_messages)

def ingredient(*toppings):
    print("Here are some toppings customer required for pizza:")
    for topping in toppings:
        print(f"-{topping}")

# ingredient('apple','banana','peach','onion')
