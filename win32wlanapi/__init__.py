__title__ = 'win32wlanapi'
__version__ = '0.0.1'
__build__ = None
__author__ = 'György Nádudvari'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017 György Nádudvari'

def get_title():
    return __title__


import ctypes

from ctypes import byref
from ctypes import pointer

from ctypes import Structure

from ctypes import FormatError

from ctypes import c_uint
from ctypes import c_void_p
from ctypes import POINTER

from ctypes.wintypes import DWORD
from ctypes.wintypes import HANDLE
from ctypes.wintypes import WCHAR


from .guiddef import GUID
from .winerror import ERROR_SUCCESS


wlanapi = ctypes.windll.wlanapi


"""
The WLAN_INTERFACE_STATE enumerated type indicates the state of an interface.

typedef enum _WLAN_INTERFACE_STATE {
  wlan_interface_state_not_ready              = 0,
  wlan_interface_state_connected              = 1,
  wlan_interface_state_ad_hoc_network_formed  = 2,
  wlan_interface_state_disconnecting          = 3,
  wlan_interface_state_disconnected           = 4,
  wlan_interface_state_associating            = 5,
  wlan_interface_state_discovering            = 6,
  wlan_interface_state_authenticating         = 7
} WLAN_INTERFACE_STATE, *PWLAN_INTERFACE_STATE;

More info: https://msdn.microsoft.com/en-us/library/windows/desktop/ms706877(v=vs.85).aspx
"""
WLAN_INTERFACE_STATE = c_uint
WLAN_INTERFACE_STATE_DICT = {
    0: 'wlan_interface_state_not_ready',
    1: 'wlan_interface_state_connected',
    2: 'wlan_interface_state_ad_hoc_network_formed',
    3: 'wlan_interface_state_disconnecting',
    4: 'wlan_interface_state_disconnected',
    5: 'wlan_interface_state_associating',
    6: 'wlan_interface_state_discovering',
    7: 'wlan_interface_state_authenticating'
}


class WLAN_INTERFACE_INFO(Structure):
    """
    The WLAN_INTERFACE_INFO structure contains information about a wireless LAN interface.

    typedef struct _WLAN_INTERFACE_INFO {
        GUID                 InterfaceGuid;
        WCHAR                strInterfaceDescription[256];
        WLAN_INTERFACE_STATE isState;
    } WLAN_INTERFACE_INFO, *PWLAN_INTERFACE_INFO;

    More info: https://msdn.microsoft.com/en-us/library/windows/desktop/ms706868(v=vs.85).aspx
    """
    _fields_ = [
        ("InterfaceGuid", GUID),
        ("strInterfaceDescription", WCHAR * 256),  # ctypes.c_wchar
        ("isState", WLAN_INTERFACE_STATE)
    ]


class WLAN_INTERFACE_INFO_LIST(Structure):
    """
    The WLAN_INTERFACE_INFO_LIST structure contains an array of NIC interface information.

    typedef struct _WLAN_INTERFACE_INFO_LIST {
        DWORD               dwNumberOfItems;
        DWORD               dwIndex;
        WLAN_INTERFACE_INFO InterfaceInfo[];
    } WLAN_INTERFACE_INFO_LIST, *PWLAN_INTERFACE_INFO_LIST;

    More info: https://msdn.microsoft.com/en-us/library/windows/desktop/ms706873(v=vs.85).aspx
    """
    _fields_ = [
        ("dwNumberOfItems", DWORD),
        ("dwIndex", DWORD),
        ("InterfaceInfo", WLAN_INTERFACE_INFO * 16)
    ]


def WlanOpenHandle():
    """
    The WlanOpenHandle function opens a connection to the server.

    DWORD WINAPI WlanOpenHandle(
        _In_       DWORD   dwClientVersion,
        _Reserved_ PVOID   pReserved,
        _Out_      PDWORD  pdwNegotiatedVersion,
        _Out_      PHANDLE phClientHandle
    );

    More info: https://msdn.microsoft.com/en-us/library/windows/desktop/ms706759(v=vs.85).aspx
    """
    function_ref = wlanapi.WlanOpenHandle
    function_ref.argtypes = [DWORD, c_void_p, POINTER(DWORD), POINTER(HANDLE)]
    function_ref.restype = DWORD

    dwClientVersion = DWORD(2)
    pReserved = None
    dwNegotiatedVersion = DWORD()
    hClientHandle = HANDLE()

    result = wlanapi.WlanOpenHandle(dwClientVersion, pReserved, byref(dwNegotiatedVersion), byref(hClientHandle))

    if result != ERROR_SUCCESS:
        raise Exception(FormatError(result))

    return hClientHandle


def WlanCloseHandle(client_handle):
    """
    The WlanCloseHandle function closes a connection to the server.

    DWORD WINAPI WlanCloseHandle(
        _In_       HANDLE hClientHandle,
        _Reserved_ PVOID  pReserved
    );

    More info: https://msdn.microsoft.com/en-us/library/windows/desktop/ms706610(v=vs.85).aspx

    :param client_handle:
    :return:
    """

    function_ref = wlanapi.WlanCloseHandle
    function_ref.argtypes = [HANDLE, c_void_p]
    function_ref.restype = DWORD

    hClientHandle = client_handle

    result = wlanapi.WlanCloseHandle(hClientHandle, None)

    if result != ERROR_SUCCESS:
        raise Exception(FormatError(result))


def WlanEnumInterfaces(client_handle):
    """
    The WlanEnumInterfaces function enumerates all of the wireless LAN interfaces currently enabled on the local
    computer.

    DWORD WINAPI WlanEnumInterfaces(
        _In_       HANDLE                    hClientHandle,
        _Reserved_ PVOID                     pReserved,
        _Out_      PWLAN_INTERFACE_INFO_LIST *ppInterfaceList
    );

    More info: https://msdn.microsoft.com/en-us/library/windows/desktop/ms706716(v=vs.85).aspx

    :return:
    """

    function_ref = wlanapi.WlanEnumInterfaces
    function_ref.argtypes = [HANDLE, c_void_p, POINTER(POINTER(WLAN_INTERFACE_INFO_LIST))]
    function_ref.restype = DWORD

    hClientHandle = client_handle
    pInterfaceList = pointer(WLAN_INTERFACE_INFO_LIST())

    result = function_ref(hClientHandle, None, byref(pInterfaceList))

    if result != ERROR_SUCCESS:
        raise Exception(FormatError(result))

    interfaces = (pInterfaceList.contents.InterfaceInfo._type_ * pInterfaceList.contents.dwNumberOfItems).from_address(
        ctypes.addressof(pInterfaceList.contents.InterfaceInfo))

    interface_list = []

    for interface in interfaces:
        interface_dict = {
            'InterfaceGuid': str(interface.InterfaceGuid),
            'strInterfaceDescription': interface.strInterfaceDescription,
            'isState': WLAN_INTERFACE_STATE_DICT[interface.isState]
        }

        interface_list.append(interface_dict)

    return interface_list