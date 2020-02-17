# Q.27

class Country:

    def __init__(self, name, popl, area):
        self.name = name
        self.popl = popl
        self.area = area

    def is_larger(self, country1, country2):
        return country1.area > country2.area

    def __str__(self):
        return "{0} has a population of {1} and is {2} sq.km.".format(self.name, self.popl, self.area)


# Q.28
class Continent:

    def __init__(self, name, list_of_c):
        self.name = name
        self.list_of_c = list_of_c

    def total_population(self):
        total_p = 0

        for country in self.list_of_c:
            total_p += country.popl

        return total_p

    def total_area(self):
        total_a = 0

        for country in self.list_of_c:
            total_a += country.area

        return total_a

    def __str__(self):
        p = self.total_population()
        a = self.total_area()

        return "{} has a popl. of {} and is {} sq.km.".format(self.name, p, a)


def main():
    usa = Country("USA", 100000, 200000)
    canada = Country("Canada", 90000, 190000)
    india = Country("India", 1500000000, 100000)

    print(india.__str__())
    print(usa.is_larger(canada, india))

    africa = Continent("Africa", (usa, canada, india))
    print(africa.__str__())


if __name__ == "__main__":
    main()
