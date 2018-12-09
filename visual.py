from City import *


def read_input_file(file):
    with open(file) as f:
        info = f.readlines()
    return info


if __name__ == '__main__':
    information = read_input_file("b_short_walk.in")

    new_city = City(information)
    new_city.build()

    # TODO: Rewrite according to new utilities collection structure
    # for i in new_city.possible_utilities:
    #     print("----Utility {}----".format(i.project_number))
    #     i.draw()
    #     print("Size : {}".format(i.size))
    #     print("Service type : {}".format(i.service_type))

    # for i in new_city.possible_residentials:
    #     print("----Residential {}----".format(i.project_number))
    #     i.draw()
    #     print("Size : {}".format(i.size))
    #     print("Capacity : {}".format(i.capacity))
    #     size = i.size
    #     print("Profit : {}".format(i.profit))

    print()
