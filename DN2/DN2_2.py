our_list = [1,2,3,4,5,6,7]


our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}



our_tuple = (357, 12, 12, 8, 5, 2, 2)



#print(our_list[4])
#our_list.append(8)
#print(our_list)
#our_list.pop()
#print(our_list)
#our_list.insert(0,0)
#print(our_list)
#our_list.pop(0)
#print(our_list)

#our_dict.add(our_list[4])
#our_list[4] #izberemo index št. 4 na listu


print(our_dict)
our_dict["d"]=our_list[4]  #ključu v dictionary-ju priredimo vrednost iz indexa 4 iz našega lista
print(our_dict)


print(our_list)
our_list.pop(4) #odstranimo vrednost na indexu 4
print(our_list)


list = [(v) for v in our_dict.items()] #naš dictionary spremenimo v tuple
print(list)
print(our_tuple)






