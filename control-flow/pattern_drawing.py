num = int(input("Enter the size of the pattern: "))
i = 0
while i <= num:
    for i in range(1,num + 1):
        print(f"{'*' * num}")
        i+=1

