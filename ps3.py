# Sixaxis controller


PS3_UDEV_MAPPING = {
    "Cross": "14",
    "Square": "15",
    "Triangle": "12",
    "Circle": "13",
    "Select": "0",
    "Start": "3",
    "D up": "4",
    "D down": "6",
    "D left": "7",
    "D right": "5",
    "L": "10",
    "R": "11",
    "LT": "+12",
    "RT": "+13",
    "Ps": "16",
    "L analog left": "-0",
    "L analog right": "+0",
    "L analog up": "-1",
    "L analog down": "+1",
    "R analog left": "-2",
    "R analog right": "+2",
    "R analog up": "-3",
    "R analog down": "+3",
    "L thumb": "1",
    "R thumb": "2"
}

PS3_DEFAULT_BINDINGS = {
    "b_btn": "Cross", # down
    "y_btn": "Square", # left
    "a_btn": "Triangle", # right
    "x_btn": "Circle", # top
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


PS3_NES_BINDINGS = {
    "b_btn": "Square",
    "a_btn": "Cross",
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


class PS3Bindings(object):

    def __init__(self):
        self.bindings = {
            "default": PS3_DEFAULT_BINDINGS,
            "snes": PS3_DEFAULT_BINDINGS,
            "nes": PS3_NES_BINDINGS,
            "pce": PS3_NES_BINDINGS
        }

    def _apply_mapping(self, bindings):
        result = {}

        for key, value in bindings.items():
            result[key] = PS3_UDEV_MAPPING[value]

        return result

    def create(self, system="default"):
        bindings = self._apply_mapping(self.bindings[system])

        if system in ["nes", "pce", "snes"]:
            bindings["analog_dpad_mode"] = "1"
        else:
            bindings["analog_dpad_mode"] = "0"

        return bindings
