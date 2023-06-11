# class Restaurant:
#     """创建关于酒店的类"""
#
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 5
#
#     def describe_restaurant(self):
#         print(f"This restaurant is {self.restaurant_name} and {self.cuisine_type}.")
#
#     def open_restaurant(self):
#         print("The restaurant is opening!")
#
#     def describe_number_served(self):
#         print(f"{self.number_served} persons have been served")
#
#     def set_number_served(self,number):
#         self.number_served = number
#
#     def increment_number_served(self,increment_number):
#         self.number_served += increment_number
#
# class IceCreamStand(Restaurant):
#     """冰淇淋店，继承类“Restaurant”"""
#     def __init__(self,restaurant_name,cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavors = ['apple','banana','peach','onion','chocolate']
#
#     def show_flavors(self):
#         print("Here are ice cream's flavors:")
#         for flavor in self.flavors:
#             print(f"-{flavor}")
# ice_cream = IceCreamStand('Ice','IceCream')
# ice_cream.show_flavors()
# restaurant1 = Restaurant('Green','restaurant')
# restaurant2 = Restaurant('Blue','livehouse')
# restaurant3 = Restaurant('Red','luxury')
#
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()
#
# restaurant1.set_number_served(8)
# restaurant1.increment_number_served(200)
# restaurant1.describe_number_served()


class User:
    """用户"""
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User:{self.first_name.title()}{self.last_name.title()}")

    def greet_user(self):
        print("Hello guy!")

class Privileges:
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_previleges(self):
        print("Here are admin's privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privilege = Privileges()



admin = Admin('Wang','Ming')
admin.privilege.show_previleges()

# user1 = User('Li','Jin')
# user2 = User('Su','Sa')
#
# user1.describe_user()
# user1.greet_user()
#
# user2.describe_user()
# user2.greet_user()