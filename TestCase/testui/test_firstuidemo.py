#! /usr/bin/env python
# -*- coding: utf-8 -*-
import allure
from selenium import webdriver
import time
import os



from Common.Assert import Assertion
from Common.baseui import baseUI


# class TestFirstUIDemo:
#     def tttttest_demo1(self,driver):
#         time.sleep(2)
#         #打开网址
#         driver.get("http://192.168.60.132/#/login")
#         #输入用户名
#         #通过xpath定位元素
#         username = driver.find_element_by_xpath("//input[@name='username']")
#         username.clear()
#         username.send_keys("admin")
#         time.sleep(2)
#         #数据密码
#         password = driver.find_element_by_xpath('//input[@name="password"]')
#         password.clear()
#         password.send_keys("123456")
#         time.sleep(2)
#         #点击登录
#         login = driver.find_element_by_xpath("(//span[contains(text(),'登录')])[1]")
#         login.click()
#         time.sleep(2)
#
#         #断言
#
#         Assertion.assert_in_text(driver.page_source,'首页')
#
#
#
#         #点击营销
#         yingxiao = driver.find_element_by_xpath("//span[contains(text(),'营销')]")
#         yingxiao.click()
#         time.sleep(2)
#
#         #点击优惠券列表
#         youhuiquanliebiao = driver.find_element_by_xpath("//span[contains(text(),'优惠券列表')]")
#         youhuiquanliebiao.click()
#         time.sleep(2)
#         #输入优惠券名称
#         youhuiquanmingcheng = driver.find_element_by_xpath("//input[@placeholder='优惠券名称']")
#         youhuiquanmingcheng.clear()
#         youhuiquanmingcheng.send_keys("小米手机专用券")
#         time.sleep(2)
#         #点击查询搜索
#         chaxunsousuo  = driver.find_element_by_xpath('//span[contains(text(),"查询搜索")]')
#         chaxunsousuo.click()
#         time.sleep(2)
class TestFirstUIDemo:
 def test_demo2(self,driver):
        base = baseUI(driver)
        # 输入网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        base.send_keys('输入用户名', '//input[@name="username"]', 'admin')
        # 密码
        base.send_keys('密码', '//input[@name="password"]', '123456')
        # 点击登录
        base.click('点击登录', "//span[contains(text(),'登录')]")
        # 点击商品
        base.click('点击商品', "//span[contains(text(),'商品')]")
        # 点击添加商品
        base.click('点击添加商品', '//span[contains(text(), "添加商品")]')
        # 商品分类
        base.click('商品分类', "//label[contains(text(),'商品分类')]/following-sibling::div/span")
        # 手机数码
        base.click('手机数码', "//li[contains(text(),'手机数码')]")
        # 智能设备
        base.click('智能设备', "//li[contains(text(),'智能设备')]")
        # 商品名称
        base.send_keys('商品名称', "//label[contains(text(),'商品名称')]/following-sibling::div//input", '我有98k')
        # 副标题
        base.send_keys('副标题', "//label[contains(text(),'副标题')]/following-sibling::div//input", '大哥别杀我')
        # 商品品牌
        base.click('商品品牌', "//label[contains(text(),'商品品牌')]/following-sibling::div//input")
        # 点击苹果
        base.click('点击苹果', "//span[contains(text(),'苹果')]")
        # 滚动窗口
        base.scroll_screen("滚动窗口")
        # 点击下一步
        base.click("击下一步", "//span[text()='下一步，填写商品促销']")
        # 点击下一步
        base.click("点击下一步", "//span[text()='下一步，填写商品属性']")
        # 上传商品图片
        # base.send_keys("上传商品图片","//input[@name='file']/parent::*","‪D:\\1.png")
        # 切换iframe
        base.switch_to_frame("切换到iframe", "(//iframe[contains(@id,'vue-tinymce-')])[1]")
        # 填写规格参数
        base.send_keys("填写规格参数", "//body[@id='tinymce']", "我要AWM")
        driver.switch_to.default_content()
        # 点击下一步
        base.click("点击下一步", "//span[contains(text(),'下一步，选择商品关联')]")
        time.sleep(2)
        # # 输入专题名称搜索(//input[@placeholder="请输入专题名称"])[1]
        # base.send_keys("输入专题名称搜索", "(//input[@placeholder=请输入专题名称])[1]", "健康")
        # # 勾选待选择(//span[contains(text(),'待选择')])[1]
        # base.click("勾选待选择","(//span[contains(text(),'待选择')])[1]")
        # #点击右键按钮//button[@class="el-button el-button--primary el-button--small el-transfer__button"]
        # base.click("点击右键按钮","//button[@class=el-button el-button--primary el-button--small el-transfer__button]")
        # # 点击已选择(//span[contains(text(),'已选择')])[1]
        # base.click("点击已选择","(//span[contains(text(),'已选择')])[1]")
        # # 输入专题名称搜索(//input[@placeholder="请输入专题名称"])[2]
        # base.send_keys ("输入专题名称搜索","(//input[@placeholder=请输入专题名称])[2]","健康")





