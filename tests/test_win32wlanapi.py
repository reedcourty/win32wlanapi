def test_import_win32wlanapi_package():
    # Arrange
    import context
    import win32wlanapi

    # Act
    expected = 'win32wlanapi'
    actual = win32wlanapi.get_title()

    # Assert
    assert expected == actual
