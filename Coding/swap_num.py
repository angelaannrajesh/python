def Swap(list,pos1,pos2):
    e1 = list.pop(pos1)
    e2 = list.pop(pos2-1)
    list.insert(pos1,e2)
    list.insert(pos2,e1)
    return list

v1 = [1,2,3,4,5]
pos1,pos2 = 3,5
print(Swap(v1,pos1-1,pos2-1))

    
    