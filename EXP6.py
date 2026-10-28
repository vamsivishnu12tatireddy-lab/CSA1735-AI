
rooms = {
    "A": input("Enter status of room A (Dirty/Clean): ").lower(),
    "B": input("Enter status of room B (Dirty/Clean): ").lower()
}

position = input("Enter starting position (A/B): ").upper()

while "dirty" in rooms.values():
    print("Vacuum is in room", position)

    if rooms[position] == "dirty":
        print("Cleaning room", position)
        rooms[position] = "clean"

    position = "B" if position == "A" else "A"

print("Both rooms are clean!")