def asserting(self,message,predictinfo,casename):
    """assert是否实际提示和预期是否相等"""
    try:
        self.assertEqual(message, predictinfo)
        print(casename+'：Test Pass:页面提示信息和预期一致.')
        # print('预期提示:',data[6])
        # print('实际提示:', message)
    except Exception as e:
        print('页面提示信息和预期不一致:fail')
        # print('预期提示:',data[6])
        # print('实际提示:', message)
        raise AssertionError(casename+':Test Fail:页面提示信息和预期不一致.', format(e))


def assertin(self,message,predictinfo,casename):
    """assert是否实际提示是否包含预期"""
    try:
        self.assertIn(predictinfo,message)
        # print('页面提示信息和预期一致: pass')
        # print('预期提示:',data[6])
        # print('实际提示:', message)
    except Exception as e:
        # print('页面提示信息和预期不一致:fail')
        # print('预期提示:',data[6])
        # print('实际提示:', message)
        raise AssertionError(casename+':Test Fail:页面提示信息和预期不一致.', format(e))