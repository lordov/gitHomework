# Home work 3.1.

hat_list = [1, 2, 3, 4, 5]

print(len(hat_list))

number = int(input("Enter number: ")) # Enter number for line.
hat_list[2] = number # Reokace middle number with an integer
print(hat_list)

hat_list.pop() # Remove the last element
print(hat_list)

print(len(hat_list))

# Home work 3.2.

beatles = []

# Create an empty list.
print("Step 1:", beatles)

# Add the members of the band to the list.
beatles.append("John Lennon, Paul McCartney, George Harrison")
print("Step 2:", beatles)

# Add the last members of the band to the list.
for i in range(2):
   beatles.append(input("Add following members of the band "))
print("Step 3:",beatles)

# Us pop() or remove() metods to remove Stu and Pete.
del beatles[-1]
beatles.pop()
print("Step 4:", beatles)

# Use insert() metod to add Ringo Starr.
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# Home work 3.3.
li = []
swapped = True
print(li)

numbers = int(input("Enter the quantity "))

for i in range(numbers):
    print(f"Enter number {i + 1} in list")
    number_from_user = int(input('--> '))
    li.append(number_from_user)

while swapped:
    swapped = False
    for i in range(len(li) - 1):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
            swapped = True
print(li)

li.reverse()
print("Reverse", li)

# Home work 3.4.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
res_list = list(set(my_list))
print(res_list)

# Home work 3.5.

li = input("Enter the numbers ").split()
Li = [int(val) for val in li]
S = sum(Li)
print(S)
