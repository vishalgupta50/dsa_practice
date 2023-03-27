# ipv4 address

def validate_ipv4_address(address):
    components = address.split('.')

    if len(components) > 4:
        return False
    for component in components:
        if not component.isdigit():
            return False
        value = int(component)
        if 0 > value > 255:
            return False
        if component[0] == '0' and len(component) > 1:
            return False
    return True


print(validate_ipv4_address("12.34.56.12"))






