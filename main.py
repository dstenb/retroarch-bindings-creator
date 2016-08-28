import argparse

from joysticks import get_joysticks
from n64 import N64Bindings
from ps3 import PS3Bindings
from xbox360 import Xbox360Bindings


# A list of mappings between Retroarch's controller bindings to the physical
# controllers:
# https://github.com/retropie/retropie-setup/wiki/retroarch-configuration


FULL_NAME_MAPPINGS = {
    "n64:0": "HuiJia  USB GamePad:0",
    "n64:1": "HuiJia  USB GamePad:1",
    "ps3:0": "Sony PLAYSTATION(R)3 Controller:0",
    "ps3:1": "Sony PLAYSTATION(R)3 Controller:0",
    "xbox360:0": "Xbox 360 Wireless Receiver:0",
    "xbox360:1": "Xbox 360 Wireless Receiver:1",
    "xbox360:2": "Xbox 360 Wireless Receiver:2",
    "xbox360:3": "Xbox 360 Wireless Receiver:3",
}


BINDING_KEYS = [
    "b_btn", "b_axis",
    "y_btn", "y_axis",
    "select_btn", "select_axis",
    "start_btn", "start_axis",
    "up_btn", "up_axis",
    "down_btn", "down_axis",
    "left_btn", "left_axis",
    "right_btn", "right_axis",
    "a_btn", "a_axis",
    "x_btn", "x_axis",
    "l_btn", "l_axis",
    "r_btn", "r_axis",
    "l2_btn", "l2_axis",
    "r2_btn", "r2_axis",
    "l3_btn", "l3_axis",
    "r3_btn", "r3_axis",
    "l_x_plus", "l_x_plus_btn", "l_x_plus_axis",
    "l_x_minus", "l_x_minus_btn", "l_x_minus_axis",
    "l_y_plus", "l_y_plus_btn", "l_y_plus_axis",
    "l_y_minus", "l_y_minus_btn", "l_y_minus_axis",
    "r_x_plus", "r_x_plus_btn", "r_x_plus_axis",
    "r_x_minus", "r_x_minus_btn", "r_x_minus_axis",
    "r_y_plus", "r_y_plus_btn", "r_y_plus_axis",
    "r_y_minus", "r_y_minus_btn", "r_y_minus_axis",
    "turbo", "turbo_btn", "turbo_axis"]


def create_bindings(gamepad, player_no, system):
    joystick_bindings = {
        "n64:0": N64Bindings(),
        "n64:1": N64Bindings(),
        "ps3:0": PS3Bindings(),
        "ps3:1": PS3Bindings(),
        "xbox360:0": Xbox360Bindings(),
        "xbox360:1": Xbox360Bindings(),
        "xbox360:2": Xbox360Bindings(),
        "xbox360:3": Xbox360Bindings()
    }

    assert player_no > 0
    data = {k: "nul" for k in BINDING_KEYS}
    data.update(joystick_bindings[gamepad].create(system))

    output = []

    joysticks = get_joysticks()
    udev_index = joysticks[FULL_NAME_MAPPINGS[gamepad]]

    output.append("input_player{}_joypad_index = \"{}\"".format(
        player_no, udev_index))

    for key, value in sorted(data.items()):
        output.append("input_player{}_{} = \"{}\"".format(
            player_no, key, value))

    return "\n".join(output)


def parse_args():
    parser = argparse.ArgumentParser(description=\
            "Generate a Retroarch configuration file.")
    parser.add_argument("-j", dest="joystick", required=True, \
            choices=FULL_NAME_MAPPINGS.keys())
    parser.add_argument("-p", dest="player", required=True, type=int)
    parser.add_argument("-s", dest="system", required=True)
    parser.add_argument("-o", dest="path", required=True)

    return parser.parse_args()


def main():
    args = parse_args()
    output = create_bindings(args.joystick, args.player, args.system)

    with open(args.path, "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
