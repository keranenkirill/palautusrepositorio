from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, Or, Not, HasAtLeast, HasFewerThan, PlaysIn, All


def main():
    # URL pelaajadataan
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    print("Kysely: Vähintään 45 maalia TAI vähintään 70 syöttöä")
    matcher1 = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    for player in stats.matches(matcher1):
        print(player)

    print("\nKysely: Vähintään 70 pistettä ja joukkue NYR, FLA tai BOS")
    matcher2 = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher2):
        print(player)

    print("\nKysely: Kaikki pelaajat (All)")
    all_players = stats.matches(All())
    print(f"Pelaajia yhteensä: {len(all_players)}")

    print("\nKysely: Pelaajat, joilla on vähemmän kuin 2 maalia ja joukkue NYR")
    matcher4 = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher4):
        print(player)


if __name__ == "__main__":
    main()
