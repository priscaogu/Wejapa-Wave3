#Unzip tuples
cast = (("Barney",72),("Robin" ,68),("Ted" , 72), ("Lily", 66), ("Marshal", 76))

name,heights = zip(*cast)

print(name)
print(heights)
