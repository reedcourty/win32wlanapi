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
from ctypes import FormatError

from ctypes import c_void_p
from ctypes import POINTER

from ctypes.wintypes import DWORD
from ctypes.wintypes import HANDLE


from .winerror import ERROR_SUCCESS


wlanapi = ctypes.windll.wlanapi

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
