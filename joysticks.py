import sdl2


def get_joysticks():
    sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)

    num_joysticks = sdl2.SDL_NumJoysticks()

    joysticks = {}
    indexes = {}

    for index in range(num_joysticks):
        joystick = sdl2.SDL_JoystickOpen(index)
        name = sdl2.SDL_JoystickNameForIndex(index).decode("utf-8")
        jindex = indexes.get(name, 0)
        indexes[name] = jindex + 1
        joysticks[name + ":" + str(jindex)] = index

        sdl2.SDL_JoystickClose(joystick)

    return joysticks
