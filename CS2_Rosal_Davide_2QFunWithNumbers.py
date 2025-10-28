age = int(input("Hi there! Please enter your age: ")) 
total_sum = 0 
for num in range (1, age+1, 1):
 total_sum += num 
print("The sum of all numbers from 1 to",age, "is:",total_sum)