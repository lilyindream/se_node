import csv

from   src.library.getRootPath  import get_root_path

def getDataFromCsv(file):
    """读取csv文件"""
    all_test_data = []
    filepath=get_root_path().replace('\\','/')
    basepath=filepath + file
    with open(basepath,'r',encoding='utf-8') as filedata:
        # print(filedata)
        filereader = csv.reader(filedata)
        # print(filereader)

        next(filereader)   # 去掉第一行列名数据
        for row in filereader:
            # print(row)
            all_test_data.append(row)

    return all_test_data


def getData():
    """读取项目中的csv文件"""
    file='/src/data/register_testdata.csv'
    datas=getDataFromCsv(file)
    return datas











