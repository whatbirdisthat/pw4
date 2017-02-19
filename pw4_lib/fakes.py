

class FakeGpg:
    def __init__(self):
        pass

    def GPG(self, **kwargs):
        pass

    def decrypt_file(self, the_file, passphrase):
        return FakeStatus(the_file, passphrase)


class FakeStatus:
    def __init__(self, file, passphrase):
        self.file = file
        self.passphrase = passphrase
        self.ok = False

