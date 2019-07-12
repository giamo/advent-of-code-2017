def puzzle1(location):
    """
    Find the manhattan distance between the location and square 1

    The solution uses the fact that the sequence of bottom right numbers of each "ring"
    is the sequence of squared roots of odd numbers
    """
    return find_location_distance(location, find_ring_number(location))


def find_ring_number(location):
    """Finds which concentric ring the input location belongs to (the first ring is 0)"""
    ring_number = 0
    next_odd = 1
    next_odd_squared = 1
    while location > next_odd_squared:
        next_odd += 2
        next_odd_squared = next_odd ** 2
        ring_number += 1
    return ring_number


def find_location_distance(location, ring_number):
    """Given a location and the ring it belongs to, find the coordinates in the grid"""
    ring_side_length = 1 + 2 * ring_number
    bottom_right_location = ring_side_length ** 2
    if location == 1:
        return 0

    if bottom_right_location - ring_side_length + 1 <= location <= bottom_right_location:
        last_side_number = bottom_right_location
        x_distance = abs(location - (last_side_number - ring_side_length // 2))
        y_distance = ring_number
    elif bottom_right_location - 2 * ring_side_length + 2 <= location <= bottom_right_location - ring_side_length + 1:
        last_side_number = bottom_right_location - ring_side_length + 1
        x_distance = ring_number
        y_distance = abs(location - (last_side_number - ring_side_length // 2))
    elif bottom_right_location - 3 * ring_side_length + 3 <= location <= bottom_right_location - 2 * ring_side_length + 2:
        last_side_number = bottom_right_location - 2 * ring_side_length + 2
        x_distance = abs(location - (last_side_number - ring_side_length // 2))
        y_distance = ring_number
    else:
        last_side_number = bottom_right_location - 3 * ring_side_length + 3
        x_distance = ring_number
        y_distance = abs(location - (last_side_number - ring_side_length // 2))
    return x_distance + y_distance


def main():
    print('Solution for day 1, puzzle 1: %s' % puzzle1(289326))


if __name__ == '__main__':
    main()
