# 导入python内置的os模块和sys模块
import os
import sys
import time
# 程序入口
if __name__ == "__main__":
    mark ="_999_"
    # 获取本目录下所有的文件名
    path='E:\\Workspace-Python\\WxSQL-InspecTion\\win\\'
    old_names = os.listdir(path)
    print(old_names)
    # 遍历目录下的文件名
    for old_name in old_names:
        # 跳过本脚本文件
        if old_name != sys.argv[0]:
            # 用新的文件名替换旧的文件名
            s_time =(str(time.time())).replace('.','')
            old_name=old_name.split('.')[0]
            os.rename( path+old_name+'.png', old_name+mark+s_time+'.jpg')