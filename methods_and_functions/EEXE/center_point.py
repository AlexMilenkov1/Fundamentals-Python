from math import floor


def closet_to_0(coordinates):
    smallest_coordinate_nums = []

    for _ in range(len(coordinates)):
        smallest_coordinate_num = min(coordinates, key=abs)

        if smallest_coordinate_num not in smallest_coordinate_nums:
            smallest_coordinate_nums.append(smallest_coordinate_num)

        coordinates.remove(smallest_coordinate_num)

        if len(smallest_coordinate_nums) == 2:
            break

    return smallest_coordinate_nums


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

random_coordinates = [x1, y1, x2, y2]

result = closet_to_0(random_coordinates)

formatted_result = [floor(element) for element in result]

print(tuple(formatted_result))
