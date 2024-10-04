Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
students = {
    "Noah": {
    "maths": 5,
    "biology": 2,
    "geography": 3,
    "Russian": 5,
    "English": 5,
    "PE": 5,
    "physics": 4,
    "programming": 4
},
    "Oliver": {
    "maths": 4,
    "biology": 4,
    "geography": 5,
    "Russian": 5,
    "English": 5,
    "PE": 3,
    "physics": 2,
    "programming": 5
},
    "Arthur": {
    "maths": 2,
    "biology": 3,
    "geography": 4,
    "Russian": 5,
    "English": 2,
    "PE": 3,
    "physics": 4,
    "programming": 5
}
}
print(students["Noah"]["maths"])
students["Oliver"]["biology"] = 3