#integer and string types are immutable so define nested list into the list creates a new object which creates the reference 
import copy
l1 = [1,2,[3,4]]
myset = {1,5,3,1,2}
myset.remove(2)
myset.add(9)
print(myset)
# myset.update(3) = 7 not allowed because you can not update single element in set
copyl1 = copy.copy(l1)
copyl1[2][0] = 10
print(copyl1)
print(l1) 

deepcopyl1 = copy.deepcopy(l1)
deepcopyl1[2][0] = 20
print(l1)
print(deepcopyl1)

for k,v in enumerate(myset):
    print(k, "key")
    print(v, "value")