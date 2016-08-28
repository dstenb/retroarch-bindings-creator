# Mapping for the Mayflash/HuiJie N64 controller adapter


N64_UDEV_MAPPING = {
    "A": "1",
    "B": "2",
    "Z": "8",
    "Start": "9",
    "D up": "12",
    "D down": "14",
    "D left": "15",
    "D right": "13",
    "Analog left": "-0",
    "Analog right": "+0",
    "Analog up": "-1",
    "Analog down": "+1",
    "L": "6",
    "R": "7",
    "C up": "-2",
    "C down": "+2",
    "C left": "+3",
    "C right": "-3"
}


N64_BINDINGS = {
    "b_btn": "B",
    "a_btn": "A",
    "l2_btn": "Z",
    "start_btn": "Start",
    "up_btn": "D up",
    "down_btn": "D down",
    "left_btn": "D left",
    "right_btn": "D right",
    "l_btn": "L",
    "r_btn": "R",
    "l_x_plus_axis": "Analog right",
    "l_x_minus_axis": "Analog left",
    "l_y_plus_axis": "Analog down",
    "l_y_minus_axis": "Analog up",
    "r_x_plus_axis": "C right",
    "r_x_minus_axis": "C left",
    "r_y_plus_axis": "C down",
    "r_y_minus_axis": "C up"
}



class N64Bindings(object):

    def __init__(self):
        self.bindings = {
            "n64": N64_BINDINGS
        }

    def _apply_mapping(self, bindings):
        result = {}

        for key, value in bindings.items():
            result[key] = N64_UDEV_MAPPING[value]

        return result

    def create(self, system):
        return self._apply_mapping(self.bindings[system])
