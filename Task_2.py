def center_pyramid(n):
    for i in range(0, n):
        for j in range(0, n - i - 1):
            print(end=" ")
        for j in range(1, i*2+2):
            print(j,end="")   
        print()


def right_pyramid(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print(end="")
        for j in range(1, i+2):
            print(j,end=" ")
        print()


def left_pyramid(n):
     for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print("\r")



def number_pattern(n):
    for i in range(0, n):
        for j in range(1, i+2):
            print(j, end=" ")
        print("\r")
    for i in range(n,0,-1):
        for j in range(1,i+2):
            print(j, end=" ")
        print("\r")



print("Which pyramid you want to print: \n 1. For right side.\n 2. For center.\n 3. For left side.\n 4. For  ")
user_choise = int(input("Enter your choise: "))
n = int(input("Enter the size of pyramid: "))

if user_choise == 1:
    right_pyramid(n)
elif user_choise == 2:
    center_pyramid(n)
elif user_choise == 3:
    left_pyramid(n)
elif user_choise == 4:
    number_pattern(n)
else:
    print("Invalid choise..")

