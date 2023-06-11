names = ['sua','lijin','kang']
print(names[0],names[1],names[2])
print(names)
message = "nice to meet you!"
print(f"{names[0].title()},{message}")
print(f"{names[1]},{message}")
print(f"{names[2]},{message}")
#3-4
list = ['mom','dad','bao zexuan']
print(f"Dear {list[0].title()},{list[1].title()},{list[2].title()},I want to invite you to have dinner with me!")
#3-5
print(f"{list[2].title()} can not arrive")
list[2] = 'kangkang'
print(f"Dear {list[0].title()},{list[1].title()},{list[2].title()},I want to invite you to have dinner with me!")
#3-6
list.insert(0,'grandma')
list.insert(2,'grandpa')
list.append('nainai')
print(f"Dear {list[0].title()},{list[1].title()},{list[2].title()},{list[3].title()},{list[4].title()},{list[5].title()},I want to invite you to have dinner with me!")
#3-8
plays = ['beijing','tianjing','nanjing','suzhou','xian']
print(plays)
print(sorted(plays))
print(plays)
print(sorted(plays,reverse=True))
print(plays)
plays.reverse()
print(plays)
plays.reverse()
print(plays)