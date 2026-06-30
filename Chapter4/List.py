# list stores multiple values in one variable 
# list is muteable can be change any time
# Store many values
# Access values
# Update values
# Add new values
# Remove values
# Loop through values
# ------------------List Properties-------
# 1)Ordered
# 2)Mutable
# 3) Duplicate values allowed
# 4)Mixed data types allowed
fruits=["mallikarjun alyal","rayappa alyal","ningraj alyal","vijayalaxmi"]
print(fruits[0])
la=fruits[0]="sudeep alyal"
print(la)
# print(fruits[0:3]) this is called sliceing
# --------------------list methods------------
# append:Adds item at end.
fruits.append("pradeep alyal")
print(fruits)
# sort:it sort array element in ascending order
li=[1,29,30,87,54,53,45,2]
li.sort()
print(li)
# reversed:it reverse the array elements
li.reverse()
print(li)
# insert: insert new element using the index  
fruits.insert(4,"sakamma alyal")
print(fruits)
# remove:remove any value inside the array
fruits.remove("rayappa alyal")
print(fruits)
# pop:removes the last item 
#this also pop using index value 
fruits.pop(2)
print(fruits)