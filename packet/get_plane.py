def get_plane():
    race = input("Название пункта назначения рейса: ")
    number = random.randint(1000, 9999)
    type = random.randint(1, 99)

    return {
        "race": race,
        "number": number,
        "type": type,
    }