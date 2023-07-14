names = []
for i in range(5):
    name = input("Please enter your name of someone you know  ")
    names.append(name)
    lowercased = [name.lower() for name in names]
    titlecased = [name.title() for name in lowercased]

    invitations = [f"Dear {name}, please come to my birfday party" for name in titlecased]
    for invitation in invitations:
        print(invitation)