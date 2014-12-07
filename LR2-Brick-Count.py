#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import os

inFile = "UNIQUEBRICKS.TXT"
doNotExist = []

with open(inFile, "rt") as f:
    lines = f.readlines()

brickCount = 0
for line in lines:

    # Do not process comments or blank lines
    if not line.startswith("#") and line not in ("\r", "\n", "\r\n"):
        brickCount += 1

        # Extract only the file path to the model, removing unneeded path
        line = line[:line.find("MD2") + 3].split("\\")[3:]

        # Construct the path to the 3D model
        modelPath = os.path.join(os.getcwd(), os.path.sep.join(line))

        # The 3D model does exist, move along
        if os.path.isfile(modelPath):
            continue

            # Nope, it does not exist
        else:
            doNotExist.append(os.path.sep.join(line))

# Report the number of bricks
print("There are {0} bricks listed in {1}.\n".format(brickCount,
      os.path.basename(inFile)))

# Some 3D models do not exist, report them
if len(doNotExist) > 0:
    print("Of the bricks listed, {0} do not exist. They are as follows:"
          .format(len(doNotExist)))

    for part in doNotExist:
        print("* {0}".format(part))

# All models exist
else:
    print("All {0} bricks exist.".format(brickCount))
