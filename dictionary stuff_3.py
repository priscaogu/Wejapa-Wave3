

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the keys in the basket\
# search using thekeys for items in fruits\
#and items not in fruits
for key in basket_items:
    if key in fruits:
        fruit_count +=basket_items[key]
    else:
        not_fruit_count += basket_items[key]



print(fruit_count, not_fruit_count)