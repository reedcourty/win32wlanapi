import pytest

import context
import win32wlanapi

def test_import_win32wlanapi_package():
    # Arrange

    # Act
    expected = 'win32wlanapi'
    actual = win32wlanapi.get_title()

    # Assert
    assert expected == actual


def test_WlanOpenHandle():
    # Arrange

    # Act
    expected = 1
    actual = win32wlanapi.WlanOpenHandle().value

    print(actual)

    # Assert
    assert expected == actual


def test_WlanCloseHandle_with_invalid_handle():
    # Arrange

    # Act
    with pytest.raises(Exception) as excinfo:
        win32wlanapi.WlanCloseHandle(2)

    # Assert
    assert 'A leíró érvénytelen.' in str(excinfo.value)


def test_WlanCloseHandle():
    # Arrange
    client_handle = win32wlanapi.WlanOpenHandle()

    # Act
    win32wlanapi.WlanCloseHandle(client_handle)

    # Assert
    assert True


def test_WlanEnumInterfaces():
    # Arrange
    import re
    import subprocess
    import sys

    guid_pattern = r'[abcdef0-9]{8}-[abcdef0-9]{4}-[abcdef0-9]{4}-[abcdef0-9]{4}-[abcdef0-9]{12}'
    p = re.compile(guid_pattern)

    client_handle = win32wlanapi.WlanOpenHandle()
    cp = subprocess.run('netsh wlan show interface', shell=True, stdout=subprocess.PIPE)
    guid = p.search(cp.stdout.decode('latin-1')).group()

    # Act
    expected = guid
    actual = win32wlanapi.WlanEnumInterfaces(client_handle)[0].get('InterfaceGuid')

    # Assert
    assert expected == actual
