Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
employees = {
    "Harry": 10000,
    "Jacob": 20000,
    "Charley": 13500,
    "Thomas": 13000,
    "George": 15000,
    "Oscar": 50000,
    "James": 25000,
    "William": 24500
}
print(dict(sorted(employees.items(), key=lambda item: item[1])))
print(dict(sorted(employees.items())))