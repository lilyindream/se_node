from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from src.library.pdata import pdata
from src.library.register import register
from src.library.loginout import login,logout
from src.library.post import post
from src.library.capturing import caturing
from src.library.asserting import asserting,assertin

class TestCnode(unittest.TestCase):
    """测试Cnode网页"""
    #定义类变量datas
    datas=pdata.datas

    @classmethod
    def setUpClass(self):
        """启动浏览器"""
        # print("*"*10+'Test Cases Set executing...'+"*"*10+'\n')
        self.dr = webdriver.Chrome(executable_path=pdata.rootpath + '/chromedriver.exe')
        time.sleep(5)


    @classmethod
    def tearDownClass(self):
        """退出浏览器"""
        self.dr.quit()
        # print("*"*10+'Test Cases Execution End'+"*"*10)


    def setUp(self):
        """导航到cnode首页"""
        # print("*"*5+'Test Case start'+"*"*5)
        self.dr.get(pdata.url)


    def tearDown(self):
        # print("*"*5+'Test Case end'+"*"*10)
        pass

    # @unittest.skip('直接跳过测试')
    def test_01register(self):
        """正常和异常注册测试,Case 1 to 6"""
        #点击注册按钮
        self.dr.find_element_by_link_text('注册').click()
        time.sleep(5)

        #执行csv测试数据中的前六条测试用例
        for data in self.datas[:6]:
            print()
            #调用注册函数
            message=register(self.dr,data[0],data[1],data[2],data[3])
            #调用截图函数
            caturing(self.dr,data[5])
            #调用
            asserting(self,message,data[6],data[4])
            self.dr.back()
            self.dr.refresh()

    # @unittest.skip('直接跳过测试')
    def test_02exlogin(self):
        """异常登陆测试,Case 7 to 8"""
        #点击登录按钮
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[6]/a').click()
        time.sleep(5)
        for data in self.datas[6:8]:
            message=login(self.dr,data[0],data[1])
            caturing(self.dr,data[5])
            asserting(self,message,data[6],data[4])
            self.dr.back()
            self.dr.refresh()

    # @unittest.skip('直接跳过测试')
    def test_03loginout(self):
        """正常登陆和退出测试,Case 9"""
        # 点击登录按钮
        self.dr.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[6]/a').click()
        time.sleep(5)
        for data in self.datas[8:9]:
            message=login(self.dr,data[0],data[1])
            caturing(self.dr,data[5])
            asserting(self, message, data[6], data[4])
            self.dr.back()
            self.dr.refresh()
        #点击退出按钮
        logout(self.dr)


    def test_04post(self):
         """正常发帖测试,Case10"""
         # 点击登录按钮并输入用户信息登录
         self.dr.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[6]/a').click()
         time.sleep(5)
         for data in self.datas[8:9]:
             message = login(self.dr, data[0], data[1])
         time.sleep(5)
         #发布帖子
         for data in self.datas[9:]:
            message=post(self.dr,data[0],data[1])
            caturing(self.dr, data[5])
            assertin(self, message, data[6], data[4])



if __name__=='__main__':
    # unittest.main
    testunit = unittest.TestSuite()
    testunit.addTest(TestCnode("test_01register"))
    testunit.addTest(TestCnode("test_02exlogin"))
    testunit.addTest(TestCnode("test_03loginout"))
    testunit.addTest(TestCnode("test_04post"))


    #调用报告存放reportpath
    fp=open(pdata.reportpath, 'wb')
    #定义测试报告
    runner=HTMLTestRunner(stream=fp,
                          title='CNODE测试报告',
                          description='用例执行情况：')

    runner.run(testunit)   #运行测试用例
    fp.close()