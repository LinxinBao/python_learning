#4-1
pizzas = ['apple','banana','peach']
for pizza in pizzas:
    print(f"I like {pizza} pizza!")
print("I really like pizza!")
#4-3
numbers = []
numbers = [value for value in range(1,21)]
print(numbers)
numbers = list(range(1,11))
print(numbers)
print(min(numbers))
print(max(numbers))
numbers = list(range(1,21,2))
for number in numbers:
    print(number)
numbers = [value**3 for value in range(1,11)]
for number in numbers:
    print(number)