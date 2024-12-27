add=lambda number1,number2: number1+number2
print(add(6,5))

numbers=[1,2,3,4,5,6,7,8,9,10]
# write to check whether the number is even or odd, you would get the number in the parameter
def evenorodd(number):
    if number % 2== 0:
      print(f"{number} is a even number")
    else:
      print(f"{number} is an odd number")

evenorodd(17) 
for a in range(len(numbers)):
   