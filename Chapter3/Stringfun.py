#1)length  fucntion:this function will find the length of string 
name="mallikarjunalyal"
print(len(name))
# 2) endstring function means it will find the endstring if it is correct it return the true or False
print(name.endswith("hello")) 
# 3)startstring function it will find the starting string and it will return the true or False
print(name.startswith("king"))
# 4) capitalize function if  first  letter  it is in will convert into captilize
print(name.capitalize()) 
# 5) string.find(word)
# this function friends a word and returns the index of first occurrence of that word in the SyntaxWarning
u=name.find("alyal")
print(u)
m="mallu bhai"
print(m.replace("mallu","mallikarjun"))