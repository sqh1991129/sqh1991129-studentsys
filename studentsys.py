import os

fileName = "studentInfo.txt"


# 主菜单列表
def menu():
    print("=======================学生信息管理系统======================")
    print("------------------------功能菜单---------------------------------")
    print("\t\t\t\t\t\t1.录入学生信息")
    print("\t\t\t\t\t\t2.查找学生信息")
    print("\t\t\t\t\t\t3.删除学生信息")
    print("\t\t\t\t\t\t4.修改学生信息")
    print("\t\t\t\t\t\t5.排序")
    print("\t\t\t\t\t\t6.统计学生总人数")
    print("\t\t\t\t\t\t7.显示所有学生信息")
    print("\t\t\t\t\t\t0.退出")


'''
 功能主函数
'''


def main():
    while True:
        # 显示系统菜单
        menu()
        choice = int(input("请选择："))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                choiceExit = input("请确认是否退出系统？y/n:")
                if choiceExit == "y" or choiceExit == "Y":
                    print("欢迎再次使用")
                    break
            elif choice == 1:
                add()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()

        else:
            print("不能识别的操作,请检查输入")


# 添加学生信息,保存到字典，写入本地磁盘


def add():
    # 学生信息集合
    student_lis = []
    while True:
        sid = input("请输入学生ID(如：1001)：")
        if not id:
            break
        name = input("请输入学生姓名：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入Python成绩："))
            java = int(input("请输入java成绩："))
            # 定义学生信息字典
            info = {"id": sid, "name": name, "english": english, "python": python, "java": java}
            student_lis.append(info)
        except:
            print("输入错误请重新输入")
            continue
        answer = input("是否继续录入学生信息？y/n:")
        if answer == "y":
            continue
        else:
            # 保存并退出系统
            print("学生信息录入完毕")
            save(student_lis)
            break


# 保存学生信息到文件中
def save(list):
    try:
        studentFile = open(fileName, "b", encoding="utf-8")
    except:
        studentFile = open(fileName, "w", encoding="utf-8")
    for info in list:
        studentFile.write(str(info) + "\n")
    studentFile.close()


# 查找学生信息


def search():
    stid = input("请输入要查找的学生ID:")
    if stid == "":
        print("没有输入学习ID")
        search()
    else:
        # 读取文件中内容
        with open(fileName, "r", encoding="utf-8") as rFile:
            s_lst = rFile.readlines()
            for item in s_lst:
                d = dict(eval(item))
                if d["id"] == stid:
                    print("已查询到学生信息")
                else:
                    print("未查询到学生信息")


# 删除学生信息

def delete():
    while True:
        sid = input("请输入学生ID(如：1001)：")
        # 文件中读的所有学生信息
        #  判断文件是否存在
        if os.path.exists(fileName):
            # 读取文件中所有学生信息
            with open(fileName, "r", encoding="utf-8") as rfile:
                old_info = rfile.readlines()
        else:
            old_info = []
        flag = False
        if old_info:
            for info in old_info:
                sinfo = dict(eval(info))
                if sinfo["id"] != sid:
                    # 重新写入磁盘
                    with open(fileName, "w", encoding="utf-8") as wFile:
                        wFile.write(str(sinfo))
                else:
                    flag = True
                if flag:
                    print(f"学号为{sid}的学生信息已被删除")
                else:
                    print(f"学号为{sid}的学生信息未被找到")

        else:
            print(f"无法找到学生信息{sid}")
        answer = input("是否继续删除?y/n:")
        if answer == "y":
            continue
        else:
            break
    #  重新显示学生信息
    show()


# 修改学生信息


def modify():
    pass


# 排序

def sort():
    pass


# 统计学生总数


def total():
    pass


# 显示学生信息

def show():
    pass


# 运行主函数


if __name__ == '__main__':
    main()
