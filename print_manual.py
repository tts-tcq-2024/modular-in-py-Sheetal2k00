from color_code import MAJOR_COLORS, MINOR_COLORS, get_color_from_pair_number

def print_reference_manual():
    print("25-Pair Color Code Reference Manual")
    print("---------------------------------")
    for i in range(1, 26):
        major_color, minor_color = get_color_from_pair_number(i)
        print(f"{i}: Major Color - {major_color}, Minor Color - {minor_color}")
