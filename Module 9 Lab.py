#Alberto Alcaide-Morales
#3/17/2023

#Problem 1: Creating an infinite loop, This will keep on going because x == 1 and will never be less than 0
print("\n\nProblem 1: ")

x = 1 
while x > 0:
    print('Inifinte')
else:
    print('NOT Infinite')

# Problem 2: Counter begins at 0 and list iterations until list appends all numbers until it reaches 10.
print("\n\nProblem 2: ")

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0
while counter <= 10:
    L.append(counter)
    counter = counter + 1

print(L)

#Problem 3: User inputs random number, numbers are save into a list and iterations stops when sum of numbers in list is greater than 100
print("\n\nProblem 3: ")

L = []
Sum = 0
while Sum < 100:
    x = int(input("Enter Number: "))
    L.append(x)
    Sum = sum(L)
print("List of numbers that sum up to be greater or equal to 100: ", L)
print("Total sum of list: ", Sum)

#Problem 4:  While loop iterates until it Counter < 50, all numbers divisle by 10 are save in a list and print statement prints out solution.
print("\n\nProblem 4: ")

Counter = 0
tens_lst = []

while Counter < 50:
    Counter = Counter + 1
    if Counter % 10 == 0:
        tens_lst.append(Counter)
print("List contains all numbers divisible by 10: ", tens_lst)
  



