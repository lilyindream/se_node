from src.library.pdata import pdata

def caturing(dr,screename):
    """#每次测试的页面截图存放到项目下的screenshot中"""
    dr.get_screenshot_as_file(pdata.rootpath + '/src/screenshots/' + pdata.ntime + screename + ".png")