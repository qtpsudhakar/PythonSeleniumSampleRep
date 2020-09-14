import pytest


class TestClass1:
    @pytest.mark.run(order=2)
    def test_one(self):
        print('test_one executed')

    @pytest.mark.run(order=3)
    def test_two(self):
        print('test_two executed')

    @pytest.mark.run(order=1)
    def test_four(self):
        print('test_four executed')

    @pytest.mark.run(order=1)
    def test_three(self):
        print('test_three executed')

