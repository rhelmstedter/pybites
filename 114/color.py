import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, "color_values.py")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/color_values.py", color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(self.color.upper(), None)

    @staticmethod
    def hex2rgb(self):
        """Class method that converts a hex value into an rgb one"""
        red = int(self[1:3], 16)
        green = int(self[3:5], 16)
        blue = int(self[5:], 16)
        return red, green, blue

    @staticmethod
    def rgb2hex(self):
        """Class method that converts an rgb value into a hex one"""
        hex_color = "#"
        for value in self:
            if not isinstance(value, int):
                raise ValueError

            if 0 <= value <= 255:
                hex_color += f"{hex(value).lstrip('0x'):02}"
            else:
                raise ValueError
        return hex_color

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if not self.rgb:
            return "Unknown"
        return f"{self.rgb}"
