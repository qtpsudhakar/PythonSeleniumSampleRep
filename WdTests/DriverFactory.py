from selenium import webdriver  # import selenium


def getDriver(browsername):
    if browsername == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        return webdriver.Chrome(executable_path=r'C:\Users\envy\Desktop\PythonForTestersProject\BD\chromedriver.exe',options= options)
    elif browsername == 'firefox':
        return webdriver.Firefox(executable_path=r'C:\Users\envy\Desktop\PythonForTestersProject\BD\geckodriver.exe')
    elif browsername == 'edge':
        return webdriver.Edge(executable_path=r'C:\Users\envy\Desktop\PythonForTestersProject\BD\msedgedriver.exe')
    else:
        return webdriver.Chrome(executable_path=r'C:\Users\envy\Desktop\PythonForTestersProject\BD\chromedriver.exe')
