import json 
def add_person():

    name = input("enter the name")
    age = input("enter the age")

    d = {
        "name": name,
        "age": age
    }
    return d


def display(people):
    for i, person in enumerate(people):

        print("index:", str(i), "name", person["name"])


def delete_contact(people):
    display(people)
    while True:
        num = input("enter the number to delete")
        try:
            num = int(num)
            if (num < 0):
                print("the number is invalid")
            else:
                break
        except:
            print("cannot do")
    if not people:
        print("the list is empty")
    else:
        for i, person in enumerate(people):
            people.pop(i-1)


def search(people):
    search_name = input("enter the keywordto  search:")

    for person in people:
        if search_name in person["name"]:
            print("the element found at the index")
            result =[]
            result.append(person)
            display(result)

with open("contact.json","r") as f:
            people = json.load(f)["contact"]

while True:
    command = input("enter the task add/delete/search").lower()
    if command == "a":
        person = add_person()
        people.append(person)

        print("person added")

    elif command == "d":
        delete_contact(people)
    elif command == "s":
        search(people)
    elif command == "q":
        break
    else:
        print("invalid input")

print(people)
