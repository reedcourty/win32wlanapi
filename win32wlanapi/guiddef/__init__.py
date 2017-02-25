from ctypes import Structure

from ctypes.wintypes import DWORD
from ctypes.wintypes import WORD
from ctypes.wintypes import BYTE

class GUID(Structure):
    """
    GUIDs identify objects such as interfaces, manager entry-point vectors (EPVs), and class objects. A GUID is a
    128-bit value consisting of one group of 8 hexadecimal digits, followed by three groups of 4 hexadecimal digits
    each, followed by one group of 12 hexadecimal digits. The following example GUID shows the groupings of hexadecimal
    digits in a GUID: 6B29FC40-CA47-1067-B31D-00DD010662DA

    The GUID structure stores a GUID.

    typedef struct _GUID {
        DWORD Data1;
        WORD  Data2;
        WORD  Data3;
        BYTE  Data4[8];
    } GUID;

    More info: https://msdn.microsoft.com/en-us/library/aa373931.aspx
    """
    _fields_ = [
        ("Data1", DWORD),      # ctypes.c_ulong
        ("Data2", WORD),       # ctypes.c_ushort
        ("Data3", WORD),       # ctypes.c_ushort
        ("Data4", BYTE * 8)    # ctypes.c_byte
    ]

    def __str__(self):
        return "{:08x}-{:04x}-{:04x}-{}-{}".format(self.Data1, self.Data2, self.Data3,
            ''.join(["{:02x}".format(256+d if d < 0 else d) for d in self.Data4[:2]]),
            ''.join(["{:02x}".format(256+d if d < 0 else d) for d in self.Data4[2:]]),
        )
