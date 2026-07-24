import copy



# normal copy  (problem: a and b point to same object when we change either b or a it change  the same object)

a=[1,2]
b=a
b.append(4)
print("Normal Copy".center(50))
print("normal_copy_test1_append_4_in_b","a",a,"b",b)


#shallow copy
c=[1,2]
d=c[:]
e=copy.copy(c)
c.append(5)
print("Shallow Copy".center(50))
print("shallow_copy_test1_append_in_c","c",c,"d",d,"e",e)
d.append(4)
print("shallow_copy_test2_append_in_d","c",c,"d",d,"e",e)
e.append(6)
print("shallow_copy_test3_append_in_e","c",c,"d",d,"e",e)



# problem in shallow copy
"""If an iterable contains nested mutable objects (such as lists or dictionaries), a shallow copy copies only the references to those nested objects, not the objects themselves.

As a result, all copies point to the same nested object. Therefore, if you modify a nested object in one copy, the change is visible in all other shallow copies because they share the same underlying object."""

c=[1,2,3,[2,3,4]]
d=c[:]
e=copy.copy(c)
c[3][0]=99
print("Problem in Shallow Copy".center(50))
print("shallow_copy_test4_update_in_position_c_0","c",c,"d",d,"e",e)
d[3][1]=100
print("shallow_copy_test5_update_in_position_d_1","c",c,"d",d,"e",e)
e[3][2]=102
print("shallow_copy_test6_update_in_position_e_2","c",c,"d",d,"e",e)




# deepcopy
c=[1,2,3,[2,3,4]]
e=copy.deepcopy(c)
c.append(5)
print("Deepcopy Copy".center(50))

print("deepcopy_test1_append_in_c","c",c,"e",e)
e.append(6)
print("deepcopy_test2_append_in_e","c",c,"e",e)




# check shallow copy problem (the shallow problem solved by deepcopy)
c[3][0]=999
print("Check shallow copy problem".center(50))
print("deepcopy_test3_update_in_postion_c_0","c",c,"e",e)

e[3][1]=10222
print("deepcopy_test3_update_in_postion_e_2","c",c,"e",e)
