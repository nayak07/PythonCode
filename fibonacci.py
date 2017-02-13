first_value=0
second_value=1
fibonacci_list=[]

for i in range(10):
    next_value=first_value+second_value
    first_value=second_value
    second_value=next_value
    fibonacci_list.append(next_value)

print fibonacci_list
