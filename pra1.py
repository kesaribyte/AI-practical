
def vaccum_agent(location, status):
    if status == "Dirty":
        return "suck"
    elif location == "A":
        return "move right"
    elif location == "B":
        return "move left"


rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

print("Initial environment:")
print(rooms)
print("Vacuum position:", location)

for i in range(4):
    status = rooms[location]
    action = vaccum_agent(location, status)

    print("\nCurrent location:", location)
    print("Room status:", status)
    print("Action:", action)

    if action == "suck":
        rooms[location] = "Clean"
    elif action == "move right":
        location = "B"
    elif action == "move left":
        location = "A"

print("\nFinal Environment:")
print(rooms)
