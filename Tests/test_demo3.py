import pytest

class Test_cls1():

    @pytest.fixture()
    def test_p1(self):
        print('login')
        yield
        print('logout')

    def test_demoadd2(self,test_p1):
        print('demo add2 executed')


