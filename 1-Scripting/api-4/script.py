for number in range(1, 20):
  is_divisible_by_3 = number % 3 == 0
  is_divisible_by_5 = number % 5 == 0
  if(is_divisible_by_3 and is_divisible_by_5):
    print("Fizz Buzz")
    continue
  if(is_divisible_by_3):
    print("Fizz")
    continue
  if(is_divisible_by_5):
    print("Buzz")
    continue
  print(number)