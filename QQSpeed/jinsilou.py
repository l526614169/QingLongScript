'''
new Env('掌上飞车-0点开30个金丝篓')
cron: 0 0 * * *
Author       : BNDou
Date         : 2022-12-28 23:58:11
LastEditTime : 2022-12-30 22:52:22
FilePath     : /Auto_Check_In/checkIn_ZhangFei_JinSiLou.py
Description  : 金丝篓开永久雷诺
添加环境变量COOKIE_ZHANGFEI、REFERER_ZHANGFEI，多账号用回车换行分开
值分别是cookie和referer
'''
from urllib.parse import unquote
import requests
import os
import sys
sys.path.append('.')
requests.packages.urllib3.disable_warnings()

# 测试用环境变量
os.environ['COOKIE_ZHANGFEI'] = 'access_token=3589300F3A3A168F8967E637BCA2ABE3; appOpenId=2CFA4BE9C08A7C8D813BF06D2BA09972; appOpenid=2CFA4BE9C08A7C8D813BF06D2BA09972; openId=2CFA4BE9C08A7C8D813BF06D2BA09972; openid=2CFA4BE9C08A7C8D813BF06D2BA09972; appid=1105330667; appId=1105330667; uin=o0948840188; accessToken=3589300F3A3A168F8967E637BCA2ABE3; acctype=qc; access_token=3589300F3A3A168F8967E637BCA2ABE3; appOpenId=2CFA4BE9C08A7C8D813BF06D2BA09972; appOpenid=2CFA4BE9C08A7C8D813BF06D2BA09972; openId=2CFA4BE9C08A7C8D813BF06D2BA09972; openid=2CFA4BE9C08A7C8D813BF06D2BA09972; appid=1105330667; appId=1105330667; uin=o0948840188; accessToken=3589300F3A3A168F8967E637BCA2ABE3; acctype=qc; 300969a6ff940bbdfd62ab232499eedd=1; access_token=3589300F3A3A168F8967E637BCA2ABE3; openid=2CFA4BE9C08A7C8D813BF06D2BA09972; appid=1105330667; acctype=qc; eas_sid=R1t6Z7J3p2e2y5D472c8X5g4m7'
os.environ['REFERER_ZHANGFEI'] = 'https://bang.qq.com/app/speed/treasure/index?toOpenid=&serverName=&toUin=948840188&cGameId=1003&serverId=0&gameName=QQ%E9%A3%9E%E8%BD%A6%E7%AB%AF%E6%B8%B8&areaName=%E7%94%B5%E4%BF%A1%E5%8C%BA&nickname=%E6%95%99%E4%B8%BB&uin=948840188&roleLevel=201&accType=qc&gameId=10013&roleId=948840188&uniqueRoleId=173393807&avatar=http%3A%2F%2Fq.qlogo.cn%2Fqqapp%2F1104466820%2F57637BA7E695AFC3692326569BE55ED5%2F100&accessToken=3589300F3A3A168F8967E637BCA2ABE3&userId=328733790&token=8bUWmBJm&isMainRole=1&subGameId=10013&appOpenid=2CFA4BE9C08A7C8D813BF06D2BA09972&areaId=1&roleJob=&appid=1105330667&roleName=My%E4%B8%A8%E7%81%ACDear%E4%B8%BF%E6%89%B6%E6%91%87&_isShare=1&'

try:  # 异常捕捉
    from sendNotify import send  # 导入消息通知模块
except Exception as err:  # 异常捕捉
    print('%s\n加载通知服务失败~' % err)


# 获取环境变量
def get_env():
    # 判断 COOKIE_ZHANGFEI是否存在于环境变量
    if "COOKIE_ZHANGFEI" in os.environ:
        # 读取系统变量 以 \n 分割变量
        cookie_list = os.environ.get('COOKIE_ZHANGFEI').split('\n')
        # 判断 cookie 数量 大于 0 个
        if len(cookie_list) <= 0:
            # 标准日志输出
            print('COOKIE_ZHANGFEI变量未启用')
            send('掌上飞车开金丝篓', 'COOKIE_ZHANGFEI变量未启用')
            # 脚本退出
            sys.exit(1)
    else:
        # 标准日志输出
        print('未添加COOKIE_ZHANGFEI变量')
        send('掌上飞车开金丝篓', '未添加COOKIE_ZHANGFEI变量')
        # 脚本退出
        sys.exit(0)

    # 判断 REFERER_ZHANGFEI是否存在于环境变量
    if "REFERER_ZHANGFEI" in os.environ:
        referer_list = os.environ.get('REFERER_ZHANGFEI').split('\n')
        if len(referer_list) <= 0:
            print('REFERER_ZHANGFEI变量未启用')
            send('掌上飞车开金丝篓', 'REFERER_ZHANGFEI变量未启用')
            sys.exit(1)
    else:
        print('未添加REFERER_ZHANGFEI变量')
        send('掌上飞车开金丝篓', '未添加REFERER_ZHANGFEI变量')
        sys.exit(0)

    return cookie_list, referer_list


