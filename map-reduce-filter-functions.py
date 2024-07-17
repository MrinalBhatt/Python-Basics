import functools
list1 = [1,2,3,4,5]

# map applies to all the items return an iterator.
multiplyres = map(lambda x : x*2 , list1)
print(list(multiplyres))

#reduce the iterator to single value
sumup_nums = functools.reduce(lambda x,y : x+y, list1)
print(sumup_nums)

#filter the even number from the list
evennums = filter(lambda x: x%2 == 0 , list1)
print(list(evennums))