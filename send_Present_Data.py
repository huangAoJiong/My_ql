import datetime

# 获取当前日期和时间
current_datetime = datetime.datetime.now()

# 格式化日期和时间
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_datetime)
