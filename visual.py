from City import City
from Building import Building


def read_input_file(file):
    with open(file) as f:
        info = f.readlines()
    return info


def make_city(city_data):
    city_info = [city_data[0]]

    def parse_building(data):

        build_info = []
        construction_building = []

        for index_element in range(1, len(data)):
            if data[index_element][0] == 'R' or data[index_element][0] == 'U':
                length = data[index_element][2]
                build_info.append(data[index_element])
                temporary_lst = data[int(index_element+1):int(index_element)+1+int(length)]
                construction_building.append(temporary_lst)
        return [build_info, construction_building]

    new = parse_building(city_data)
    result = city_info + new

    return result


if __name__ == '__main__':
    information = read_input_file("a_example.in")

    sorted_information = make_city(information)

    new_city = City(sorted_information[0])

    for build in range(len(sorted_information[1])):

        info_about_building = sorted_information[1][build]

        construction = sorted_information[2][build]

        new_build = Building(info_about_building, construction)

        new_city.possible_building.append(new_build)

    for i in new_city.possible_building:
        print(i.get_building_size())
