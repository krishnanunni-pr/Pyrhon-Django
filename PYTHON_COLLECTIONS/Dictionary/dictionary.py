# dict={"Name": "Zara" ,"Age":7,"Class":"First" } #here "name" is key and "zara" is value
# print(dict)
# print(type(dict))
# print("dict[Name]:",dict["Name"] )
# print("dict[Age]:",dict["Age"])

# key must be unique
# dictionary is mutable(changable)
# keeps order
# key must not be dictionary
# values can be dictionary


# Empty Dictionary
# dictio={}
# print(dictio)
# print(type(dictio))


# UPDATE DICTIONARY

# dict={"Name": "Zara" ,"Age":7,"Class":"First" }
# dict["Age"]=8 # update the existing value
# print(dict)
# dict.update({"Location":"Kochi"}) # adding new key and value
# print(dict)



# REMOVING ELEMENT IN DICTIONARY

dict={"Name": "Zara" ,"Age":7,"Class":"First" }
del dict["Name"] # Remove entry with key "name"
print(dict)
dict.clear() # clear all aentries in th dictionary
print(dict)
del dict # DELETE DICTIONARY
print(dict)

# Key canot be nested values can

dict={1:2,2:{3:4}}
print(dict)
