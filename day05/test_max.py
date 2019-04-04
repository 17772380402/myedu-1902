import allure

@allure.feature("类上的装饰器")
class TestLee:
    @allure.story("max1方法上的")
    def test_Max1(self):
        assert 1<2


    @allure.story("max2方法上的")
    def test_Max2(self):
        assert 3>2


    @allure.story("max3方法上的")
    def test_Max3(self):
        assert 5<2
