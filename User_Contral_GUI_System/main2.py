''''#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python2.x 导入方法
from tkinter import *  # 导入 Tkinter 库

# Python3.x 导入方法
# from tkinter import *
root = Tk()  # 创建窗口对象的背景色
# 创建两个列表
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = Listbox(root)  # 创建两个列表组件
listb2 = Listbox(root)
for item in li:  # 第一个小部件插入数据
    listb.insert(0, item)

for item in movie:  # 第二个小部件插入数据
    listb2.insert(0, item)

listb.pack()  # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()  # 进入消息循环'''


'''import time
import os
t1 = time.asctime(time.localtime())
t2=time.localtime()
a=t2.tm_year
b=t2.tm_mon
c=t2.tm_mday
d=t2.tm_hour
e=t2.tm_min
f=t2.tm_sec
filename_save= 'D://daima'+ '//'+f'{a};{b}.{c};{d}.{e}.{f}.txt'

print(filename_save)
a=open(rf'{filename_save}','w')
a.write('nihjjao')
a.close()'''



'''tkinter解决time延迟问题'''
'''import tkinter as tk
import time
import threading
# 初始化窗口
window = tk.Tk()
# 窗口名称
window.title("My Window")
# 窗口大小,是 x 不是 *
window.geometry("400x400")
# 不能改变窗口的大小
window.resizable(width=False,height=False)
def count():
    label = tk.Label(window,bg='green')
    label.pack()
    button.pack()
    while True:
        try:
            # 获取当前时间
            date = time.strftime("%Y-%m-%d\n%H:%M:%S")
            label.config(text=date)
            #更新窗口
            window.update()
            time.sleep(1)
        except:
            break
# 创建按钮，只是为了测试sleep与按钮之间是否存在延迟
button = tk.Button(window,text='Hit_me',width=20)
# 创建线程，如果函数里面有参数，args=()
t = threading.Thread(target=count)
# 开启线程
t.start()
# 循环窗口
window.mainloop()'''





'''import tkinter as tk
from tkinter import filedialog
root = tk.Tk()

path1 = filename_input1 = filedialog.askopenfilename()
path2 = filename_input2 = filedialog.askopenfilename()
x1=open(path1,'r')
content1=x1.read()
x2=open(path2,'r')
content2=x2.read()

sb = tk.Scrollbar(root)
txt1 = tk.Text(
    root,
    font=('楷体', 15),
    bg='#e9faff',
    width=65,
    height=30
)

txt2 = tk.Text(
    root,
    font=('楷体', 15),
    bg='#e9faff',
    width=65,
    height=30
)
# 创建下方滚动条
scroll_x = tk.Scrollbar(root, orient=tk.HORIZONTAL)
# 创建右侧滚动条
scroll_y = tk.Scrollbar(root)
# 放到窗体的右侧 沿Y轴平铺
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
# 放到窗体的下方 沿X轴平铺
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
txt1.pack(side=tk.RIGHT, fill=tk.Y)
txt2.pack(side=tk.RIGHT, fill=tk.Y)
# 关联文本控件
scroll_y.config(command=txt1.yview)
scroll_x.config(command=txt1.xview)

scroll_y.config(command=txt2.yview)
scroll_x.config(command=txt2.xview)

txt1.insert(tk.INSERT, content1)
txt2.insert(tk.INSERT, content2)



root.mainloop()'''

'''from difflib import HtmlDiff


def get_file_content(file_path):
    lines = []
    with open(file_path, mode="r", encoding="utf8") as f:
        lines = f.read().splitlines()
    return lines


def compare_file(file1, file2):
    lines1 = get_file_content(file1)
    lines2 = get_file_content(file2)

    # 找出差异输出到result(str)
    html_diff = HtmlDiff()
    result = html_diff.make_file(lines1, lines2)

    # 将差异写入html文件
    with open("comparison.html", "w", encoding="utf8") as f:
        f.write(result)


if __name__ == "__main__":
    file11 = "C:\\Users\86199\Desktop\\1.txt"
    file22 = "C:\\Users\86199\Desktop\\2.txt"
    compare_file(file11, file22)'''

