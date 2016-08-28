#! /bin/bash

OUTPUT_PATH="$HOME/.config/retroarch/bindings"

mkdir -p $OUTPUT_PATH

# Super Nintendo
python3 main.py -j xbox360:0 -p 1 -s snes -o $OUTPUT_PATH/snes_p1.cfg
python3 main.py -j xbox360:1 -p 2 -s snes -o $OUTPUT_PATH/snes_p2.cfg
python3 main.py -j ps3:0 -p 1 -s snes -o $OUTPUT_PATH/snes_p1.cfg
python3 main.py -j ps3:1 -p 2 -s snes -o $OUTPUT_PATH/snes_p2.cfg

# PC Engine
python3 main.py -j xbox360:0 -p 1 -s pce -o $OUTPUT_PATH/pce_p1.cfg
python3 main.py -j xbox360:1 -p 2 -s pce -o $OUTPUT_PATH/pce_p2.cfg
python3 main.py -j ps3:0 -p 1 -s pce -o $OUTPUT_PATH/pce_p1.cfg
python3 main.py -j ps3:1 -p 2 -s pce -o $OUTPUT_PATH/pce_p2.cfg

# Nintendo 64
python3 main.py -j n64:0 -p 1 -s n64 -o $OUTPUT_PATH/n64_p1.cfg
python3 main.py -j n64:1 -p 2 -s n64 -o $OUTPUT_PATH/n64_p2.cfg

# Nintendo Entertainment System
python3 main.py -j xbox360:0 -p 1 -s nes -o $OUTPUT_PATH/nes_p1.cfg
python3 main.py -j xbox360:1 -p 2 -s nes -o $OUTPUT_PATH/nes_p2.cfg
python3 main.py -j ps3:0 -p 1 -s nes -o $OUTPUT_PATH/nes_p1.cfg
python3 main.py -j ps3:1 -p 2 -s nes -o $OUTPUT_PATH/nes_p2.cfg
