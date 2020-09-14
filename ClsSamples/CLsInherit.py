class Google:
    def search(self):
        print('google search')
    @classmethod
    def open(cls):
        pass
class Gmail(Google):
    def searchKeyword(self):
        self.search()
        self.open()