class TestFirstUIDemo:
 def test_demo3(self,driver):
        base = baseUI(driver)
        # 输入网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        base.send_keys('输入用户名', '//input[@name="username"]', 'admin')
        # 密码
        base.send_keys('密码', '//input[@name="password"]', '123456')
        # 点击登录
        base.click('点击登录', "//span[contains(text(),'登录')]")
        # 点击营销
        base.click('点击营销', "//span[contains(text(),'营销')]")
        # 点击优惠券列表
        base.click ("点击优惠券列表","//span[contains(text(),'优惠券列表')]")
        # 点击第一条的编辑
        base.click("点击第一条的编辑","//span[contains(text(),'编辑')][1]")
        # 点击优惠券类型：//label[contains(text(),'优惠券类型')]/following-sibling::div//input
        base.click("点击优惠券类型","//label[contains(text(),'优惠券类型')]/following-sibling::div//input")
        # 点击会员赠送 // span[text() = '会员赠券']
        base.click("点击会员赠送", "// span[text() = '会员赠券']")
        # 优惠券名称：(//input[@type="text"])[2]
        base.send_keys("优惠券名称", "(//input[@type='text'])[2]", "九亿少女的梦")
        # 点击适用平台：//label[contains(text(),'适用平台')]/following-sibling::div//input
        base.click("点击适用平台", "//label[contains(text(),'适用平台')]/following-sibling::div//input")
        # 点击pc平台 // span[text() = 'PC平台']
        base.click("点击pc平台", "// span[text() = 'PC平台']")
        # 总发行量：//label[contains(text(),'总发行量')]/following-sibling::div//input
        base.send_keys("总发行量", "//label[contains(text(),'总发行量')]/following-sibling::div//input", "999999")
        # 面额：//label[contains(text(),'面额')]/following-sibling::div//input
        base.send_keys("面额", "//label[contains(text(),'面额')]/following-sibling::div//input", "99999999")
        #  每人限领：//label[contains(text(),'每人限领')]/following-sibling::div//input
        base.send_keys("每人限领", "//label[contains(text(),'每人限领')]/following-sibling::div//input", "1")
        # 使用门槛：//label[contains(text(),'使用门槛')]/following-sibling::div//input
        base.send_keys("使用门槛", "//label[contains(text(),'使用门槛')]/following-sibling::div//input","110")
        # 有效期：
        # 点击可使用商品：//span[contains(text(),'指定商品')]
        base.click("点击可使用商品", "//span[contains(text(),'指定商品')]")
        # 备注输入
        base.send_keys("备注输入","//textarea[@rows=5]","我有98k")
        # 点击提交
        base.click("点击提交","//span[text()='提交']")
        # 点击确定
        base.click("点击确定","//span[contains(text(),'确定')]")
        # 断言
        print(driver.page_source)
        text = base.get_text("获取页面展示文本", "//div[@role='alert']/p")
        Assertion.assert_in_text('text','修改成功')
        # print(text)
        time.sleep(4)





class TestFirstUIDemo:
 def test_demo4(self,driver):
        base = baseUI(driver)
        # 输入网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        base.send_keys('输入用户名', '//input[@name="username"]', 'admin')
        # 密码
        base.send_keys('密码', '//input[@name="password"]', '123456')
        # 点击登录
        base.click('点击登录', "//span[contains(text(),'登录')]")
        # 点击订单(//span[contains(text(),'订单')])[1]
        base.click("点击订单","(//span[contains(text(),'订单')])[1]")
        # 点击订单列表//span[contains(text(),'订单列表')]
        base.click("点击订单列表", "//span[contains(text(),'订单列表')]")
        # 点击订单状态//label[contains(text(),'订单状态')]/following-sibling::div//input
        base.click("点击订单状态", "//label[contains(text(),'订单状态')]/following-sibling::div//input")
        # 点击待发货//span[contains(text(),'待发货')]
        base.click("点击待发货", "//span[contains(text(),'待发货')]")
        # 滚动屏幕
        base.scroll_screen("滚动屏幕")
        # 点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("点击查询搜索", "//span[contains(text(),'查询搜索')]")
        # 点击第一条的订单发货(//span[text()='订单发货'])[1]
        base.click("点击第一条的订单发货", "(//span[text()='订单发货'])[1]")
        # 点击选择物流公司//input[@placeholder="请选择物流公司"]
        base.click("点击选择物流公司","//input[@placeholder='请选择物流公司']")
        # 点击顺丰快递//span[text()='顺丰快递']
        base.click("点击顺丰快递","//span[text()='顺丰快递']")
        # 点击确定//span[text()='确定']
        base.click("点击确定","//span[text()='确定']")
        # 点击确定提交(//span[contains(text(),'确定')])[2]
        base.click("点击确定提交","(//span[contains(text(),'确定')])[2]")

