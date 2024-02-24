#一、登录页面
import tkinter as tk
from tkinter import filedialog
import difflib
import time
import copy


class Userdata:

    def __init__(self):
        with open('user.txt', mode='r', encoding='utf-8') as f:#从用户库中查询所有信息
            self.text = eval(f.read())

    def check_login(self, username, password):
        for user in self.text:
            if user.get('username') == username:
                if user.get('password') == password:
                    return True, '登 录 成 功!'
                else:
                    return False, '密 码 错 误'
        else:
            return False, '用户不存在'

GUI_mode=Userdata()
class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry('600x400')
        self.root.title('注册界面')
        self.register_frame=tk.Frame(self.root)
        self.register_frame.pack()

        self.register_username = tk.StringVar()
        self.register_password = tk.StringVar()

        with open('user.txt', mode='r', encoding='utf-8') as f1:  # 从用户库中查询所有信息
            self.users = eval(f1.read())
            f1.close()



        tk.Label(self.register_frame, text='账户：', font=('Arial', 12)).grid(row=1, column=1, pady=10)  # 账户所在位置
        tk.Entry(self.register_frame, textvariable=self.register_username).grid(row=1, column=2)  # 输入框所在位置

        tk.Label(self.register_frame, text='密码：', font=('Arial', 12)).grid(row=2, column=1, pady=10)  # 密码所在位置
        tk.Entry(self.register_frame, textvariable=self.register_password).grid(row=2, column=2)  # 输入框所在位置

        tk.Button(self.register_frame, text='注册', fg='red', command=self.register_in).grid(row=3, column=1, pady=20)  # 注册按钮
        tk.Button(self.register_frame, text='取消', command=self.quxiao).grid(row=3, column=3, pady=20)  # 取消按钮,直接退出界面


    def register_check(self,register_username):

        if register_username == None or register_username.strip() == "":
            '''try:
                self.cunzai.grid_forget()
            except:
                pass'''
            self.kong=tk.Label(self.register_frame,text='用户名不能为空',fg='red')
            self.kong.grid(row=3, column=2, pady=10)
            return False

        for i in self.users:
            if i.get("username") == self.username:
                '''try:
                    self.kong.grid_forget()
                except:
                    pass'''
                self.cunzai=tk.Label(self.register_frame, text='对不起，该用户已经存在，请重新输入', fg='red')
                self.cunzai.grid(row=3, column=2, pady=10)
                return False
        return True


    def register_in(self):

        self.username = self.register_username.get()  # get到输入的用户名
        self.password = self.register_password.get()  # get到输入的密码

        check=self.register_check(self.username)
        if check:
            #self.kong.grid_forget()
            #self.cunzai.grid_forget()
            tk.Label(self.register_frame, text='注册成功', fg='red').grid(row=3, column=2, pady=10)
            self.user=copy.deepcopy(self.users)
            self.user.append({'username':self.username,'password':self.password})
            with open('user.txt', mode='w', encoding='utf-8') as f2:  # 从用户库中查询所有信息
                f2.write(str(self.user))
                f2.close()


    def quxiao(self):
        self.register_frame.destroy()
        Page_firstWindows(root)


class Page_firstWindows:
    def __init__(self,master):

        self.root=master
        self.root.geometry('600x250')#初始窗口的大小
        self.root.title('登录页面')#窗口左上角的标题

        self.username=tk.StringVar()
        self.password=tk.StringVar()
        #check=tk.StringVar()

        self.page=tk.Frame(root)#在屏幕上显示一个矩形区域
        self.page.pack()#pack函数布局页面
        self.page.update()
        tk.Label(self.page).grid(row=0,column=0)

        tk.Label(self.page,text='账户：',font=('Arial', 12)).grid(row=1,column=1,pady=10)#账户所在位置
        tk.Entry(self.page,textvariable=self.username).grid(row=1,column=2)#输入框所在位置

        tk.Label(self.page,text='密码：',font=('Arial', 12)).grid(row=2,column=1,pady=10)#密码所在位置
        tk.Entry(self.page,textvariable=self.password).grid(row=2,column=2)#输入框所在位置

        #tk.Label(page,textvariable=check).grid(row=3,column=2)
        tk.Button(self.page, text='注册', fg='red', command=self.zhuce).grid(row=4, column=2, pady=20)  # 注册按钮
        tk.Button(self.page,text='登录',fg='red',command=self.get_in).grid(row=3,column=1,pady=20)#登录按钮
        tk.Button(self.page,text='取消',command=quit).grid(row=3,column=3,pady=20)#取消按钮,直接退出界面

    def get_in(self):#获取用户输入的结果

        name=self.username.get()#get到输入的用户名
        pwd=self.password.get()#get到输入的密码

        check_result,information_result=GUI_mode.check_login(name,pwd)#检验输入的数据是否在数据库中

        if check_result:
            #tk.Label(page, text='账户或密码错误',fg='beige').grid(row=3, column=2, pady=10)#用颜色掩盖过去，以后改一下这个代码吧
            tk.Label(self.page,text=information_result,fg='green').grid(row=3,column=2,pady=10)
            self.page.destroy()
            Page_secondWindows(self.root)
        else:
            tk.Label(self.page,text=information_result,fg='red').grid(row=3,column=2,pady=10)


    def zhuce(self):
        self.page.destroy()
        Register(root)


