#Python Program to add a record to nested dictionary
  # people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},
   #       2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}
t={1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"}, 2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}
t[1]['chaitanya']=24
t[2]['krishna']=23
print(t)
