# Bindings for the 8bitdo SFC30 controller


SFC30_UDEV_MAPPING = {
    "A": "0",
    "B": "1",
    "X": "3",
    "Y": "4",
    "Select": "10",
    "Start": "11",
    "D up": "-1",
    "D down": "+1",
    "D left": "-0",
    "D right": "+0",
    "L": "6",
    "R": "7",
}


SFC30_BINDINGS = {
    "b_btn": "B",
    "a_btn": "A",
    "x_btn": "X",
    "y_btn": "Y",
    "select_btn": "Select",
    "start_btn": "Start",
    "up_axis": "D up",
    "down_axis": "D down",
    "left_axis": "D left",
    "right_axis": "D right",
    "l_btn": "L",
    "r_btn": "R"
}


SFC30_NES_PCE_BINDINGS = {
    "b_btn": "Y",
    "a_btn": "B",
    "select_btn": "Select",
    "start_btn": "Start",
    "up_axis": "D up",
    "down_axis": "D down",
    "left_axis": "D left",
    "right_axis": "D right"
}


SFC30_GENESIS_BINDINGS = {
    "y_btn": "Y",
    "b_btn": "B",
    "a_btn": "A",
    "x_btn": "X",
    "l_btn": "L",
    "r_btn": "R",
    "select_btn": "Select",
    "start_btn": "Start",
    "up_axis": "D up",
    "down_axis": "D down",
    "left_axis": "D left",
    "right_axis": "D right"
}


class SFC30Bindings(object):

    def __init__(self):
        self.bindings = {
            "genesis": SFC30_GENESIS_BINDINGS,
            "nes": SFC30_NES_PCE_BINDINGS,
            "pce": SFC30_NES_PCE_BINDINGS,
            "snes": SFC30_BINDINGS
        }

    def _apply_mapping(self, bindings):
        result = {}

        for key, value in bindings.items():
            result[key] = SFC30_UDEV_MAPPING[value]

        return result

    def create(self, system):
        return self._apply_mapping(self.bindings[system])
