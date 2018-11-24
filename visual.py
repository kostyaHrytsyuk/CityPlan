from City import City


def show(data):
    with open("a_example.in") as f:
        # for line in f:
        #     print(line)
        info = f.readlines()
    return info


def make_city(data, new_city: City):

    city_info = []
    building_info = []
    count = 0

    for element in data:
        if count == 0:
            city_info = element.split(" ")
            for i in city_info:
                i.replace("\n", '')
            print(city_info)

    return city_info


if __name__ == '__main__':
    data = "a_example.in"
    information = show(data)
    # print(information)
    # first_data = information[0].split(" ")
    # print("Here",first_data)
    # for i in information:
    #     print(i)
    new_city = City()
    make_city(information, new_city)