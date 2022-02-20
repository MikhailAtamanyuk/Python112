d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
n = d.pop("name")
sal = d.pop("salary")
d1 = dict(name=n, salary=sal)
print(d)
print(d1)
# _________________________________________________________
d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
d["location"] = d.pop("city")
print(d)