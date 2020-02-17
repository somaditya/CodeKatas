class Country:

    def __init__(self, name, popl, area):
        self.name = name
        self.popl = popl
        self.area = area

    def is_larger(self, country1, country2):
        return country1.area > country2.area

    def __str__(self):
        return "{0} has a population of {1} and is {2} sq.km.".format(self.name, self.popl, self.area)


def main():
    usa = Country("USA", 100000, 200000)
    canada = Country("Canada", 90000, 190000)
    india = Country("India", 1500000000, 100000)

    print(india.__str__())
    print(usa.is_larger(canada, india))


if __name__ == "__main__":
    main()