#二、系统界面
class Page_secondWindows:#定义登录后页面
    def __init__(self,master:tk.Tk):#tk.Tk不影响代码，只是标注master是个TK属性的字符串，可以有智能提示
        self.root=master
        self.root.title('代码版本管理系统 v0.0.1')
        self.root.geometry('600x400')
        self.creat_page()

    def creat_page(self):#菜单栏
        #设计关于页面的内容

        self.about_frame =tk.Frame(self.root)
        tk.Label(self.about_frame,text='关于作品：本作品使用tkinter制作',font=24).grid(row=1,column=2)
        tk.Label(self.about_frame,text='关于作者：浙江传媒学院学生制作',font=24).grid(row=2,column=2,pady=10)

        #设计添加页面的内容
        self.input_frame=tk.Frame(self.root)
        txt_input = '请选择你要上传的代码文件'
        txt_output='请选择你要存储的位置'
        self.bei=tk.StringVar()

        self.choice_input_label = tk.Label(self.input_frame, text=txt_input, font=('宋体', 10), padx=7, pady=7, borderwidth=1, width=40, height=1,
                         anchor='w', relief='solid')
        self.choice_input_button = tk.Button(self.input_frame, text='选择文件', anchor='w', command=self.choice_input)
        self.choice_input_label.grid(row=1, column=0)
        self.choice_input_button.grid(row=1, column=1)

        self.choice_output_label=tk.Label(self.input_frame, text=txt_output, font=('宋体', 10), padx=7, pady=7, borderwidth=1, width=40, height=1,
                         anchor='w', relief='solid')
        self.choice_output_button=tk.Button(self.input_frame, text='选择文件', anchor='w',command=self.choice_output)
        self.choice_output_label.grid(row=2, column=0)
        self.choice_output_button.grid(row=2, column=1)
        tk.Button(self.input_frame, text='确定', command=self.file_read).grid(row=2, column=2)
        #tk.Label(self.input_frame,text='注：点击确定后代码文件会自动复制到所输出文件中').grid(row=4)

        tk.Label(self.input_frame, text='备注：', font=('Arial', 12)).grid(row=3, column=0,pady=10)  # 备注所在位置
        tk.Entry(self.input_frame, textvariable=self.bei).grid(row=3, column=1,pady=10)



        #添加查询页面的内容,代码逻辑与添加页面相同
        self.inquire_frame=tk.Frame(self.root)


        txt_input1 = '请选择你要对比的代码文件'
        txt_input2 = '请选择你要对比的代码文件'
        self.choice_compare1_label = tk.Label(self.inquire_frame, text=txt_input1, font=('宋体', 10), padx=7, pady=7,
                                           borderwidth=1, width=40, height=1,anchor='w', relief='solid')
        self.choice_compare1_button = tk.Button(self.inquire_frame, text='选择文件', anchor='w', command=self.chioce_compare1)
        self.choice_compare1_label.grid(row=1, column=0)
        self.choice_compare1_button.grid(row=1, column=1)

        self.choice_compare2_label = tk.Label(self.inquire_frame, text=txt_input2, font=('宋体', 10), padx=7, pady=7,
                                            borderwidth=1, width=40, height=1,anchor='w', relief='solid')
        self.choice_compare2_button = tk.Button(self.inquire_frame, text='选择文件', anchor='w', command=self.chioce_compare2)
        self.choice_compare2_label.grid(row=2, column=0)
        self.choice_compare2_button.grid(row=2, column=1)
        tk.Button(self.inquire_frame, text='确定', command=self.file_compare).grid(row=2, column=2)



        #添加菜单栏
        menubar=tk.Menu(self.root)
        menubar.add_command(label='添加',command=self.show_input)
        menubar.add_command(label='查询',command=self.show_inquire)
        menubar.add_command(label='关于',command=self.show_about)
        self.root['menu']=menubar


    #要做到一个菜单显示的时候其他都不显示

    def show_about(self):
        self.about_frame.pack()
        self.input_frame.forget()
        self.inquire_frame.forget()
        self.achievement.grid_forget()
        self.fault.grid_forget()

        #不把self.about_frame定义放一起是因为每点击一下都会再创建一次，所以每点一次都会不断出现关于中的信息

    def show_input(self):
        self.input_frame.pack()
        self.about_frame.forget()
        self.inquire_frame.forget()
        self.fault.grid_forget()



    def show_inquire(self):
        self.inquire_frame.pack()
        self.about_frame.forget()
        self.input_frame.forget()
        self.achievement.grid_forget()
        self.fault.grid_forget()


    #定义选择文件函数
    def choice_input(self):
        self.filename_input = filedialog.askopenfilename()
        if self.filename_input != '':
             self.choice_input_label.config(text= self.filename_input)
        else:
             self.choice_input_label.config(text='请选择你要上传的代码文件')
    #定义输出文件函数
    def choice_output(self):
        self.filename_output=filedialog.askdirectory()
        if self.filename_output != '':
             self.choice_output_label.config(text= self.filename_output)
        else:
             self.choice_output_label.config(text='请选择你要存储的位置')



    def file_read(self):

        try:
            with open(file=self.filename_input, mode='r+', encoding='utf-8') as file:
                file_text = file.read()
            with open(file=self.filename_output) as ff:
                x=ff.read()
        except:
            self.fault = tk.Label(self.input_frame, text='添加失败！', font=('Arial', 24), fg='red')
            self.fault.grid(row=4)

        self.t = time.localtime()
        a = self.t.tm_year
        b = self.t.tm_mon
        c = self.t.tm_mday
        d = self.t.tm_hour
        e = self.t.tm_min
        f = self.t.tm_sec
        beizhu = self.bei.get()  # get到输入的备注
        self.filename_save=f'{self.filename_output}/{a};{b}.{c};{d}.{e}.{f}({beizhu}).txt'#用保存时间给文件命名，清晰且不重复

        a=open(self.filename_save,"w")
        a.write(file_text)
        self.achievement=tk.Label(self.input_frame, text='添加成功！',font=('Arial', 24),fg='red')
        self.achievement.grid(row=4)


    def chioce_compare1(self):
        self.filename_compare1 = filedialog.askopenfilename()
        if self.filename_compare1 != '':
             self.choice_compare1_label.config(text= self.filename_compare1)
        else:
             self.choice_compare1_label.config(text='请选择你要对比的代码文件')

    def chioce_compare2(self):
        self.filename_compare2 = filedialog.askopenfilename()
        if self.filename_compare2 != '':
            self.choice_compare2_label.config(text=self.filename_compare2)
        else:
            self.choice_compare2_label.config(text='请选择你要对比的代码文件')
    def file_compare(self):

        with open(self.filename_compare1,'r',encoding='utf-8') as f1:#utf-8防止中文乱码
            compare1=f1.read()
        with open(self.filename_compare2, 'r',encoding='utf-8') as f2:#防止中文乱码
            compare2 = f2.read()

        def compare_text():
            text1 = text_box1.get('1.0', tk.END)
            text2 = text_box2.get('1.0', tk.END)
            d = difflib.Differ()#用于过滤函数
            diff = d.compare(text1.splitlines(), text2.splitlines())#两个文件差异
            result_text.delete('1.0', tk.END)
            result_text.insert(tk.END, '\n'.join(list(diff)))#显示比较结果，包括换行

        root = tk.Tk()
        root.title("代码比较结果")

        text_box1 = tk.Text(root, height=100, width=80)
        text_box1.pack(side=tk.LEFT)#开始位置

        text_box2 = tk.Text(root, height=100, width=80)
        text_box2.pack(side=tk.LEFT)

        text_box1.insert(tk.END, compare1)#结束位置
        text_box2.insert(tk.END, compare2)

        compare_button = tk.Button(root, text="比较", command=compare_text)
        compare_button.pack(side=tk.TOP)#按钮位置

        result_text = tk.Text(root, height=100, width=80)
        result_text.pack(side=tk.LEFT)

if __name__=='__main__':
    root=tk.Tk()#引用tk中的Tk方法
    Page_firstWindows(root)
    root.mainloop()



