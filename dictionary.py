
def add_person():

    name = input("enter the name")
    age = input("enter the age")

    d = {
        "name": name,
        "age": age
    }
    return d


people = []


command = input("enter the task add/delete/search").lowe()

if command == "a":
    person = add_person()
    people.append(person)
elif command == "d":
    pass
elif command == "s":
    pass
else:
    print("invalid input")
