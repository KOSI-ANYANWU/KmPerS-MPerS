numbers= [1,2,3,4,5,6]

def print_evenodd(numbers):
    result = map (lambda x: 1 if x % 2 == 0 else 0, numbers)
    for value in result:
        print(value)

print_evenodd(numbers)