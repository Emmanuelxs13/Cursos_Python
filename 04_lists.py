#  Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [36, 1.77, "Emmanuel", "Berrio"]

print(type(my_list))
print(type(my_other_list))

print("Mi edad:", my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)