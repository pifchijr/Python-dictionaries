Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
fruits = {
    "apples": 5,
    "bananas": 10,
    "peaches": 15,
    "mangos": 20
}
print(fruits["apples"])
fruits["oranges"] = 25
for key in fruits:
  print(key, fruits[key])
for key, value in fruits.items():
  print(key, 1.05 * value)