import sys
with open(sys.argv[1]) as file_1:
    arr = file_1.read().split() 
arr = [float(num) for num in arr]
summa = 0
sorted(arr)
k = round(sum(arr)/len(arr));
for i in range(len(arr)):
    summa += abs(arr[i] - k)
print(summa);