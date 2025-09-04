import math

num_items = int(input('Enter the number of items: '))
items_p_box = int(input('Enter the number of items per box: '))

box_needed = math.ceil(num_items / items_p_box)

print(f'For {num_items} items, packing {items_p_box} items per box, you will need {box_needed} boxes.')