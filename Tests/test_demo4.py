import pytest

class Test_cls1():

    @pytest.mark.parametrize('x,y,z',[(10,2,11),(1,20,21)])
    def test_demoadd2(self,x,y,z):
        assert x+y==z


