names = []
ages = []
emails = []

for i in range(3):
    print("input", i+1)
    name = input("enter the name")
    age = input("enter the age")
    email = input("enter the age")

    names.append(name)
    ages.append(age)
    emails.append(email)


for n, a, e in names, ages, emails:
    print(n)
    print(a)
    print(e)
