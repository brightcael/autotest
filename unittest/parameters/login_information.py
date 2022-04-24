###账户信息
class account_info:
    newtest = {
        'username': 'newtest',
        'pwd': 'newtest',
        'id': '0',
    }
    freetest = {
        'username': 'freetest',
        'pwd': 'freetest',
        'id': '1',
    }
    teacherAC = {
        'username': 'teacherAC',
        'pwd': '123456',
        'id': '1',
    }
'''例子
    template = {
        'username': '',      ###用户名
        'pwd': '',           ###密码
        'id': '',            ###账户权限，0：管理员；1：教师；2：学生
    }
'''

###网址信息，登录站点以及api的url
class url_info:
    ###服务api的url
    saas_front_url = ''
    saas_backend_url = ''
    saas_sso_url = ''
    saas_webide_url = ''
    saas_ldc_url = ''

    ###站点的url
    formal_website_url = 'http://linklab.tinylink.cn/'
    test_website_url = 'http://test.tinylink.cn/'
    chuzhou_website_url = 'https://chzu.tinylink.cn/'
    live_website_url = 'https://liveplatform.test.tinylink.cn/live'+'?experiment=smarthome'