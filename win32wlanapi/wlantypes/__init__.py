from ctypes import Structure

from ctypes.wintypes import CHAR
from ctypes.wintypes import UINT
from ctypes.wintypes import ULONG

DOT11_SSID_MAX_LENGTH = 32

"""
The DOT11_BSS_TYPE enumerated type defines a basic service set (BSS) network type.

typedef enum _DOT11_BSS_TYPE {
    dot11_BSS_type_infrastructure  = 1,
    dot11_BSS_type_independent     = 2,
    dot11_BSS_type_any             = 3
} DOT11_BSS_TYPE, *PDOT11_BSS_TYPE;

More info: https://msdn.microsoft.com/en-us/library/windows/desktop/ms706001(v=vs.85).aspx
"""
DOT11_BSS_TYPE = UINT
DOT11_BSS_TYPE_DICT = {
    0: 'dot11_BSS_type_infrastructure',
    1: 'dot11_BSS_type_independent',
    2: 'dot11_BSS_type_any'
}

"""
The DOT11_PHY_TYPE enumeration defines an 802.11 PHY and media type.

typedef enum _DOT11_PHY_TYPE {
    dot11_phy_type_unknown     = 0,
    dot11_phy_type_any         = 0,
    dot11_phy_type_fhss        = 1,
    dot11_phy_type_dsss        = 2,
    dot11_phy_type_irbaseband  = 3,
    dot11_phy_type_ofdm        = 4,
    dot11_phy_type_hrdsss      = 5,
    dot11_phy_type_erp         = 6,
    dot11_phy_type_ht          = 7,
    dot11_phy_type_vht         = 8,
    dot11_phy_type_IHV_start   = 0x80000000,
    dot11_phy_type_IHV_end     = 0xffffffff
} DOT11_PHY_TYPE, *PDOT11_PHY_TYPE;

More info: https://msdn.microsoft.com/en-us/library/windows/desktop/ms706015(v=vs.85).aspx
"""
DOT11_PHY_TYPE = UINT
DOT11_PHY_TYPE_DICT = {
    0: 'dot11_phy_type_unknown',
    1: 'dot11_phy_type_fhss'
    # TODO: Continue...
}


"""
A percentage value that represents the signal quality of the network. WLAN_SIGNAL_QUALITY is of type ULONG. This member
contains a value between 0 and 100. A value of 0 implies an actual RSSI signal strength of -100 dbm. A value of 100
implies an actual RSSI signal strength of -50 dbm. You can calculate the RSSI signal strength value for
wlanSignalQuality values between 1 and 99 using linear interpolation.
"""
WLAN_SIGNAL_QUALITY = ULONG

"""
The DOT11_AUTH_ALGORITHM enumerated type defines a wireless LAN authentication algorithm.

typedef enum _DOT11_AUTH_ALGORITHM {
    DOT11_AUTH_ALGO_80211_OPEN        = 1,
    DOT11_AUTH_ALGO_80211_SHARED_KEY  = 2,
    DOT11_AUTH_ALGO_WPA               = 3,
    DOT11_AUTH_ALGO_WPA_PSK           = 4,
    DOT11_AUTH_ALGO_WPA_NONE          = 5,
    DOT11_AUTH_ALGO_RSNA              = 6,
    DOT11_AUTH_ALGO_RSNA_PSK          = 7,
    DOT11_AUTH_ALGO_IHV_START         = 0x80000000,
    DOT11_AUTH_ALGO_IHV_END           = 0xffffffff
} DOT11_AUTH_ALGORITHM, *PDOT11_AUTH_ALGORITHM;

More info: https://msdn.microsoft.com/en-us/library/windows/desktop/ms705989(v=vs.85).aspx
"""
DOT11_AUTH_ALGORITHM = UINT
DOT11_AUTH_ALGORITHM_DICT = {
    1: 'DOT11_AUTH_ALGO_80211_OPEN',
    2: 'DOT11_AUTH_ALGO_80211_SHARED_KEY'
    # TODO: Continue...
}


"""
The DOT11_CIPHER_ALGORITHM enumerated type defines a cipher algorithm for data encryption and decryption.

typedef enum _DOT11_CIPHER_ALGORITHM {
    DOT11_CIPHER_ALGO_NONE           = 0x00,
    DOT11_CIPHER_ALGO_WEP40          = 0x01,
    DOT11_CIPHER_ALGO_TKIP           = 0x02,
    DOT11_CIPHER_ALGO_CCMP           = 0x04,
    DOT11_CIPHER_ALGO_WEP104         = 0x05,
    DOT11_CIPHER_ALGO_WPA_USE_GROUP  = 0x100,
    DOT11_CIPHER_ALGO_RSN_USE_GROUP  = 0x100,
    DOT11_CIPHER_ALGO_WEP            = 0x101,
    DOT11_CIPHER_ALGO_IHV_START      = 0x80000000,
    DOT11_CIPHER_ALGO_IHV_END        = 0xffffffff
} DOT11_CIPHER_ALGORITHM, *PDOT11_CIPHER_ALGORITHM;

More info: https://msdn.microsoft.com/en-us/library/windows/desktop/ms706003(v=vs.85).aspx
"""
DOT11_CIPHER_ALGORITHM = UINT
DOT11_CIPHER_ALGORITHM_DICT = {
    0x00: 'DOT11_CIPHER_ALGO_NONE',
    0x01: 'DOT11_CIPHER_ALGO_WEP40'
    # TODO: Continue...
}

class DOT11_SSID(Structure):
    """
    A DOT11_SSID structure contains the SSID of an interface.

    typedef struct _DOT11_SSID {
        ULONG uSSIDLength;
        UCHAR ucSSID[DOT11_SSID_MAX_LENGTH];
    } DOT11_SSID, *PDOT11_SSID;

    More info: https://msdn.microsoft.com/en-us/library/windows/desktop/ms706034(v=vs.85).aspx
    """
    _fields_ = [
        ("uSSIDLength", ULONG),
        ("ucSSID", CHAR * DOT11_SSID_MAX_LENGTH)
    ]