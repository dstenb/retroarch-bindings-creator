XBOX360_UDEV_MAPPING = {
    "A": "0",
    "B": "1",
    "X": "2",
    "Y": "3",
    "Select": "6",
    "Start": "7",
    "D up": "13",
    "D down": "14",
    "D left": "11",
    "D right": "12",
    "L": "4",
    "R": "5",
    "LT": "+2",
    "RT": "+5",
    "Xbox": "8",
    "L analog left": "-0",
    "L analog right": "+0",
    "L analog up": "-1",
    "L analog down": "+1",
    "R analog left": "-3",
    "R analog right": "+3",
    "R analog up": "-4",
    "R analog down": "+4",
    "L thumb": "9",
    "R thumb": "10"
}

XBOX360_DEFAULT_BINDINGS = {
    "b_btn": "A", # down
    "y_btn": "X", # left
    "a_btn": "B", # right
    "x_btn": "Y", # top
    "select_btn": "Select",
    "start_btn": "Start",
    "up_btn": "D up",
    "down_btn": "D down",
    "left_btn": "D left",
    "right_btn": "D right",
    "l_btn": "L",
    "r_btn": "R",
    "l2_axis": "LT",
    "r2_axis": "RT",
    "l3_btn": "L thumb",
    "r3_btn": "R thumb",
    "l_x_plus_axis": "L analog right",
    "l_x_minus_axis": "L analog left",
    "l_y_plus_axis": "L analog down",
    "l_y_minus_axis": "L analog up",
    "r_x_plus_axis": "R analog right",
    "r_x_minus_axis": "R analog left",
    "r_y_plus_axis": "R analog down",
    "r_y_minus_axis": "R analog up"
}


XBOX360_NES_BINDINGS = {
    "b_btn": "X",
    "a_btn": "A",
    "select_btn": "Select",
    "start_btn": "Start",
    "up_btn": "D up",
    "down_btn": "D down",
    "left_btn": "D left",
    "right_btn": "D right",
    "l_x_plus_axis": "L analog right",
    "l_x_minus_axis": "L analog left",
    "l_y_plus_axis": "L analog down",
    "l_y_minus_axis": "L analog up"
}


class Xbox360Bindings(object):

    def __init__(self):
        self.bindings = {
            "default": XBOX360_DEFAULT_BINDINGS,
            "nes": XBOX360_NES_BINDINGS,
            "pce": XBOX360_NES_BINDINGS,
            "snes": XBOX360_DEFAULT_BINDINGS,
        }

    def _apply_mapping(self, bindings):
        result = {}

        for key, value in bindings.items():
            result[key] = XBOX360_UDEV_MAPPING[value]

        return result

    def create(self, system="default"):
        bindings = self._apply_mapping(self.bindings[system])

        if system in ["nes", "pce", "snes"]:
            bindings["analog_dpad_mode"] = "1"
        else:
            bindings["analog_dpad_mode"] = "0"

        return bindings
