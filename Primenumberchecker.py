
num = int(input("ONLY ENTER A NUMBER NO LETTERS: \n"))

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break


if flag:
    print(num, "NOT PRIME")
else:
    print(num, "PRIME}")