import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', '../Report/xml/' '.'])
#     allure generate ./Report/xml/ -o ./Report/html/ --clean
