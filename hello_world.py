# 1.
print("Hello World")

# 2.
#a
name = "Kate"

print("Hello", name,"!")

#b
name = "Kate"

print("Hello " + name +"!")


# 3.
#a
fav_num = 27

print("Hello " , 27,"!")

#b
fav_num = 27

# print("Hello " + 27 +"!")

#solution provided for fix
print("Hello " + str(27) + "!")

# 4.
#a
fav_food1 = "Tacos"
fav_food2 = "Chips"

print("I love to eat {} and {}.".format(fav_food1,fav_food2))

#b
fav_food1 = "Tacos"
fav_food2 = "Chips"

print(f"I love to eat {fav_food1} and {fav_food2}.")