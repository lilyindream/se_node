import time
def register(dr,name,password,repwd,mail):
    """注册用户"""
    dr.find_element_by_link_text('注册').click()
    time.sleep(5)

    # 定位登录页面的元素
    cid_name = "loginname"
    cid_pwd = "pass"
    cid_rpd = "re_pass"
    cid_cmail = "email"
    ccname_cli = "span-primary"
    c_info = '//*[@id="content"]//strong'
    dr.find_element_by_id(cid_name).clear()
    dr.find_element_by_id(cid_name).send_keys(name)
    dr.find_element_by_id(cid_pwd).clear()
    dr.find_element_by_id(cid_pwd).send_keys(password)
    dr.find_element_by_id(cid_rpd).clear()
    dr.find_element_by_id(cid_rpd).send_keys(repwd)
    dr.find_element_by_id(cid_cmail).clear()
    dr.find_element_by_id(cid_cmail).send_keys(mail)
    dr.find_element_by_class_name(ccname_cli).click()
    time.sleep(5)
    #返回提示信息
    message = dr.find_element_by_xpath(c_info).text
    return message

