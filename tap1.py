def find_x(list1): 
    for i in range(len(list1)):
        if list1[i] == 6:
            return i
        else:
            return("Ondai zhoq")
print(find_x([1,6,3,22,8]))

