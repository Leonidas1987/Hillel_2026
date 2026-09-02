class Romb:
    """Homework 9.1 - geometric figure 'Rhombus'."""

    def __init__(self, side_a, corner_a):
        self.side_a = side_a
        self.corner_a = corner_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Side a must be greater than 0")
            object.__setattr__(self, "side_a", value)

        elif name == "corner_a":
            if value <= 0 or value >= 180:
                raise ValueError("Corner a must be between 0 and 180 degrees")
            object.__setattr__(self, "corner_a", value)
            object.__setattr__(self, "corner_b", 180 - value)

        elif name == "corner_b":
            if value <= 0 or value >= 180:
                raise ValueError("Corner b must be between 0 and 180 degrees")
            object.__setattr__(self, "corner_b", value)
            object.__setattr__(self, "corner_a", 180 - value)

        else:
            object.__setattr__(self, name, value)


def sum_numbers(row):
    """Homework 11.1 - sum of comma-separated numbers in a string."""
    return sum(int(element) for element in row.split(","))


def longest_word(text):
    """Returns the longest word in a text."""
    words = text.split()
    if not words:
        raise ValueError("Empty text")
    return max(words, key=len)