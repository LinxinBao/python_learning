dic = {'first_name':'Bao','last_name':'Linxin','age':23,'city':'Jinhua'}
print(dic['first_name'])
rivers = {'nile':'Egypt','changjiang':'China','yalv':'Kereo'}
for river,country in rivers.items():
    print(f"The {river} runs through {country}.")

for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)
