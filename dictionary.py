
def add_person():

       name = input("enter the name")
       age = input("enter the age")

       d = {
            "name": name,
            "age": age
        }
       return d


people = []


while True:
    command = input("enter the task add/delete/search").lower()
    if command == "a":
        person = add_person()
        people.append(person)
        print("person added")
        

    elif command == "d":
            pass
    elif command == "s":
            pass
    elif command=="q":
            break
    else:
            print("invalid input")

print(people)
