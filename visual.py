from City import *


def read_input_file(file):
    with open(file) as f:
        info = f.readlines()
    return info


if __name__ == '__main__':
    information = read_input_file("a_example.in")
    # informa1tion = read_input_file("b_short_walk.in")
    # information = read_input_file("c_going_green.in")
    # information = read_input_file("d_wide_selection.in")
    # information = read_input_file("e_precise_fit.in")
    # information = read_input_file("f_different_footprints.in")

    new_city = City(information)
    new_city.build()
    score = new_city.get_score()

    res = []
    res.append(len(new_city.utilities) + len(new_city.utilities))

    for r in new_city.residentials:
        house = new_city.residentials[r]
        res.append([house.project_number, house.left_top_corner[0], house.left_top_corner[1]])

    for u in new_city.utilities:
        res.append([u.project_number, u.left_top_corner[0], u.left_top_corner[1]])

    f = open('submission.txt', 'w')
    for l in res:
        f.write(str(l)+'\n')

