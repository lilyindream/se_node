import time


def login(dr,name,password):
    """登录"""
    cid_name = "name"
    cid_pwd = "pass"
    cclass_cli = 'span-primary'
    c_info='//*[@id="content"]//strong'
    c_info2='dark'
    dr.find_element_by_id(cid_name).clear()
    dr.find_element_by_id(cid_name).send_keys(name)
    dr.find_element_by_id(cid_pwd).clear()
    dr.find_element_by_id(cid_pwd).send_keys(password)
    dr.find_element_by_class_name(cclass_cli).click()
    time.sleep(5)
    #返回错误的提示信息或登录后的用户名信息
    try:
        message = dr.find_element_by_xpath(c_info).text
    except:
        message=dr.find_element_by_class_name(c_info2).text

    return message




def logout(dr):
    """退出"""
    c_back = '退出'
    dr.find_element_by_link_text(c_back).click()
    time.sleep(5)