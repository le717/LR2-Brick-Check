#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""LR2 Brick Check - Keeping your LR2 brick mods valid.

Created 2014 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""

from __future__ import print_function
import os
import sys

__all__ = ("main")


def main():
    """The entire application."""
    # We were not given enough arguments
    if len(sys.argv) != 2:
        print("\nUsage: {0} [Input file]".format(
              os.path.basename(sys.argv[0])))
        raise SystemExit(1)

    # Set up required items
    inFile = os.path.abspath(sys.argv[1]).upper()
    outFile = os.path.join(os.path.expanduser("~"), "My Documents",
                           "LR2-Brick-Check-{0}.log".format(
                           os.path.basename(inFile).rstrip(".TXT")))
    brickCount = 0
    doNotExist = []

    # The input file does not exist
    if not os.path.exists(inFile):
        print("\n{0} does not exist!".format(inFile))
        raise SystemExit(1)

    # Read the file
    with open(inFile, "rt") as f:
        lines = f.readlines()

    for line in lines:
        # Do not process comments or blank lines
        if not line.startswith("#") and line not in ("\r", "\n", "\r\n"):
            brickCount += 1

            # Extract only the file path to the model, removing unneeded path
            line = line[:line.find("MD2") + 3].split("\\")[3:]

            # Construct the path to the 3D model
            modelPath = os.path.join(os.path.dirname(inFile),
                                     os.path.sep.join(line))

            # The 3D model does exist, move along
            if os.path.isfile(modelPath):
                continue

            # Nope, it does not exist
            else:
                doNotExist.append(os.path.sep.join(line))

    # Report the number of bricks
    print("There are {0} bricks listed in {1}.\n".format(brickCount,
          os.path.basename(inFile)))

    # There is a hard limit of 512 bricks per file
    if brickCount > 512:
        print("""You have too many bricks!
The game will crash if you have more than 512 bricks!
""")

    # Some 3D models do not exist, report them
    if len(doNotExist) > 0:
        print("""Of the bricks listed, {0} do not exist.
A list has been saved to \n{1}\n"""
              .format(len(doNotExist), outFile))

        with open(outFile, "wt") as o:
            o.write("##########\n# {0}\n##########\n\n".format(inFile))

            # List all the parts
            for part in doNotExist:
                o.write("* {0}\n".format(part))

    # All models exist
    else:
        print("All {0} bricks exist.".format(brickCount))
    raise SystemExit(0)

if __name__ == "__main__":
    main()
