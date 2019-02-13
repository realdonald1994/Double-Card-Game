str1="donald"
str2="king"
str3 ='kingnn'
name=[]
name.append(str1)
name.append(str2)
name.append(str3)
for i in name:
    for j in i:
        if 'k' ==j:
            print(name[name.index(i)][2])

print(min('A','B'))

