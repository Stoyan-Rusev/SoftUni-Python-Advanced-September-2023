class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError (Exception):
    pass


MIN_NAME_LENGTH = 5
VALID_DOMAINS = ('.com', '.bg', '.org', '.net')
email = input()
while email != 'End':
    # Checking for '@' symbol:
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    # Checking name length:
    name = email.split('@')[0]
    if len(name) < MIN_NAME_LENGTH:
        raise NameTooShortError('Name must be more than 4 characters')

    # Checking if domain is valid:
    domain =  '.' + email.split('.')[-1]
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')
    email = input()
