import pytest


@pytest.fixture(scope='class')
def setupOhrm():
    print("Open Orange hrm application")
    yield
    print("Closed Application")

@pytest.fixture()
def setupOhrmMethods():
    print("Method Precodition")
    yield
    print("Method Post Condition")

@pytest.fixture()
def getdata():
    print("getting user data")
    return ["selenium", "webdriver"]

@pytest.fixture(params=['set1', 'set2'])
def paramdata(request):
    return request.param
