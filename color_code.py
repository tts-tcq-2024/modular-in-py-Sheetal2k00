major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def get_color_from_pair_number(pair_number):
    if pair_number < 1 or pair_number > 25:
        raise ValueError(f"Invalid pair number: {pair_number}")
    major_index = (pair_number - 1) // len(minor_colors)
    minor_index = (pair_number - 1) % len(minor_colors)
    return major_colors[major_index], minor_colors[minor_index]

def get_pair_number_from_colors(major_color, minor_color):
    if major_color not in major_colors or minor_color not in minor_colors:
        raise ValueError(f"Invalid colors: {major_color}, {minor_color}")
    major_index = major_colors.index(major_color)
    minor_index = minor_colors.index(minor_color)
    return major_index * len(minor_colors) + minor_index + 1