# 开箱子
def openBox(cookie, user_data):
    msg = ''
    s = requests.Session()
    s.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 GH_QQConnect GameHelper_1003/2103040778'})

    url = "https://bang.qq.com/app/speed/chest/ajax/openBoxByKey"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 GH_QQConnect GameHelper_1003/2103040778',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Referer': f"https://bang.qq.com/app/speed/chest/index/v2?uin={user_data.get('roleId')}&roleId={user_data.get('roleId')}&uniqueRoleId={user_data.get('uniqueRoleId')}&accessToken={user_data.get('accessToken')}&userId={user_data.get('userId')}&token={user_data.get('token')}&areaId={user_data.get('areaId')}&",
        'Cookie': cookie
    }

    # 生成表单
    data = {
        'userId': user_data.get('userId'),  # 掌飞id
        'uin': user_data.get('roleId'),  # QQ账号
        'areaId': user_data.get('areaId'),  # 大区
        'token': user_data.get('token'),  # 令牌
        'keyId1': '17456',  # 大闸蟹17456
        'keyNum1': '2',  # 1个金丝篓开2个大闸蟹
        'boxId': '17455',  # 金丝篓17455
        'openNum': '1'  # 1个金丝篓开2个大闸蟹
    }

    # 延迟2秒执行，防止频繁
    # time.sleep(2)

    r = s.post(url=url, data=data, headers=headers)
    a = r.json()
    # 是否成功
    if 'data' in a:
        if 'itemList' in a.get('data'):
            itemList = a.get('data').get('itemList')
            num = 0
            for num in range(len(itemList)):
                msg += f"{itemList[num].get('avtarname')} * {itemList[num].get('num')} "
                print(
                    f"{itemList[num].get('avtarname')} * {itemList[num].get('num')}")
                num += 1

        if 'msg' in a.get('data'):
            msg += a.get('data').get('msg')
            print(a.get('data').get('msg'))

    return msg


def main(*arg):
    msg = ""
    sendnoty = 'true'
    global cookie_zhangfei
    global referer_zhangfei
    cookie_zhangfei, referer_zhangfei = get_env()

    i = 0
    while i < len(cookie_zhangfei):
        # 获取user_data参数
        user_data = {}
        for a in referer_zhangfei[i].split('?')[1].split('&'):
            if len(a) > 0:
                user_data.update(
                    {a.split('=')[0]: unquote(a.split('=')[1])})
        # print(user_data)

        # 开始任务
        log = f"第 {i+1} 个账号 {user_data.get('uin')} {user_data.get('roleName')} 开始执行任务"
        msg += log + '\n'
        print(log)

        # 开金丝篓 * 30
        num = 0
        for num in range(1):
            log = f"开第{num+1}个："
            msg += log
            print(log)

            # 开箱子
            log = openBox(cookie_zhangfei[i].replace(' ', ''), user_data)
            msg += log + '\n'
            if '雷诺' in msg:
                msg += '\n❗❗❗❗❗❗\n成功开出 永久雷诺\n❗❗❗❗❗❗\n'
                print('\n❗❗❗❗❗❗\n成功开出 永久雷诺\n❗❗❗❗❗❗\n')
                break
            if '不足' in msg:
                break

        i += 1

    if sendnoty:
        try:
            send('掌上飞车开金丝篓', msg)
        except Exception as err:
            print('%s\n错误，请查看运行日志！' % err)
            send('掌上飞车开金丝篓', '%s\n错误，请查看运行日志！' % err)

    return msg[:-1]


if __name__ == "__main__":
    print("----------掌上飞车开始尝试开金丝篓----------")
    main()
    print("----------掌上飞车开金丝篓执行完毕----------")