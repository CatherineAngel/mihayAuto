import requests
import xlwt
import time
import json



headers={
"Host": "api.gotokeep.com",
"Connection": "keep-alive",
"Authorization": "",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",

}
def 全部数据():
    url = 'https://api.gotokeep.com/tapers-webapp/run/group/activity/memberList?activityId=626672a74eea680001467684&pageSize=10&pageNum={}&onlyUnFinish=false'
    all_res1 = []
    userids=[]
    for j in range(1, 42):
        res = requests.get(url=url.format(j), headers=headers).text
        print("完成第", j, "页数据抓取")
        res = json.loads(res)
        activityMemberList = res['data']['activityMemberList']
        if(activityMemberList==[]):
            print("数据为空继续")
            continue
        for activi in activityMemberList:
            all_res = {}
            all_res['nickName'] = activi['nickName']
            all_res['userId'] = activi['userId']
            all_res['wxNickName'] = activi['wxNickName']
            all_res['targetDistance'] = activi['personalChallenge']['targetDistance']
            all_res['totalDistance'] = activi['personalChallenge']['totalDistance']
            all_res1.append(all_res)
            userids.append(activi['userId'])
        print("睡眠1s")
        time.sleep(1)

    Excel = xlwt.Workbook(encoding='utf-8', style_compression=0)
    table = Excel.add_sheet('Sheet1', cell_overwrite_ok=True)
    # 写入第一行
    table.write(0, 0, "昵称")
    table.write(0, 1, "用户Id")
    table.write(0, 2, "微信昵称")
    table.write(0, 3, "目标距离")
    table.write(0, 4, "总距离")

    for i in range(1, len(all_res1)):
        table.write(i, 0, all_res1[i-1]['nickName'])
        table.write(i, 1, all_res1[i-1]['userId'])
        table.write(i, 2, all_res1[i-1]['wxNickName'])
        table.write(i, 3, all_res1[i-1]['targetDistance'])
        table.write(i, 4, all_res1[i-1]['totalDistance'])

    Excel.save(r'跑图数据.xlsx')
    return all_res1
def 各自的数据(userids):
    Excel1 = xlwt.Workbook(encoding='utf-8', style_compression=0)
    table = Excel1.add_sheet('Sheet1', cell_overwrite_ok=True)
    count=1
    for i in range(len(userids)):
        userid=userids[i]['userId']
        wxNickName=userids[i]['wxNickName']
        nickName=userids[i]['nickName']
        print("正在爬取用户", userid,"数据")
        person_info_url = 'https://api.gotokeep.com/tapers-webapp/run/group/activity/personal/runList?activityId=626672a74eea680001467684&userId={}'.format(userid)
        res = requests.get(url=person_info_url, headers=headers).text
        res = json.loads(res)
        datas = res['data']
        print(datas)
        for data in datas:
            datetime = data['date']
            for  datei in data['detailList']:
                distance = datei['distance']
                duration = datei['duration']
                maxPacePerKm = datei['maxPacePerKm']
                startTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(datei['startTime']/1000))
                endTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(datei['endTime']/1000))
                table.write(count, 0, userid)
                table.write(count, 1, wxNickName)
                table.write(count, 2, nickName)
                table.write(count, 3, datetime)
                table.write(count, 4, distance)
                table.write(count, 5, duration)
                table.write(count, 6, maxPacePerKm)
                table.write(count, 7, startTime)
                table.write(count, 8, endTime)

                count+=1
        time.sleep(1)
        print("延迟一秒")

    Excel1.save(r'全部数据.xlsx')

# 写入第一行。
# for i in range(20):
# # 函数：table.write(行, 列, 要写入的数据)
#     table.write(0, i, classification[i])
# # Excel表保存的文件名字
# Excel.save(r'跑图数据.xlsx')
def shijian(timeStamp):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    return otherStyleTime
if __name__=='__main__':
    userids = 全部数据()
    各自的数据(userids)
    # 各自的数据([{'nickName': '用户gog6633ew', 'userId': '61d80a81af75f300012739e1', 'wxNickName': '专吃欧包', 'targetDistance': 120.0, 'totalDistance': 336.9194496999999}, {'nickName': '守望_r10', 'userId': '59b4678be66686780043820f', 'wxNickName': '守望', 'targetDistance': 100.0, 'totalDistance': 230.83752177}, {'nickName': 'wuli_sh', 'userId': '606da6df650b9c458e9a3d4c', 'wxNickName': None, 'targetDistance': 60.0, 'totalDistance': 222.23610641000005}, {'nickName': 'Sirius不要回答', 'userId': '5804e6b231f116684fec03ef', 'wxNickName': 'Monster.', 'targetDistance': 20.0, 'totalDistance': 203.3420865}, {'nickName': '欠子析', 'userId': '5cd1aeccd20f9c3a8e433876', 'wxNickName': '欠子析', 'targetDistance': 42.2, 'totalDistance': 194.6397158}, {'nickName': '爱深蹲的有信仰的在路上', 'userId': '5bcdc8ab7511ce3285aae462', 'wxNickName': '在路上', 'targetDistance': 80.0, 'totalDistance': 193.89438099999998}, {'nickName': '爱上树的_JYQ', 'userId': '5d3bd15255bcc44a873f95ee', 'wxNickName': '我亦是行人', 'targetDistance': 40.0, 'totalDistance': 178.48359240000002}, {'nickName': '序破Q终', 'userId': '5d02fa08c73d80102cc26ef1', 'wxNickName': 'Gogh', 'targetDistance': 40.0, 'totalDistance': 177.58368556000005}, {'nickName': '王婉aa', 'userId': '56e7f9a6524e652f0b04d496', 'wxNickName': '葡萄', 'targetDistance': 30.0, 'totalDistance': 176.3695969993137}, {'nickName': 'HebronZhai', 'userId': '59aea337e6668642acd099bc', 'wxNickName': 'Farewell', 'targetDistance': 20.0, 'totalDistance': 169.3887049}])
    #
    # url = 'https://api.gotokeep.com/tapers-webapp/run/group/activity/memberList?activityId=626672a74eea680001467684&pageSize=10&pageNum=43&onlyUnFinish=false'
    # res = requests.get(url=url, headers=headers).text
    # print(res)
    # res = json.loads(res)
    # activityMemberList = res['data']['activityMemberList']
