def laske_osamaara(a, b):
    """Laskee kahden luvun osamäärän."""
    if b == 0:
        raise ValueError("Nollalla jakaminen ei ole sallittua.")
    return a / b


if __name__ == "__main__":
    x = int(input("Anna ensimmäinen luku: "))
    y = int(input("Anna toinen luku: "))
    try:
        print(f"Lukujen {x} ja {y} osamäärä on {laske_osamaara(x, y)}")
    except ValueError as e:
        print(e)
