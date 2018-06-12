# encoding: utf-8
"""
fragment.py

Created by Thomas Mangin on 2010-02-04.
Copyright (c) 2009-2015 Exa Networks. All rights reserved.
"""

from exabgp.protocol.enum import Enum


# =================================================================== Fragment

# Uses bitmask operand format defined above.
#   0   1   2   3   4   5   6   7
# +---+---+---+---+---+---+---+---+
# |   Reserved    |LF |FF |IsF|DF |
# +---+---+---+---+---+---+---+---+
#
# Bitmask values:
# +  Bit 7 - Don't fragment (DF)
# +  Bit 6 - Is a fragment (IsF)
# +  Bit 5 - First fragment (FF)
# +  Bit 4 - Last fragment (LF)

class Fragment(Enum):
    NOT = 0x00
    DONT = 0x01
    IS = 0x02
    FIRST = 0x04
    LAST = 0x08


# reserved = 0xF0


Fragment.UNKNOWN = 'unknown fragment value %s'

Fragment.VALUE = {
    'not-a-fragment': Fragment(Fragment.NOT),
    'dont-fragment': Fragment(Fragment.DONT),
    'is-fragment': Fragment(Fragment.IS),
    'first-fragment': Fragment(Fragment.FIRST),
    'last-fragment': Fragment(Fragment.LAST),
    '0x00': Fragment(0x00),
    '0x01': Fragment(0x01),
    '0x02': Fragment(0x02),
    '0x03': Fragment(0x03),
    '0x04': Fragment(0x04),
    '0x05': Fragment(0x05),
    '0x06': Fragment(0x06),
    '0x07': Fragment(0x07),
    '0x08': Fragment(0x08),
    '0x09': Fragment(0x09),
    '0x0a': Fragment(0x0a),
    '0x0b': Fragment(0x0b),
    '0x0c': Fragment(0x0c),
    '0x0d': Fragment(0x0d),
    '0x0e': Fragment(0x0e),
    '0x0f': Fragment(0x0f),

}

Fragment.NAME = {
    Fragment(Fragment.NOT): 'not-a-fragment',
    Fragment(Fragment.DONT): 'dont-fragment',
    Fragment(Fragment.IS): 'is-fragment',
    Fragment(Fragment.FIRST): 'first-fragment',
    Fragment(Fragment.LAST): 'last-fragment',
    Fragment(0x00): '0x00',
    Fragment(0x01): '0x01',
    Fragment(0x02): '0x02',
    Fragment(0x03): '0x03',
    Fragment(0x04): '0x04',
    Fragment(0x05): '0x05',
    Fragment(0x06): '0x06',
    Fragment(0x07): '0x07',
    Fragment(0x08): '0x08',
    Fragment(0x09): '0x09',
    Fragment(0x0a): '0x0a',
    Fragment(0x0b): '0x0b',
    Fragment(0x0c): '0x0c',
    Fragment(0x0d): '0x0d',
    Fragment(0x0e): '0x0e',
    Fragment(0x0f): '0x0f',

}
