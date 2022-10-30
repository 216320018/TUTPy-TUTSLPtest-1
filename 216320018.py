s = 'fullstackslp'
print(s[0])
print(s[4:9])
print(s[9:])
print(s[7:10])
print(s[-1:-12])

d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

list_set = set(mylist)
unique_list = (list(list_set))
print(unique_list)

age = 45
name = "Kyle"
print("Hello my dog's name is {} and he looks {} years old".format(name,age))