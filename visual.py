from City import *


def read_input_file(file):
    with open(file) as f:
        info = f.readlines()
    return info


if __name__ == '__main__':
    information = read_input_file("a_example.in")

    new_city = City(information)

    for i in new_city.possible_utilities:
        i.draw()
        print(i.get_building_size())
