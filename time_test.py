# import time
# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H %h'))



import datetime
# print(datetime.datetime.now())
# newtime = datetime.timedelta(minutes=10)
# print(datetime.datetime.now()+newtime)

oneday=datetime.datetime(2008,5,27)
new_time=datetime.timedelta(days=10)
print(oneday+new_time)