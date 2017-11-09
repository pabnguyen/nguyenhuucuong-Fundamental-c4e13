inventory ={
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gamestone'],
    'backpack': ['xylophone', 'dragger', 'bedroll', 'bread loaf'],
}

inventory['pocket'] = ['seashell', 'strange Berry', 'lint']
inventory['backpack'].remove("dragger")
inventory['gold'] += 50
print(inventory)
