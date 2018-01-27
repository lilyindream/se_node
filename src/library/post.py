import  time
from src.library.pdata import pdata
def post(dr,title,content):
    """正常发帖"""
    c_publish = '发布话题'
    c_ban='//*[@id="tab-value"]/option[2]'
    c_title = '#title'
    c_content = '//*[@id="create_topic_form"]/fieldset/div/div/div[1]/a[4]'
    c_cli = '//*[@id="create_topic_form"]/fieldset/div/div/div[4]/input'


    #点击发布话题
    dr.find_element_by_link_text(c_publish).click()
    time.sleep(5)

    #选择版块，标题和内容,并点击提交
    #内容输入定位没有实现
    dr.find_element_by_xpath(c_ban).click()
    dr.find_element_by_css_selector(c_title).send_keys(pdata.ntime+title)
    dr.find_element_by_xpath(c_content).click()
    dr.find_element_by_xpath(c_cli).click()
    #返回标题
    return pdata.ntime+dr.title
