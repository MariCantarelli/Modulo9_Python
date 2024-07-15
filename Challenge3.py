employees = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
day = ['Ana', 'Marcos', 'Alice', 'Melissa']
night = ['Pedro', 'Sophia', 'Bruno']
was_car = ['Marcos', 'Alice','Bruno', 'Melissa']

#List 1 
list1 = set(was_car).intersection(night)
print(list1)

#List 2
list2 = set(was_car).intersection(day)
print(list2)

#List 3 
list3 = set(employees).difference(was_car)
print(list3)