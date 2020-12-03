
bool_var = False
none_var = None
str_empty = ''
str_var = 'Test'
int_var0 = 0
int_var = 5

# if <condition>:
#     pass
# else:
#     pass
if int_var:
    print('Condition satisfied')
else:
    print('Something went wrong!')

if 5 > 3:
    print('Condition satisfied')
else:
    print('Something went wrong!')

if 5 > 5:
    print('Condition satisfied')
else:
    print('Something went wrong!')

if 5 == 5:
    print('Condition satisfied')
else:
    print('Something went wrong!')

if 5 != 5:
    print('Condition satisfied')
else:
    print('Something went wrong!')

if 'test' > 'test':
    print('Condition satisfied')
else:
    print('Something went wrong!')

if 'test' > 'test':
    print('Condition satisfied')
else:
    print('Something went wrong!')

if not False:
    print('Condition satisfied')
else:
    print('Something went wrong!')

if not True:
    print('Condition satisfied')
else:
    print('Something went wrong!')

if not '':
    print('element not found')

# print(str_var)

str_empty = ''
str_var = 'test'
bool_var = True

if (5 > 3) and (str_var):
    print('Condition satisfied')
else:
    print('Something went wrong!')

if (5 > 8) and (str_var):
    print('Condition satisfied')
else:
    print('Something went wrong!')

if (5 > 8) or (False):
    print('Condition satisfied')
else:
    print('Something went wrong!')


if 5 > 8:
    print('If rules')
elif 5 > 7:
    print('elif 1 works')
elif 5 > 4:
    print('elif 2 works')
else:
    print('else')

