from main import House
house_one = House("1_kitchen", "blue", "3_bedroom", "three_master_en_suite", "75,000")
house_two = House("2_kitchen", "black", "2_bedroom", "two_master_en_suite", "50,000")
house_three = House("3_kitchen", "white", "1_bedroom", "one_master_en_suite", "20,000")

print(house_one.kitchen)
print(house_two.kitchen)
print(house_three.kitchen)

print(house_one.color)
print(house_two.color)
print(house_three.color)

print(house_one.bedroom)
print(house_two.bedroom)
print(house_three.bedroom)

print(house_one.master_en_suite)
print(house_two.master_en_suite)
print(house_three.master_en_suite)

print(house_one.cost)
print(house_two.cost)
print(house_three.cost)


