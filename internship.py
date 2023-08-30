def find_index_of_darkest_street_light(road_length, non_working_street_lights):
    total_lamps = int(road_length / 20) + 1
    is_working = {}

    for non_working_light_index in non_working_street_lights:
        is_working[non_working_light_index] = False

    light_range = 9

    def intensity(lightIndex):
        result = 0
        leftmost = lightIndex - light_range
        rightmost = lightIndex + light_range
        for otherIndex in range(leftmost, rightmost + 1):
            if otherIndex >= 0 and otherIndex < total_lamps and is_working.get(otherIndex, True):
                result += 3 ** (-((lightIndex - otherIndex) * 20 / 90) ** 2)
        return result

    lowest_intensity_index = None

    for i in non_working_street_lights:
        if lowest_intensity_index is None or intensity(i) < intensity(lowest_intensity_index):
            lowest_intensity_index = i

    return lowest_intensity_index

print(find_index_of_darkest_street_light(200, [4,5,6]))