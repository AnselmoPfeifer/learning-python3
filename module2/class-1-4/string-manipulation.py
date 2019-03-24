
my_string = 'my string is bla bla !!!'

print(my_string)
# my string is bla bla !!!
test_string = my_string.capitalize()
print(test_string)
# My string is bla bla !!!

test_string = my_string.endswith('!')
print(test_string)
# True

test_string = my_string.startswith('my')
print(test_string)
# True

test_string = my_string.upper()
print(test_string)
# MY STRING IS BLA BLA !!!

test_string = my_string.lower()
print(test_string)
# my string is bla bla !!!

my_strip_string = "   ABC    "
print(my_strip_string.strip())
# ABC
