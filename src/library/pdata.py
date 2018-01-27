from src.library.getRootPath import get_root_path
from src.library.getData import getData
import time
class pdata():
    """公共变量定义"""
    rootpath = get_root_path().replace('\\', '/')
    ntime = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    reportpath = get_root_path()+ '\\src\\report\\' + ntime + '_result.html'
    url = 'http://118.31.19.120:3000'
    datas = getData()