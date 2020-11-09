def check_pwd(password):
    if len(password) < 8:
        return False
    if len(password) > 20:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    spi_char = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=']
    if not any(char in spi_char for char in password):
        return False
    return True