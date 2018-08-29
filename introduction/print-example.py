# using sep= and end on print content
country = 'Brazil'
province = 'Mato Grosso do Sul'
city = 'Campo Grande'
population = 900000

print (country, province, city, population , sep=', ', end='\n') # Brazil, Mato Grosso do Sul, Campo Grande, 900000

print (type(population)) # <class 'int'>
population = 'Test to String type'
print (type(population)) # <class 'str'>
population = 9.0
print (type(population)) # <class 'float'>
population = 9,0
print (type(population)) # <class 'tuple'>