import os

def get_root_path():
    """获得项目根路径"""
    rootpath = os.path.dirname(os.path.abspath(__file__))
    while rootpath:
        if os.path.exists(os.path.join(rootpath, 'readme.md')):
            break

        rootpath = rootpath[0:rootpath.rfind(os.path.sep)]

    return rootpath


#
# def get_father_path():
#      fatherpath=os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
#      return fatherpath






