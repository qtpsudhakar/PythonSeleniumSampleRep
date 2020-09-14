class Gmail:
    def __init__(self,browser,uname,pwd):
        self.browser = browser
        self.username = uname
        self.password = pwd
    def openApplication(self):
        print(f'Application opened in {self.browser}')
    def login(self,env='test'):
        print(f'logged in to gmail using {self.username} and {self.password}')
gm =Gmail('chrome','admin','asdf')
gm1 =Gmail('firefox','admin','asdf')

gm.openApplication()
gm.login()

gm1.openApplication()
gm1.login()