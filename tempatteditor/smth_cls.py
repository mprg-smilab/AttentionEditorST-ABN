#!/usr/bin/env python
# -*- coding: utf-8 -*-

# smth_cls.py
# Copyright (c) Tsubasa Hirakawa, 2021


CLASS_LABEL = {
    0: "Approaching [something] with your camera",
    1: "Attaching [something] to [something]",
    2: "Bending [something] so that it deforms",
    3: "Bending [something] until it breaks",
    4: "Burying [something] in [something]",
    5: "Closing [something]",
    6: "Covering [something] with [something]",
    7: "Digging [something] out of [something]",
    8: "Dropping [something] behind [something]",
    9: "Dropping [something] in front of [something]",
    10: "Dropping [something] into [something]",
    11: "Dropping [something] next to [something]",
    12: "Dropping [something] onto [something]",
    13: "Failing to put [something] into [something] because [something] does not fit",
    14: "Folding [something]",
    15: "Hitting [something] with [something]",
    16: "Holding [something]",
    17: "Holding [something] behind [something]",
    18: "Holding [something] in front of [something]",
    19: "Holding [something] next to [something]",
    20: "Holding [something] over [something]",
    21: "Laying [something] on the table on its side, not upright",
    22: "Letting [something] roll along a flat surface",
    23: "Letting [something] roll down a slanted surface",
    24: "Letting [something] roll up a slanted surface, so it rolls back down",
    25: "Lifting a surface with [something] on it but not enough for it to slide down",
    26: "Lifting a surface with [something] on it until it starts sliding down",
    27: "Lifting [something] up completely without letting it drop down",
    28: "Lifting [something] up completely, then letting it drop down",
    29: "Lifting [something] with [something] on it",
    30: "Lifting up one end of [something] without letting it drop down",
    31: "Lifting up one end of [something], then letting it drop down",
    32: "Moving away from [something] with your camera",
    33: "Moving [part] of [something]",
    34: "Moving [something] across a surface until it falls down",
    35: "Moving [something] across a surface without it falling down",
    36: "Moving [something] and [something] away from each other",
    37: "Moving [something] and [something] closer to each other",
    38: "Moving [something] and [something] so they collide with each other",
    39: "Moving [something] and [something] so they pass each other",
    40: "Moving [something] away from [something]",
    41: "Moving [something] away from the camera",
    42: "Moving [something] closer to [something]",
    43: "Moving [something] down",
    44: "Moving [something] towards the camera",
    45: "Moving [something] up",
    46: "Opening [something]",
    47: "Picking [something] up",
    48: "Piling [something] up",
    49: "Plugging [something] into [something]",
    50: "Plugging [something] into [something] but pulling it right out as you remove your hand",
    51: "Poking a hole into [some substance]",
    52: "Poking a hole into [something soft]",
    53: "Poking a stack of [something] so the stack collapses",
    54: "Poking a stack of [something] without the stack collapsing",
    55: "Poking [something] so it slightly moves",
    56: "Poking [something] so lightly that it doesn't or almost doesn't move",
    57: "Poking [something] so that it falls over",
    58: "Poking [something] so that it spins around",
    59: "Pouring [something] into [something]",
    60: "Pouring [something] into [something] until it overflows",
    61: "Pouring [something] onto [something]",
    62: "Pouring [something] out of [something]",
    63: "Pretending or failing to wipe [something] off of [something]",
    64: "Pretending or trying and failing to twist [something]",
    65: "Pretending to be tearing [something that is not tearable]",
    66: "Pretending to close [something] without actually closing it",
    67: "Pretending to open [something] without actually opening it",
    68: "Pretending to pick [something] up",
    69: "Pretending to poke [something]",
    70: "Pretending to pour [something] out of [something], but [something] is empty",
    71: "Pretending to put [something] behind [something]",
    72: "Pretending to put [something] into [something]",
    73: "Pretending to put [something] next to [something]",
    74: "Pretending to put [something] on a surface",
    75: "Pretending to put [something] onto [something]",
    76: "Pretending to put [something] underneath [something]",
    77: "Pretending to scoop [something] up with [something]",
    78: "Pretending to spread air onto [something]",
    79: "Pretending to sprinkle air onto [something]",
    80: "Pretending to squeeze [something]",
    81: "Pretending to take [something] from [somewhere]",
    82: "Pretending to take [something] out of [something]",
    83: "Pretending to throw [something]",
    84: "Pretending to turn [something] upside down",
    85: "Pulling [something] from behind of [something]",
    86: "Pulling [something] from left to right",
    87: "Pulling [something] from right to left",
    88: "Pulling [something] onto [something]",
    89: "Pulling [something] out of [something]",
    90: "Pulling two ends of [something] but nothing happens",
    91: "Pulling two ends of [something] so that it gets stretched",
    92: "Pulling two ends of [something] so that it separates into two pieces",
    93: "Pushing [something] from left to right",
    94: "Pushing [something] from right to left",
    95: "Pushing [something] off of [something]",
    96: "Pushing [something] onto [something]",
    97: "Pushing [something] so it spins",
    98: "Pushing [something] so that it almost falls off but doesn't",
    99: "Pushing [something] so that it falls off the table",
    100: "Pushing [something] so that it slightly moves",
    101: "Pushing [something] with [something]",
    102: "Putting [number of] [something] onto [something]",
    103: "Putting [something] and [something] on the table",
    104: "Putting [something] behind [something]",
    105: "Putting [something] in front of [something]",
    106: "Putting [something] into [something]",
    107: "Putting [something] next to [something]",
    108: "Putting [something] on a flat surface without letting it roll",
    109: "Putting [something] on a surface",
    110: "Putting [something] on the edge of [something] so it is not supported and falls down",
    111: "Putting [something] onto a slanted surface but it doesn't glide down",
    112: "Putting [something] onto [something]",
    113: "Putting [something] onto [something else that cannot support it] so it falls down",
    114: "Putting [something similar to other things that are already on the table]",
    115: "Putting [something] that can't roll onto a slanted surface, so it slides down",
    116: "Putting [something] that can't roll onto a slanted surface, so it stays where it is",
    117: "Putting [something that cannot actually stand upright] upright on the table, so it falls on its side",
    118: "Putting [something] underneath [something]",
    119: "Putting [something] upright on the table",
    120: "Putting [something], [something] and [something] on the table",
    121: "Removing [something], revealing [something] behind",
    122: "Rolling [something] on a flat surface",
    123: "Scooping [something] up with [something]",
    124: "Showing a photo of [something] to the camera",
    125: "Showing [something] behind [something]",
    126: "Showing [something] next to [something]",
    127: "Showing [something] on top of [something]",
    128: "Showing [something] to the camera",
    129: "Showing that [something] is empty",
    130: "Showing that [something] is inside [something]",
    131: "[Something] being deflected from [something]",
    132: "[Something] colliding with [something] and both are being deflected",
    133: "[Something] colliding with [something] and both come to a halt",
    134: "[Something] falling like a feather or paper",
    135: "[Something] falling like a rock",
    136: "Spilling [something] behind [something]",
    137: "Spilling [something] next to [something]",
    138: "Spilling [something] onto [something]",
    139: "Spinning [something] so it continues spinning",
    140: "Spinning [something] that quickly stops spinning",
    141: "Spreading [something] onto [something]",
    142: "Sprinkling [something] onto [something]",
    143: "Squeezing [something]",
    144: "Stacking [number of] [something]",
    145: "Stuffing [something] into [something]",
    146: "Taking [one of many similar things on the table]",
    147: "Taking [something] from [somewhere]",
    148: "Taking [something] out of [something]",
    149: "Tearing [something] into two pieces",
    150: "Tearing [something] just a little bit",
    151: "Throwing [something]",
    152: "Throwing [something] against [something]",
    153: "Throwing [something] in the air and catching it",
    154: "Throwing [something] in the air and letting it fall",
    155: "Throwing [something] onto a surface",
    156: "Tilting [something] with [something] on it slightly so it doesn't fall down",
    157: "Tilting [something] with [something] on it until it falls off",
    158: "Tipping [something] over",
    159: "Tipping [something] with [something in it] over, so [something in it] falls out",
    160: "Touching (without moving) [part] of [something]",
    161: "Trying but failing to attach [something] to [something] because it doesn't stick",
    162: "Trying to bend [something unbendable] so nothing happens",
    163: "Trying to pour [something] into [something], but missing so it spills next to it",
    164: "Turning [something] upside down",
    165: "Turning the camera downwards while filming [something]",
    166: "Turning the camera left while filming [something]",
    167: "Turning the camera right while filming [something]",
    168: "Turning the camera upwards while filming [something]",
    169: "Twisting (wringing) [something] wet until water comes out",
    170: "Twisting [something]",
    171: "Uncovering [something]",
    172: "Unfolding [something]",
    173: "Wiping [something] off of [something]"
}
