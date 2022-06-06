#numbers = int(input("Enter the numbers: "))
#print(numbers)

odd = []
even = []
for i in range(10):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f'The even numbers are: {even}')
print(f'The odd numbers are: {odd}')
