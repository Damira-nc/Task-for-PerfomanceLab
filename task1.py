import sys
if (len(sys.argv) == 1):
    print("Параметры не были переданы.")
elif (len(sys.argv) == 3):
    i = 1
    while True:
        print(i, end = '')
        i = 1 + (i + int(sys.argv[2]) - 2) % int(sys.argv[1])
        if i == 1:
            break
else: 
    print("Введено неправильное количество параметров.")