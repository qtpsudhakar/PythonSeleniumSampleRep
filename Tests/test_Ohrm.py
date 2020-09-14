import pytest

@pytest.mark.usefixtures('setupOhrm','setupOhrmMethods')
class Test_cls1():

    def test_login(self):
        print('Logged in to application')

    def test_AddEmp(self):
        print('Employee Added')

    def test_Logout(self):
        print('Loggedout of application')


