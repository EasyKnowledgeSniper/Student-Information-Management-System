# @curryyuan30
# IT IS THE COURAGE TO CONTINUE THAT COUNTS
# an online interview in 25 March 2022.

import os

fileName = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()  # 查找学生信息
            elif choice == 3:
                delete()  # 删除学生信息
            elif choice == 4:
                modify()  # 修改学生信息
            elif choice == 5:
                sort()  # 排序
            elif choice == 6:
                total()  # 统计学生总人数
            elif choice == 7:
                show()  # 显示所有学生信息


def menu():
    print('===================================学生信息管理系统=====================================')
    print('-----------------------------------功能菜单--------------------------------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出')
    print('-------------------------------------------------------------------------------------')


def insert():  # 录入学生信息
    student_list = []
    while True:
        id = input('请输入ID（如1001）：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            englishResult = int(input('请输入英语成绩：'))
            pythonResult = int(input('请输入Python成绩：'))
            javaResult = int(input('请输入Java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        # 将录入的学生信息保存到字典当中
        student = {'id': id, 'name': name, 'englishResult': englishResult,
                   'pythonResult': pythonResult, 'javaResult': javaResult}
        # 将学生信息添加到列表中
        student_list.append(student)
        # 是否继续添加学生信息？
        answer = input('是否继续添加学生信息？ y/n\n')
        if answer == 'y':
            continue
        else:
            break
    # 调用save()函数
    save(student_list)
    print('学生信息录入完毕！！！')


def save(lst):
    try:
        stu_txt = open(fileName, 'a', encoding='utf-8')  # 以追加的方式打开
    except:
        stu_txt = open(fileName, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []  # 因为同名学生可能很多，所以要把id和name放到列表里
    while True:
        id = ''
        name = ''
        if os.path.exists(fileName):
            mode = input('按ID查找请输入“1”，按姓名查找请输入“2”：')
            if mode == '1':
                id = input('请输入学生ID：')
            elif mode == '2':
                name = input('请输入学生姓名：')
            else:
                print('您输入有误，请重新输入')
                search()
            with open(fileName, 'r', encoding='utf-8') as rFile:
                student = rFile.readlines()  # 读取，放进这个列表里
                for item in student:  # 遍历这个列表
                    d = dict(eval(item))  # 把字符串转换为字典类型
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)  # 将查找到的学生添加到student_query列表当中
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input('是否要继续查询？ y/n\n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return


# 显示查询结果的函数
def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！！！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', 'English成绩', 'Python成绩', 'Java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('englishResult'),
                                 item.get('pythonResult'),
                                 item.get('javaResult'),
                                 int(item.get('englishResult')) + int(item.get('pythonResult'))
                                 + int(item.get('javaResult'))
                                 ))


def delete():
    while True:
        student_id = input('请输入要删除的学生id：')
        if student_id != '':
            if os.path.exists(fileName):  # 判断文件是否存在
                with open(fileName, 'r', encoding='utf-8') as file:  # 上下文管理语句，将文件打开
                    student_old = file.readlines()  # 文件存在时，读取所有数据，把文件放到列表student_old中
            else:  # 文件不存在时
                student_old = []
            flag = False  # 用来标记是否删除，默认无删除
            if student_old:  # 如果此列表不为空，故bool值为1
                with open(fileName, 'w', encoding='utf-8') as wFile:
                    d = {}  # 空字典
                    for item in student_old:  # 遍历列表，将不删除的信息重新写入文件
                        # print(item)
                        d = dict(eval(item))  # eval()将字符串转成字典
                        if d['id'] != student_id:
                            wFile.write(str(d) + '\n')  # 删除即覆盖
                        else:
                            flag = True  # 表示已删除
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:  # 若列表student_old无数据，即从磁盘上没有读到数据
                print('无学生信息')
                break
            show()  # 删除之后要重新显示所有学生信息
            answer = input('是否继续删除？ y/n\n')
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as rFile:
            student_old = rFile.readlines()
    else:
        return
    student_id = input('请输入要修改的学员的ID：')
    with open(fileName, 'w', encoding='utf-8') as wFile:
        for item in student_old:
            d = dict(eval(item))  # 把读取到的字符串转换成 字典类型
            if d['id'] == student_id:
                print('找到学生信息，可以修改他的相关信息！')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['englishResult'] = input('请输入英语成绩：')
                        d['pythonResult'] = input('请输入Python成绩：')
                        d['javaResult'] = input('请输入Java成绩：')
                    except:
                        print('您的输入有误，请重新输入！！！')
                    else:
                        break
                wFile.write(str(d) + '\n')
                print('修改成功！！！')
            else:
                wFile.write(str(d) + '\n')
    answer = input('是否继续修改其他学生的信息？ y/n\n')
    if answer == 'y' or answer == 'Y':
        modify()


# 排序函数
def sort():
    show()
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as sFile:
            student_list = sFile.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)  # 把d字典添加到student_new列表当中
    else:
        return
    ascend_or_descend = input('请选择（0，升序 1，降序）：')
    if ascend_or_descend == '0':
        ascend_or_descend_bool = False
    elif ascend_or_descend == '1':
        ascend_or_descend_bool = True
    else:
        print('您的输入有误，请重新输入！')
        sort()
    mode = input('请选择排序方式（1.按English成绩排序 2.按Python成绩排序 3.按Java成绩排序 0.按总成绩排序）：')
    if mode == '1':
        '''lambda是匿名函数，student_new是一个列表，里面存放的是字典。下面的x（可以是任意名字）代表的就是列表中的内容，也就是字典，
        根据Keys来获取值'''
        student_new.sort(key=lambda x: int(x['englishResult']), reverse=ascend_or_descend_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['pythonResult']), reverse=ascend_or_descend_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['javaResult']), reverse=ascend_or_descend_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['englishResult']) + int(x['pythonResult'])
                                       + int(x['javaResult']), reverse=ascend_or_descend_bool)
    else:
        print('您的输入有误，请重新输入！！！')
        sort()
    show_student(student_new)  # 排序完后，展示学生信息


# 统计学生总人数的函数
def total():
    if os.path.exists(fileName):  # 判断文件是否存在
        with open(fileName, 'r', encoding='utf-8') as tFile:  # 打开文件
            students = tFile.readlines()  # 读取文件内容
            if students:  # 若列表不为空，为空则为False
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息！')
    else:
        print('暂未保存数据信息......')


# 显示所有学生信息功能
def show():
    student_lst = []
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as sFile:
            students = sFile.readlines()
            for item in students:
                student_lst.append(eval(item))  # 将读到的字符串转换成字典类型，再添加到student_lst列表中
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存过数据！！！')


print(__name__)
if __name__ == '__main__':  # 直接作为脚本执行，而不是import到其他Python脚本中被调用执行
    main()
