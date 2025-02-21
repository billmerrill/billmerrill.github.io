#!/usr/bin/env python
import sys

if len(sys.argv) == 1:
    exit()


prob = float(sys.argv[1]) / 100.0
flip = 1
coin_prob = .5
while coin_prob > prob:
    flip += 1
    coin_prob *= .5

disp_prob = str(round(coin_prob * 100, 3))

sys.stdout.write("The chance of flipping a coin the same way " + 
                str(flip) + " times in a row is " + disp_prob + "%.\n")
sys.exit(0)