
"""
array = [5,7,2,23,45,13,20,86,76,44,32]

l = len(array)
moved = False
for i in range(l-1): 
    for j in range(l-1-i): 
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            moved = True
    if not moved:
        break



print("Sorted", array)

"""
array = [5,7,2,23,45,13,20,86,76,44,32] 
# Tip: when you imagine nested loop imagine two same loop as it become easier to visualize 

l = len(array)

for i in range(l-1):
    moved = False
    for j in range(l-1-i): 
        if array[j] > array[j+1]:
            array[j] , array[j+1] = array[j+1], array[j]
            moved = True
    if not moved:
        break

print("Sorted", array)


