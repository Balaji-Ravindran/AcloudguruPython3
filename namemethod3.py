name = input("enter your name: ")
#print(name)

## unique_name assigned to empty List[]
unique_name = []
for i in name:
    if i not in unique_name:
        unique_name.append(i)
print(f'unique characters are: {unique_name}')