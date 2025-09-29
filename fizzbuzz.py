# Problem

# Write a function that prints the numbers from 1 to n.
# 	•	For multiples of 3, print "Fizz".
# 	•	For multiples of 5, print "Buzz".
# 	•	For multiples of both 3 and 5, print "FizzBuzz".
# 	•	Otherwise, just print the number.

n = 15

def fizzbuzz(n):
    fizzbuzz_list = []

    for i in range(1, n+1):
        if i % 15 == 0:
            fizzbuzz_list.append("FizzBuzz")
        elif i % 3 == 0:
            fizzbuzz_list.append("Fizz")
        elif i % 5 == 0:
            fizzbuzz_list.append("Buzz")
        else:
            fizzbuzz_list.append(i)
    
    return fizzbuzz_list

print(fizzbuzz(n))

for item in fizzbuzz(n):
    print(item)    

