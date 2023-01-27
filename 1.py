count = input("Введите количество чисел\n")
while count == "":
  count = input("Необходимо ввести количество чисел\n Введите количесвто чисел\n")

res = 0

numbers = []
for i in range(int(count)):
  numbers.append(int(input()))

action = input("Выберите действие(+,-,/,*)")

res = 0

match action:
  case "+":
    for i in numbers:
      res+=i
  case "-":
    for i in numbers:
      res-=i
  case "*":
    res = 1
    for i in numbers:
      res*=i
  case "/":
    res = 1
    for i in numbers:
      res/=i

print(res)