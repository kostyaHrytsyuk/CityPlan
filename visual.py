from City import *


def read_input_file(file):
    with open(file) as f:
        info = f.readlines()
    return info


if __name__ == '__main__':
    information = read_input_file("a_example.in")
    # information = read_input_file("b_short_walk.in")
    # information = read_input_file("c_going_green.in")
    # information = read_input_file("d_wide_selection.in")
    # information = read_input_file("e_precise_fit.in")
    # information = read_input_file("f_different_footprints.in")

    new_city = City(information)
    new_city.build()
    score = new_city.get_score()

    print(score)
