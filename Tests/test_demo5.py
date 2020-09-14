import pytest

# @pytest.mark.usefixtures("getdata","paramdata")
class TestClass5:
    def test_t1(self,getdata):
        print("this is t1 demo")
        print(getdata[0])
        print(getdata[1])

    def test_t2(self,paramdata):
        print("this is t2 demo")
        print(paramdata)
