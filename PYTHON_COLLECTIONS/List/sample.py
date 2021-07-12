my_list=[1,25,4,554,664,11,778,54]
new_list = []
while my_list:
    min = my_list[0]
    for i in my_list:
        if i < min: #111<111
            min = i
    new_list.append(min)
    my_list.remove(min)

print(new_list)
print(my_list)
