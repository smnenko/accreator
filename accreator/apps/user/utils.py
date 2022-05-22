class PasswordValidator:

    def __init__(self, password: str):
        self.password = password

        self.has_digit = False
        self.has_upper = False
        self.has_lower = False
        self.has_no_space = False
        self.has_special = False

    def is_valid(self):
        for i in self.password:
            if i.isdigit() and not self.has_digit:
                self.has_digit = True
            if i.isupper() and not self.has_upper:
                self.has_upper = True
            if i.islower() and not self.has_lower:
                self.has_lower = True
            if i.isascii() and (not i.isascii() and not i.isalpha()):
                self.has_special = True

        if ' ' not in self.password:
            self.has_no_space = True

        return (
            self.has_digit and
            self.has_upper and
            self.has_lower and
            self.has_special and
            self.has_no_space
        )

