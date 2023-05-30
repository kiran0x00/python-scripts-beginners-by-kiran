# File Handiling example


# Opening file in read mode
f = open("places.txt","r")
# print(f.readline()) //function is used to read the file line by line
print(f.read())
f.close()

"""
# Opening file in write mode
f = open("places.txt","w")
print(f.write("5) Roam on the roads in nights"))
f.close()
"""

"""
# Opening file in append mode
f = open("places.txt","a")
print(f.write("\n6) Roam on the roads in nights"))
f.close()
"""

