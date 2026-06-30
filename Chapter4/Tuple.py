# what is tuple?
# tuple is similar to list but immutable
# # it also similar ti the string it can not be changed 
# Why use Tuple?
# Use tuple when data should not change.
# t=(1,2,3)
# t[1]=200
# print(t)
# the aboue program output is typerror: 'tuple' object does not support item assignment 
# ----------tuple methods------
# Very few methods because tuple is immutable.
# 1)count():it will conut the number of item not index
tu=(1,2,3,3,3,3,"mallikarjun alyal","bitm ",56)
temp=tu.count(3)
print(temp)
# 2)index():it will find the index value of item
temp2=tu.index(56)
print(temp2)