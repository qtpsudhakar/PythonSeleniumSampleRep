class Google:
    def __init__(self):
        self.user = 'admin' # public variable everywhere
        self.__password ='asdf' # private variable Same class
        self._environment = 'test' # protected Same and sub classes
        print('constructor executed')
    def search(self):
        print('searching for keyword')
    def createnewbrand(self):
        print('brand Google created')
# Google is super/parent class
# Gmail is sub class

class ABCD:
    def __init__(self):
        self.user1 = 'guest'
        print('constructor executed from abcd')
    def createnewbrand(self):
        print('new brand ABCD created')

class Gmail(Google,ABCD): # multiple inheritance
    def __init__(self):
        Google.__init__(self)
        ABCD.__init__(self)
    def demo(self):
        print(self.user)
        print(self._environment)
    # class gmailsub:
    #     def dm(self):
    #         print('from inner')

g1 = Google()
print(g1.user)
print(g1._environment)
# print(hasattr(g1, '__password'))
gm = Gmail()
gm.search()
gm.createnewbrand()
# gm.gmailsub().dm()
print(gm.user1)