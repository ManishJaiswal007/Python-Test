import verify_password

def test_valid_password():
    pwd = "Rakaj123"
    check=verify_password.check_password(pwd)
    assert check == True

def test_special_symbol_password():
    pwd = "Rakaj@123"
    check=verify_password.check_password(pwd)
    assert check == False

def test_password_symbol_end():
    pwd = "Rakaj123@"
    check=verify_password.check_password(pwd)
    assert check == False

def test_password_numeric_start():
    pwd = "54Rakaj123"
    check=verify_password.check_password(pwd)
    assert check == False

def test_no_password():
    pwd = ""
    check=verify_password.check_password(pwd)
    assert check == False

def test_max_len_password():
    pwd = "Raga1279-ghdjasnhq3u097hvjal"
    check=verify_password.check_password(pwd)
    assert check == False