'''import tkinter as tk
from tkinter import filedialog
import difflib


def load_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as f:
            return f.read()
    return ''


def compare_text():
    text1 = text_box1.get('1.0', tk.END)
    text2 = text_box2.get('1.0', tk.END)
    d = difflib.Differ()
    diff = d.compare(text1.splitlines(), text2.splitlines())
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, '\n'.join(list(diff)))


root = tk.Tk()
root.title("Text Compare Tool")

text_box1 = tk.Text(root, height=20, width=50)
text_box1.pack(side=tk.LEFT)

text_box2 = tk.Text(root, height=20, width=50)
text_box2.pack(side=tk.LEFT)

text_box1.insert(tk.END, load_file())


text_box2.insert(tk.END, load_file())


compare_button = tk.Button(root, text="Compare", command=compare_text)
compare_button.pack(side=tk.TOP)

result_text = tk.Text(root, height=20, width=50)
result_text.pack(side=tk.LEFT)

root.mainloop()'''


import tkinter as tk
import copy
class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry('600x400')
        self.register_frame=tk.Frame(self.root)
        self.register_frame.pack()

        self.register_username = tk.StringVar()
        self.register_password = tk.StringVar()

        with open('user.txt', mode='r', encoding='utf-8') as f1:  # 从用户库中查询所有信息
            self.users = eval(f1.read())
        self.user = {}



        tk.Label(self.register_frame, text='账户：', font=('Arial', 12)).grid(row=1, column=1, pady=10)  # 账户所在位置
        tk.Entry(self.register_frame, textvariable=self.register_username).grid(row=1, column=2)  # 输入框所在位置

        tk.Label(self.register_frame, text='密码：', font=('Arial', 12)).grid(row=2, column=1, pady=10)  # 密码所在位置
        tk.Entry(self.register_frame, textvariable=self.register_password).grid(row=2, column=2)  # 输入框所在位置

        tk.Button(self.register_frame, text='注册', fg='red', command=self.register_in).grid(row=3, column=1, pady=20)  # 注册按钮
        tk.Button(self.register_frame, text='取消', command=quit).grid(row=3, column=3, pady=20)  # 取消按钮,直接退出界面


    def register_check(self,register_username):

        if register_username == None or register_username.strip() == "":
            self.kong=tk.Label(self.register_frame,text='用户名不能为空',fg='red')
            self.kong.grid(row=3, column=2, pady=10)
            return False

        for i in self.users:
            if i.get("username") == self.username:
                self.cunzai=tk.Label(self.register_frame, text='对不起，该用户已经存在，请重新输入', fg='red')
                self.cunzai.grid(row=3, column=2, pady=10)
                return False
        return True


    def register_in(self):
        self.username = self.register_username.get()  # get到输入的用户名
        self.password = self.register_password.get()  # get到输入的密码

        check=self.register_check(self.username)
        if check:
            self.kong.grid_forget()
            self.cunzai.grid_forget()
            tk.Label(self.register_frame, text='注册成功', fg='red').grid(row=3, column=2, pady=10)
            self.user=copy.deepcopy(self.users)
            self.user.append({'username':self.username,'password':self.password})
            with open('user.txt', mode='w', encoding='utf-8') as f2:  # 从用户库中查询所有信息
                f2.write(str(self.user))
        self.register_frame.destroy()
        Page_firstWindows(root)

if __name__ == '__main__':
    root = tk.Tk()
    Register(root)
    root.mainloop()










'''def is_login(username, password):
        for i in users:
            if i.get("username") == username and i.get("password") == password:
                print("登录成功")
                return True
            return False


    def login():
        username = input("输入用户名：")
        password = input("输入用户密码：")
        password = password

        if is_login(username, password):
            print("恭喜你登录成功")
        else:
            print("对不起，登录失败，请重新登录")


while True:
    choice = main()
    if choice == "1":
        print("用户注册")
        register()
    elif choice == "2":
        print("用户登录")
        login()
    elif choice == "3":
        print("程序正常退出")
        sys.exit()
    else:
        print("请输入正确的数字")
        main()'''






