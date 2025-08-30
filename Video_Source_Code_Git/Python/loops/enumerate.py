# Looping through indices and values of a list
my_list = ["Simple","Easy","Python","Hello","World"]

for i in range(len(my_list)):
    print(i, my_list[i])

# Looping through indices and values of a list with index starting at 1 instead of 0
my_list = ["Simple","Easy","Python","Hello","World"]

for i in range(len(my_list)):
    print(i + 1, my_list[i])

# enumerate returns an enumerate object
my_list = enumerate(["Simple","Easy","Python","Hello","World"])
print(my_list)
print(type(my_list))

#In order to see what is inside the enumerate object, convert it into a list
# which produces a list of tuples. These tuples have index starting with 0 
# and list item corresponding to that index. 
print(list(enumerate(["Simple","Easy","Python","Hello","World"])))

# Using enumerate to print both index and value, index starting at 0
my_list = ["Simple","Easy","Python","Hello","World"]
for i, v in enumerate(my_list):
    print(i, v)

# Using enumerate to print both index and value, index starting at 1
my_list = ["Simple","Easy","Python","Hello","World"]
for i, v in enumerate(my_list, start = 1):
    print(i, v)

# Using enumerate to print both index and value, index starting at -5
my_list = ["Simple","Easy","Python","Hello","World"]
for i, v in enumerate(my_list, start = -5):
    print(i, v)

# If you try to print only either index or value using enumerate,
# it will end up producing a tuple of both index and value

my_list = ["Simple","Easy","Python","Hello","World"]
for i in enumerate(my_list):
    print(i)


my_list = ["Simple","Easy","Python","Hello","World"]
for v in enumerate(my_list):
    print(v)