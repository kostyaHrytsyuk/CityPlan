from City import City
from Building import Building


def show(data):
    with open("a_example.in") as f:
        # for line in f:
        #     print(line)
        info = f.readlines()
    return info


def make_city(data):
    result = []
    city_info = [data[0]]

    def parse_building(data):

        result = []
        construction_building = []

        for index_element in range(1, len(data)):
            temporary_lst = []

            if data[index_element][0] == 'R' or data[index_element][0] == 'U':
                length = data[index_element][2]
                result.append(data[index_element])
                temporary_lst = data[int(index_element+1):int(index_element)+1+int(length)]
                construction_building.append(temporary_lst)
        return [result, construction_building]

    new = parse_building(data)
    result = city_info + new

    return result


if __name__ == '__main__':
    data = "a_example.in"
    information = show(data)

    sorted_information = make_city(information)

    new_city = City(sorted_information[0])

    for build in range(len(sorted_information[1])):

        info_about_building = sorted_information[1][build]

        construction = sorted_information[2][build]

        new_build = Building(info_about_building, construction)

        new_city.possible_building.append(new_build)

    for i in new_city.possible_building:
        print(i.structura)
        # for j in i.structura:
