print(sum(range(11)))

print('*' * 10)

l = list(range(100))

print(l)

# Q.24

males = {'Som', 'Nikhil', 'Pawan', 'Manoj', 'Vin'}
females = {'Sia', 'Jenny', 'Michelle', 'Kenny', 'Kate'}


def mating_pairs(set1, set2):
    list_pair = []
    for i in range(1, 6):
        list_pair.append((set1.pop(), set2.pop()))

    return list_pair


print(mating_pairs(males, females))

color = {'red': 1, 'green': 1, 'blue': 2}
color2 = {'red': 1, 'blue': 2}


def count_values(dict):
    distinct = set()

    for val in dict.values():
        distinct.add(val)

    return len(distinct)


print(count_values(color))


# 26
def dict_intersect(dict1, dict2):
    intersect = {}

    for pair1 in dict1.items():
        for pair2 in dict2.items():
            if pair1 == pair2:
                # print(pair1, '##', pair2)
                intersect[pair1[0]] = pair1[1]

    return intersect


print(dict_intersect(color, color2))
