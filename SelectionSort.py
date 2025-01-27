array = [5,7,2,23,45,13,20,86,76,44,32] #length = 11

l = len(array)
for i in range(l-1):
    min_index = i
    for j in range(i+1, l):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
            

print("Sorted array :", array)