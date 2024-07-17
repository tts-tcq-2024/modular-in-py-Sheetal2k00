MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def get_color_from_pair_number(pair_number):
    zero_based = pair_number - 1
    major_index, minor_index = divmod(zero_based, len(MINOR_COLORS))
    if major_index >= len(MAJOR_COLORS) or minor_index >= len(MINOR_COLORS):
        raise Exception('Index out of range')
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major, minor):
    try: major_index = MAJOR_COLORS.index(major)
    except ValueError: raise Exception('Major index out of range')
    try: minor_index = MINOR_COLORS.index(minor)
    except ValueError: raise Exception('Minor index out of range')
    return major_index * len(MINOR_COLORS) + minor_index + 1

def print_reference_manual():
    for i in range(1, 26):
        major, minor = get_color_from_pair_number(i)
        print(f"{i}: {major} {minor}")

def test_functions():
    assert(get_color_from_pair_number(4) == ('White', 'Brown'))
    assert(get_color_from_pair_number(5) == ('White', 'Slate'))
    assert(get_pair_number_from_color('Black', 'Orange') == 12)
    assert(get_pair_number_from_color('Violet', 'Slate') == 25)
    print('All tests passed.')

if __name__ == "__main__":
    test_functions()
    print_reference_manual()
