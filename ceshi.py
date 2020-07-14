import os

# 获取当前文件所在路径(*)
path = os.getcwd()

# 查看当前路径下的所有文件
print(os.listdir(path))

# 获取文件的大小
paths = path + '/nile_write.py'
print(paths)
print(os.path.getsize(paths))

# 文件路径的拼接(爬取的文件管理)(*)
path1 = os.path.join(path, 'dir', 'file_write.py')  # 其中的 'dir'为新建文件夹名，若不想新建文件夹可删除
print(path1)

# 判断路径是否存在(*)
print(os.path.exists(path1))    # 不存在返回Ｆａｌｓｅ
path2 = '/home/tarena/PycharmProjects/PYTHON_VIP/Class_2/Day09/file_write.py'
print(os.path.exists(path2))

# 创建文件目录(方便文件的管理)(*)
path3 = os.path.join(path, 'dir')
# print(path3)
# os.mkdir(path3)

# 判断是否是文件
path2 = '/home/tarena/PycharmProjects/PYTHON_VIP/Class_2/Day09/file_write.py'
print(os.path.isfile(path2))
print(os.path.isfile(path3))

# 删除文件
path = os.path.join(os.getcwd(), 'seq.txt')
print(path)
os.remove(path)

# 构建文件路径
os.path.join(os.getcwd(), 'path')

# 判断该路径
path = os.path.join(os.getcwd(), 'path')
if not os.path.exists(path):
     os.makedir(path)