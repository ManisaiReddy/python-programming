person_info={
    "name":"Manisai",
    "age": 24,
    "salary":95000.34,
    "address":{
        "village":"Chalvai",
        "mondal":"Govindaraopet",
        "dist":"Mulugu",
        "pin":506343
    }
}
print(person_info['address']['pin'], type(person_info['address']['pin']))

college_info = dict(name="BITS", Branch = "ece", section = "A")
print(college_info)

# print(college_info["gate"])
print("e" in college_info)
print(college_info.get('a','missing'))
print(college_info['a'] if 'a' in college_info else 0 )
print(college_info.keys())
print(college_info.values())
print(college_info.items())

I = iter(college_info.keys())
print(next(I))
print(next(I))
print(next(I))
# print(next(I)) stop iteration

for k in college_info:
    print(college_info.keys())
