import math
import calendar


def main():
    floor = math.floor(-3.6)
    print(floor)

    rounded = abs(round(-5.6))
    print(rounded)

    leap_count = 0

    for year in (range(2000, 2050)):
        if calendar.isleap(year):
            leap_count += 1

    print("leap years:", leap_count)

    day_of_week = calendar.weekday(2018, 9, 26)
    print(day_of_week)

    season = "summer"

    new_season = "Ilove" + season + "!"
    print(new_season)

    side1 = 4
    side2 = 5
    side3 = 6

    print("The sides have lengths", side1, ",", side2, ",", side3, ".")

    ids = [5343, 1234, 5692, 3245, 9764, 2538]

    ids.remove(3245)
    print(ids)

    print(ids.index(9764))

    ids.insert(4, 5588)
    print(ids)

    ids.extend([4363, 2368])
    print(ids)

    ids.reverse()
    print(ids)

    ids.sort()
    print(ids)

    temps = [22.5, 17.8, 30.4, 26.9, 27, 23.5, 18.6]

    temps.sort()
    print(temps)

    cool_temps = temps[:2]
    print(cool_temps)

    warm_temps = temps[3:]
    print(warm_temps)

    temps_in_celsius = cool_temps + warm_temps
    print(temps_in_celsius)

    units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]

    print(units[0])
    print(units[1])
    print(units[0][0])
    print(units[1][0])
    print(units[0][1:])
    print(units[1][0:2])

    print("Alkaline Earth Metals")
    print("+++++++++++++++++++++")
    alkaline_earth_metals = [[4, 9.012], [12, 24.305], [20, 40.078], [38, 87.63], [56, 137.327], [88, 226]]

    for metal in alkaline_earth_metals:
        print(metal)

    number_and_weight = []

    for metal in alkaline_earth_metals:
        for item in metal:
            number_and_weight.append(item)

    print(number_and_weight)

    cat_1 = [4, 4, 4, 4, 5, 5, 5, 5, 4, 7]
    cat_2 = [5, 5, 5, 5, 5, 6, 6, 6, 6, 6]

    if cat_1[0] > cat_2[0]:
        print("Cat 1 weighed more than cat 2 on day 1.")
    elif cat_1[0] < cat_2[0]:
        print("Cat 1 weighed less than cat 2 on day 1.")
    else:
        print("cat1 == cat2")

    if cat_1[0] > cat_2[0] and cat_1[9] > cat_2[9]:
        print("Cat 1 remained heavier than cat 2.")
    else:
        print("Cat 2 became heavier than Cat 1.")

    for n in range(34, 52):
        print(n, end=" ")

    print()

    for n in range(11, 0, -1):
        print(n, end=" ")

    def find_dups(list_ints=[]):
        dups_list = []

        for item in list_ints:
            if list_ints.count(item) > 1:
                dups_list.append(item)

        return set(dups_list)

    print()
    print(find_dups([1, 2, 3, 4, 5, 3, 4, 5, 5]))


if __name__ == "__main__":
    main()
