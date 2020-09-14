import pytest

class Test_cls1():

    @pytest.mark.g1
    def test_demoadd1(self):
        print('first')

    @pytest.mark.skip(reason='not to test')
    def test_demoadd3(self):
        print('third')

    @pytest.mark.g1
    def test_demoadd2(self):
        print('second')


