from City import *


def read_input_file(file):
    with open(file) as f:
        info = f.readlines()
    return info


if __name__ == '__main__':
    # information = read_input_file("a_example.in")
    # information = read_input_file("b_short_walk.in")
    # information = read_input_file("c_going_green.in")
    # information = read_input_file("d_wide_selection.in")
    # information = read_input_file("e_precise_fit.in")
    information = read_input_file("f_different_footprints.in")

    new_city = City(information)
    new_city.build()
    score = new_city.get_score()
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

    print(score)
