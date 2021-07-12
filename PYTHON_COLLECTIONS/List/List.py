#    LIST

lst=[1,2,3,1,2,3,"hello","asdads"]
print(lst)
print(type(lst))

#1.supports duplicate elements
#2.keeps order
#3. hetrogeneous
# List is mutable(changing posssible)
# EMPTY LIST

lst1=[]
print(lst1)
print(type(lst1))
lst1.append("hello")
lst1.append("asdhhas")
print(lst1)
lst1.remove("hello")
print(lst1)
lst1.clear()
print(lst1)
del lst
print(lst)