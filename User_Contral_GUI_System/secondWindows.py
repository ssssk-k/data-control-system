#二、登录后页面
import tkinter as tk
from tkinter import filedialog
from tkinter import Text
import time
import difflib
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
        tk.Label(self.about_frame,text='关于作者：浙江传媒学院23数字媒体技术4班 于方旭',font=24).grid(row=2,column=2,pady=10)

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

        tk.Label(self.input_frame, text='备注：', font=('Arial', 12)).grid(row=3, column=0)  # 备注所在位置
        tk.Entry(self.input_frame, textvariable=self.bei).grid(row=3, column=1)



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


#!!!!!!文件不会实时更新，在成功上传一个文件之后就无法触发添加失败



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

        with open(self.filename_compare1,'r') as f1:
            compare1=f1.read()
        with open(self.filename_compare2, 'r') as f2:
            compare2 = f2.read()

        def compare_text():
            text1 = text_box1.get('1.0', tk.END)
            text2 = text_box2.get('1.0', tk.END)
            d = difflib.Differ()
            diff = d.compare(text1.splitlines(), text2.splitlines())
            result_text.delete('1.0', tk.END)
            result_text.insert(tk.END, '\n'.join(list(diff)))

        root = tk.Tk()
        root.title("Text Compare Tool")

        text_box1 = tk.Text(root, height=65, width=50)
        text_box1.pack(side=tk.LEFT)

        text_box2 = tk.Text(root, height=65, width=50)
        text_box2.pack(side=tk.LEFT)

        text_box1.insert(tk.END, compare1)
        text_box2.insert(tk.END, compare2)

        compare_button = tk.Button(root, text="Compare", command=compare_text)
        compare_button.pack(side=tk.TOP)

        result_text = tk.Text(root, height=65, width=50)
        result_text.pack(side=tk.LEFT)








    '''def count(self):

        try:
            with open(file=self.filename_input, mode='r+', encoding='utf-8') as file:
                file_text = file.read()
            with open(file=self.filename_output) as ff:
                x = ff.read()

        except:
            self.achievement = tk.Label(self.input_frame, text='添加失败！', font=('Arial', 24), fg='red')
            self.achievement.grid(row=4)
            self.input_frame.update()
            time.sleep(1)
            self.achievement.grid_forget()

        # 创建线程，如果函数里面有参数，args=()
        t = threading.Thread(target=self.count)
        # 开启线程
        t.start()


        # 更新窗口
        self.input_frame.update()#多线程处理防止阻塞
        time.sleep(5)
        self.achievement.grid_forget()'''





    '''def lable_quit(self):
        self.on_hit=False
        self.var=tk.StringVar()
        if self.on_hit==False:
            self.on_hit=True
            self.var.set('添加成功')
        else:
            self.on_hit=False
            self.var.set('')'''



            



if __name__=='__main__':
    root = tk.Tk()
    Page_secondWindows(root)
    root.mainloop()
