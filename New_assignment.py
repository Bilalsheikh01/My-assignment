num_list: list = []
name = str(input("Hello! my name is: "))
for y in range(1,4):
    number = int(input(f"My favorite {y} number is: "))
    num_list.append(number)
    
print(f"\n{name}, Let's explore your favorite number.")
for item in num_list:
    if item % 2 == 0:
        print(f"The number {item} is an even number.")
    else:
        print(f"The number {item} is an odd number.")
      
for item in num_list:
    print(f"The number {item} and it's square: ({item}, {item ** 2})")

total_sum = sum(num_list)
print(f"\n Amazing! The sum of my favorite numbers is: {total_sum}")

prime = True
if total_sum <= 1:
    prime = False

for x in range(2, total_sum):
    if total_sum % x == 0:
        prime = False

if prime:
    print(f"WOW! my favorite number {total_sum} is prime number.")
else:
      print(f"WOW! my favorite number {total_sum} is not a prime number.")      