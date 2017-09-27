from tkinter import *
root = Tk()

# gui-01 最简单的GUI hello world
# label = Label(root,text='Hello tkinter')
# label.pack()

# gui-02 带图片的Label
# logo = PhotoImage(file='images/python_logo_small.gif')
# w1 = Label(root,image=logo).pack(side='right')
# s = 'At present, only GIF and PPM/PGM formats are supported'
# w2 = Label(root,justify=LEFT,padx=10,text=s).pack(side='left')

# gui-03 跳转Label中图片与文字的位置
# logo = PhotoImage(file='images/python_logo_small.gif')
# s = 'At present, only GIF and PPM/PGM formats are supported'
# # w = Label(root,image=logo,text=s,compound=CENTER).pack(side='left')
# w = Label(root,image=logo,text=s,compound=LEFT,padx=20,justify=LEFT).pack(side='left')

# gui-04 设置Label的文字，颜色，背景色
# Label(root, 
# 		 text="Red Text in Times Font",
# 		 fg = "red",
# 		 font = "Times").pack()
# Label(root, 
# 		 text="Green Text in Helvetica Font",
# 		 fg = "light green",
# 		 bg = "dark green",
# 		 font = "Helvetica 16 bold italic").pack()
# Label(root, 
# 		 text="Blue Text in Verdana bold",
# 		 fg = "blue",
# 		 bg = "yellow",
# 		 font = "Verdana 10 bold").pack()

# gui-04 动态设置Label文字
# counter = 0 
# def counter_label(label):
#   def count():
#     global counter
#     counter += 1
#     label.config(text=str(counter))
#     label.after(1000, count)
#   count()
 
 
# root.title("Counting Seconds")
# label = Label(root, fg="green")
# label.pack()
# counter_label(label)
# button = Button(root, text='Stop', width=25, command=root.destroy)
# button.pack()

# gui-05 Button
# class App(Frame):
# 	def __init__(self,master=None):
# 		super().__init__(master)
# 		self.pack()
# 		self.button = Button(self,text='Quit',fg='red',command=quit)
# 		self.button.pack(side=LEFT)
# 		self.slogan = Button(self,text='Hello',command=self.print_slogan)
# 		self.slogan.pack(side=LEFT)
# 	def print_slogan(self):
# 		print('life is short,you need python')
# app = App(root)

# gui-05 不使用继承 实现上例
# class App(object):
# 	def __init__(self,master=None):
# 		frame = Frame(master)
# 		frame.pack()
# 		self.button = Button(frame,text='Quit',fg='red',command=quit)
# 		self.button.pack(side=LEFT)
# 		self.slogan = Button(frame,text='Hello',command=self.print_slogan)
# 		self.slogan.pack(side=LEFT)
# 	def print_slogan(self):
# 		print('life is short,you need python')
# app = App(root)

# gui-06 动态设置label文字 指定按下stop按钮
# counter = 0
# def count_label(label):
# 	def count():
# 		global counter
# 		counter += 1
# 		label.config(text=str(counter))
# 		label.after(1000,count)
# 	count()
# label = Label(root,fg='dark green')
# label.pack()
# button = Button(root,text='stop',command=root.destroy)
# button.pack()
# count_label(label)

# gui-07 radio button
# v = IntVar()
# Label(root,
# 	text='Choose a programming language:',
# 	justify = LEFT,
# 	padx = 20
# 	).pack()
# Radiobutton(root,
# 	text='Python',
# 	padx=20,
# 	variable=v,
# 	value=1).pack(anchor=W)
# Radiobutton(root,
# 	text='Java',
# 	padx=20,
# 	variable=v,
# 	value=2).pack(anchor=W)

# gui-08 通过循环创建多个radio button
# v = IntVar()
# v.set(1)  # initializing the choice, i.e. Python

# languages = [
#     ("Python",1),
#     ("Perl",2),
#     ("Java",3),
#     ("C++",4),
#     ("C",5)
# ]

# def ShowChoice():
#     print(v.get())

# Label(root, 
#       text="""Choose your favourite 
# programming language:""",
#       justify = LEFT,
#       padx = 20).pack()

# for e in languages:
# 	Radiobutton(root,
# 		text=e[0],
# 		padx=20,
# 		variable=v,
# 		command=ShowChoice,
# 		value=e[1]).pack(anchor=W)

# gui-09 条状的radio button
# Label(root,
# 	text = 'Choose your favorite programming language:',
# 	justify = LEFT,
# 	padx = 40
# 	).pack()

# v = IntVar()
# v.set(1)

# textValues = [
# 	('Python',1),
# 	('C++',2),
# 	('Java',3),
# 	('C',4),
# ]

# for txtVal in textValues:
# 	Radiobutton(root,
# 		text = txtVal[0],
# 		value = txtVal[1],
# 		variable = v,
# 		indicatoron = 0,
# 		width = 20,
# 		padx = 20
# 		).pack()

# gui-10 checkbox
# var1 = IntVar()
# Checkbutton(root, text='male', variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(root, text='female', variable=var2).grid(row=1, sticky=W)

# gui-11 checkbox
# var1 = IntVar()
# var2 = IntVar()
# def var_states():
# 	print('male: {}\nfemale: {}'.format(var1.get(), var2.get()))
# Label(root, text='Your sex:').grid(row=0, sticky=W)
# Checkbutton(root, text='male', variable=var1).grid(row=1, sticky=W)
# Checkbutton(root, text='female', variable=var2).grid(row=2, sticky=W)
# Button(root, text='Quit', command=root.quit).grid(row=3, sticky=W, pady=4)
# Button(root, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)

# gui-12 checkbox
# class Checkbar(Frame):
# 	def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
# 		Frame.__init__(self, parent)
# 		self.vars = []
# 		for pick in picks:
# 			var = IntVar()
# 			chk = Checkbutton(self, text=pick, variable=var)
# 			chk.pack(side=side, anchor=anchor, expand=YES)
# 			self.vars.append(var)
# 	def state(self):
# 		return map((lambda var : var.get()), self.vars)

# lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
# tgl = Checkbar(root, ['English', 'German'])
# lng.pack(side=TOP, fill=X)
# tgl.pack(side=LEFT)
# lng.config(relief=GROOVE, bd=2)

# def allstates():
# 	print(list(lng.state()), list(tgl.state()))

# Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
# Button(root, text='Peek', command=allstates).pack(side=RIGHT)

# gui-12 entry 输入控件
# Label(root, text='First Name').grid(row=0)
# Label(root, text='Last Name').grid(row=1)
# e1 = Entry(root)
# e1.grid(row=0, column=1)
# Entry(root).grid(row=1, column=1)

# gui-13 获取输入框的值
# Label(root, text='First Name').grid(row=0)
# Label(root, text='Last Name').grid(row=1)

# e1 = Entry(root)
# e1.grid(row=0, column=1)
# e1.insert(0,'Mendel') #插入值

# e2 = Entry(root)
# e2.grid(row=1, column=1)

# def show_entry_fields():
# 	print('First Name: {}\nLast Name: {}'.format(e1.get(), e2.get()))

# def clear_entry_fields():
# 	e1.delete(0)
# 	e2.delete(0,END)

# Button(root, text='Quit', command=root.quit).grid(row=3, column=0, sticky=W, pady=4)
# Button(root, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
# Button(root, text='Clear', command=clear_entry_fields).grid(row=3, column=2, sticky=W, pady=4)

# gui-14 通过循环创建多个控件
# fields = 'Last Name', 'First Name', 'Job', 'Country'

# def fetch(entries):
# 	for entry in entries:
# 		field = entry[0]
# 		text = entry[1].get()
# 		print('{}: {}'.format(field, text))

# def makeform(root, fields):
# 	entries = []
# 	for field in fields:
# 		row = Frame(root)
# 		lab = Label(row, width=15, text=field, anchor='w')
# 		ent = Entry(row)
# 		row.pack(side=TOP, fill=X, padx=5, pady=5)
# 		lab.pack(side=LEFT)
# 		ent.pack(side=RIGHT, expand=YES, fill=X)
# 		entries.append((field, ent))
# 	return entries

# ents = makeform(root, fields)
# root.bind('<Return>', (lambda event, e=ents: fetch(e)))
# b1 = Button(root, text='Show', command=(lambda e=ents: fetch(e)))
# b1.pack(side=LEFT, padx=5, pady=5)
# b2 = Button(root, text='Quit', command=root.quit)
# b2.pack(side=LEFT, padx=5, pady=5)

# gui-15 简易计算器
# def calc(event):
# 	res.configure(text=str(eval(entry.get())))

# Label(root, text='结果为:').pack()

# res = Label(root)
# res.pack()

# entry = Entry(root)
# entry.pack()
# entry.bind('<Return>',calc)

# gui-16 canvas
# canvas_width = 80
# canvas_height = 40
# canvas = Canvas(root, width=canvas_width, height=canvas_height)
# canvas.pack()
# y = int(canvas_height/2)
# canvas.create_line(0, y, canvas_width, y, fill='green')

# gui-17 canvas
# canvas = Canvas(root, width=200, height=100, bg='red', bd=0)
# canvas.pack()
# canvas.create_rectangle(50,20,150,80, fill='#0f0')
# canvas.create_rectangle(65,35,135,65, fill='#ff0')
# canvas.create_line(0,0,50,20, fill='#476042', width=3)
# canvas.create_line(150,20,200,0, fill='#476042', width=3)
# canvas.create_line(0,100,50,80, fill='#476042', width=3)
# canvas.create_line(150,80,200,100, fill='#476042', width=3)

# gui-18 canvas text
# canvas_width = 200
# canvas_height = 100

# ratios = (0.2, 0.35)
# colors = ('#ff0', '#0f0')

# boxs = []
# for r in ratios:
# 	boxs.append((canvas_width*r, canvas_height*r, 
# 		canvas_width*(1-r), canvas_height*(1-r)) )

# canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='#f00')
# canvas.pack()

# for i,box in enumerate(boxs):
# 	canvas.create_rectangle(box[0],box[1],box[2],box[3], fill=colors[i])

# canvas.create_line(0,0, boxs[0][0], boxs[0][1], fill='#0f0', width=3)
# canvas.create_line(0,canvas_height, boxs[0][0], boxs[0][3], fill='#0f0', width=3)
# canvas.create_line(boxs[0][2],boxs[0][1], canvas_width, 0, fill='#0f0', width=3)
# canvas.create_line(boxs[0][2],boxs[0][3], canvas_width, canvas_height, fill='#0f0', width=3)

# canvas.create_text(canvas_width/2, canvas_height/2, text='Python')

# gui-19 canvas oval
# canvas = Canvas(root, width=200, height=100, bg='#f00')
# canvas.pack()
# # canvas.create_oval(50,20,150,80, fill='#0f0')
# canvas.create_oval(50,20,150,80, outline='#0f0', width=3)

# gui-20 canvas mouse paint
# canvas_width = 500
# canvas_height = 100
# def paint(event):
# 	x1, y1 = event.x-1, event.y-1
# 	x2, y2 = event.x+1, event.y+1
# 	canvas.create_oval(x1,y1,x2,y2, fill='#000')

# canvas = Canvas(root, width=canvas_width, height=canvas_height)
# canvas.bind('<B1-Motion>', paint)

# message = Label(root, text='Press and Drag the mouse to draw')

# root.title('Painting using Ovals')
# canvas.pack(expand=YES, fill=BOTH)
# message.pack(side=BOTTOM)

# gui-21 canvas
# canvas_width = 200
# canvas_height = 200
# canvas = Canvas(root, width=canvas_width, height=canvas_height)
# canvas.pack()
# points = [0,0, canvas_width,canvas_height/2, 0,canvas_height]
# canvas.create_polygon(points, outline='#00f', width=3, fill='#ff0')

# gui-22 canvas paint star
# canvas_width = 400
# canvas_height =400
# python_green = "#476042"
# p = 20
# t = 5
# def paint_star(canvas,x,y,p,t, outline=python_green, fill='#ff0', width=1):
# 	points = []
# 	for i in (1,-1):
# 		points.extend((x, y+i*p))
# 		points.extend((x+i*t, y+i*t))
# 		points.extend((x+i*p, y))
# 		points.extend((x+i*t, y-i*t))
# 	canvas.create_polygon(points, outline=outline, width=3, fill=fill)

# canvas = Canvas(root, width=canvas_width, height=canvas_height)
# canvas.pack()
# nsteps = 10
# dist = canvas_width/nsteps
# for i in range(1,nsteps):
# 	paint_star(canvas, i*dist, i*dist, p, t)
# 	paint_star(canvas, i*dist, canvas_height-i*dist, p, t)

# gui-23 Bitmaps
# canvas_width = 300
# canvas_height = 80
# canvas = Canvas(root,width=canvas_width,height=canvas_height)
# canvas.pack()

# bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", 
# "hourglass", "info", "questhead", "question", "warning"]
# nsteps = len(bitmaps)
# step_x = int(canvas_width/nsteps)
# for i in range(0,nsteps):
# 	canvas.create_bitmap(i*step_x+step_x/2,50,bitmap=bitmaps[i])

# gui-24 The Canvas method create_image(x0,y0, options ...) is used to draw an image on a canvas. create_image doesn't accept an image directly. It uses an object which is created by the PhotoImage() method. 
# The PhotoImage class can only read GIF and PGM/PPM images from files
# canvas = Canvas(root,width=300,height=300)
# canvas.pack()
# img = PhotoImage(file="../images/timg.gif")
# canvas.create_image(10,10,anchor=NW,image=img)

# gui-25 画方格
# canvas_width = 200
# canvas_height = 100
# def checkered(canvas,line_distance):
# 	for x in range(line_distance,canvas_width,line_distance):
# 		canvas.create_line(x,0,x,canvas_height,fill='#000')
# 	for y in range(line_distance,canvas_height,line_distance):
# 		canvas.create_line(0,y,canvas_width,y,fill='#000')

# canvas = Canvas(root,width=canvas_width,height=canvas_height)
# canvas.pack()
# checkered(canvas,10)

# gui-26 slider
# s1 = Scale(root,from_=0,to=24)
# s1.pack()
# s2 = Scale(root,from_=0,to=200,orient=HORIZONTAL)
# s2.pack()

# gui-27 获取slider的值
# s1 = Scale(root,from_=0,to=24)
# s1.pack()
# s2 = Scale(root,from_=0,to=200,orient=HORIZONTAL)
# s2.pack()
# def show_values():
# 	print(s1.get(),s2.get())
# 	print(type(s1.get()))
# Button(root,text='View value',command=show_values).pack()


# gui-28 位slider设置初值
# s1 = Scale(root,from_=0,to=24)
# s1.set(10)
# s1.pack()

# s2 = Scale(root,from_=0,to=200,orient=HORIZONTAL)
# s2.set(100)
# s2.pack()

# def show_values():
# 	print(s1.get(),s2.get())
# 	print(type(s1.get()))
# Button(root,text='View value',command=show_values).pack()

# gui-29 位slider设置初值，刻度间隔，长度
# s1 = Scale(root,from_=0,to=24,tickinterval=8)
# s1.set(10)
# s1.pack()

# s2 = Scale(root,from_=0,to=200,tickinterval=10,length=600,orient=HORIZONTAL)
# s2.set(100)
# s2.pack()

# def show_values():
# 	print(s1.get(),s2.get())
# 	print(type(s1.get()))
# Button(root,text='View value',command=show_values).pack()

# gui-30 Text
# A text widget is used for multi-line text area. The Tkinter text widget is very 
# powerful and flexible and can be used for a wide range of tasks. 
# Though one of the main purposes is to provide simple multi-line areas, 
# as they are often used in forms, 
# text widgets can also be used as simple text editors or even web browsers. 
# T = Text(root,height=2,width=30) #注意height以行为单位
# T.pack()
# T.insert(END, 'Just a text widget\nThere are two lines')

# gui-31 带滚动条的Text
# t = Text(root,height=4,width=40)
# s = Scrollbar(root)
# t.pack(side=LEFT,fill=Y)
# s.pack(side=RIGHT,fill=Y)
# t.config(yscrollcommand=s.set)
# s.config(command=t.yview)
# quote='''HAMLET: To be, or not to be--that is the question:
# Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune
# Or to take arms against a sea of troubles
# And by opposing end them. To die, to sleep--
# No more--and by a sleep to say we end
# The heartache, and the thousand natural shocks
# That flesh is heir to. 'Tis a consummation
# Devoutly to be wished.'''
# t.insert(END,quote)

# gui-32 带两个滚动条的Text
# t = Text(root,height=4,width=40,wrap=NONE)
# s = Scrollbar(root)
# s2 = Scrollbar(root,orient=HORIZONTAL)
# s.pack(side=RIGHT,fill=Y)
# s2.pack(side=BOTTOM,fill=X)
# t.pack(side=LEFT,fill=BOTH,expand=1)
# t.config(yscrollcommand=s.set)
# t.config(xscrollcommand=s2.set)
# s.config(command=t.yview)
# s2.config(command=t.xview)
# quote='''HAMLET: To be, or not to be--that is the question:
# Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune
# Or to take arms against a sea of troubles
# And by opposing end them. To die, to sleep--
# No more--and by a sleep to say we end
# The heartache, and the thousand natural shocks
# That flesh is heir to. 'Tis a consummation
# Devoutly to be wished.'''
# t.insert(END,quote)

# gui-33
# text1 = Text(root, height=20, width=30)
# photo=PhotoImage(file='../images/shakespare.gif')
# text1.insert(END,'\n')
# text1.image_create(END, image=photo)

# text1.pack(side=LEFT)

# text2 = Text(root, height=20, width=50)
# scroll = Scrollbar(root, command=text2.yview)
# text2.configure(yscrollcommand=scroll.set)
# text2.tag_configure('big', font=('Verdana', 20, 'bold'))
# text2.tag_configure('color', foreground='#476042', 
# 						font=('Tempus Sans ITC', 12, 'bold'))

# text2.insert(END,'\nWilliam Shakespeare\n', 'big')
# quote = """
# To be, or not to be that is the question:
# Whether 'tis Nobler in the mind to suffer
# The Slings and Arrows of outrageous Fortune,
# Or to take Arms against a Sea of troubles,
# """
# text2.insert(END, quote, 'color')

# # text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
# def cb(e):
# 	text2.insert(END, "Not now, maybe later!")
# 	print(e)
# text2.tag_bind('follow', '<1>', cb)
# text2.insert(END, 'follow-up\n', 'follow')
# text2.pack(side=LEFT)
# scroll.pack(side=RIGHT, fill=Y)

# gui-34 dialog
# from tkinter.messagebox import * #旧版的模块名为tkMessageBox 
# def answer():
# 	r = showerror('Answer','Sorry, no answer available')
# 	print(r)
# 	print(type(r))

# def callback():
# 	if askyesno('Verify','Really quit?'):
# 		r = showwarning('Yes','Not yet implemented')
# 	else:
# 		r = showinfo('No','Quit has been cancelled')

# Button(text='Quit',command=callback).pack(fill=X)
# Button(text='Answer',command=answer).pack(fill='x')

# gui-35 文件对话框
# import tkinter.filedialog
# def callback():
# 	path = tkinter.filedialog.askopenfilename()
# 	print(path)
# def callback2():
# 	pass
# 	path = tkinter.filedialog.asksaveasfilename()
# 	print(path)
# Button(text='File open',command=callback).pack(fill=X)
# Button(text='File save',command=callback2).pack(fill=X)

# gui-36 颜色对话框
# import tkinter.colorchooser
# def callback():
# 	color = tkinter.colorchooser.askcolor()
# 	print(color)
# Button(text='Choose color',command=callback).pack()

# gui-37 layout 布局
# Label(root,text='Red Sun',bg='red',fg='white').pack()
# Label(root,text='Green grass',bg='green',fg='white').pack()
# Label(root,text='Blue sky',bg='blue',fg='white').pack()


# gui-38 fill
# Label(root,text='Red Sun',bg='red',fg='white').pack(fill=X)
# Label(root,text='Green grass',bg='green',fg='white').pack(fill=X)
# Label(root,text='Blue sky',bg='blue',fg='white').pack(fill=X)

# gui-39 外边距 padx,pady
# Label(root,text='Red Sun',bg='red',fg='white').pack(fill=X,padx=10)
# Label(root,text='Green grass',bg='green',fg='white').pack(fill=X,padx=20)
# Label(root,text='Blue sky',bg='blue',fg='white').pack(fill=X,pady=20)

# gui-40 内边距 ipadx,ipady
# Label(root,text='Red Sun',bg='red',fg='white').pack()
# Label(root,text='Green grass',bg='green',fg='white').pack(ipadx=10)
# Label(root,text='Blue sky',bg='blue',fg='white').pack(ipady=10)

# gui-41 side
# Label(root,text='Red',bg='red',fg='white').pack(padx=5,pady=10,side=LEFT)
# Label(root,text='Green',bg='green',fg='white').pack(padx=5,pady=10,side=LEFT)
# Label(root,text='Blue',bg='blue',fg='white').pack(padx=5,pady=10,side=LEFT)

# gui-42 place布局
# import random
# # width x height + x_offset + y_offset:
# root.geometry('170x205+30+30')

# languages = ['python','Perl','C++','Java','Tcl/Tk']
# labels = range(5)
# for i in range(5):
# 	ct = [random.randrange(256) for x in range(3)]
# 	brightness = int(round(0.299*ct[0]+0.587*ct[1]+0.114*ct[2]))
# 	ct_hex = '{:02x}{:02x}{:02x}'.format(*ct)
# 	bg_color = '#'+''.join(ct_hex)
# 	l = Label(root,text=languages[i],fg='White' if brightness < 120 else 'black',
# 		bg=bg_color)
# 	l.place(x=25,y=30+i*30,width=120,height=25)

# gui-43 gird布局
# colors = ['red','orange','yellow','green','blue','white']
# for i in range(len(colors)):
# 	Label(root,text=colors[i],relief=RIDGE,width=15).grid(row=i,column=0)
# 	Entry(root,bg=colors[i],relief=SUNKEN,width=10).grid(row=i,column=1)

# gui-44 菜单
# import tkinter.filedialog
# import tkinter.messagebox

# def newFile():
# 	print("new File")
# def openFile():
# 	path = tkinter.filedialog.askopenfilename()
# 	print(path)
# def about():
# 	print(tkinter.messagebox.showinfo('about','by xxx'))

# menu = Menu(root)
# root.config(menu=menu)

# filemenu = Menu(menu)
# menu.add_cascade(label='File',menu=filemenu)
# filemenu.add_command(label='New',command=newFile)
# filemenu.add_command(label='Open...',command=openFile)
# filemenu.add_separator()
# filemenu.add_command(label='Exit',command=root.quit)

# helpmenu = Menu(menu)
# menu.add_cascade(label='help',menu=helpmenu)
# helpmenu.add_command(label='about',command=about)

# gui-45 事件
# def cb1(e):
# 	print('Button-1')

# def cb2(e):
# 	print('Double-1')

# button = Button(root, text='Click me')
# button.bind('<Button-1>', cb1)
# button.bind('<Double-1>', cb2)
# button.pack()

# gui-46 motion event
# top=root.winfo_toplevel()
# print(top is root)
# top.rowconfigure(0, weight=1)
# top.columnconfigure(0, weight=1)

# def cb1(e):
# 	print(e.__dict__)
# 	print('Mouse position: x={}, y={}'.format(e.x, e.y))

# str1 = 'To be or not to be. That is a question.'
# msg = Message(root, text=str1, bg='lightgreen')
# msg.bind('<Motion>', cb1)
# msg.grid(row=0, column=0, sticky=N+S+W)

# gui-47 显示其他格式的图片
# import PIL
# import PIL.Image,PIL.ImageTk

# image = PIL.Image.open('d:/html/images/1.jpg')
# image = PIL.ImageTk.PhotoImage(image)
# label_img = Label(root, image=image, width=300, height=200)
# label_img.grid(row=0, column=0)

# # gui-48 当图片太大时 出现滚动条
import PIL
import PIL.Image,PIL.ImageTk
import tkinter.filedialog

def image_from_path(path):
	return PIL.ImageTk.PhotoImage(PIL.Image.open(path))

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

input_label = Label(root, text='输入图像')
input_label.grid(row=0, column=0)

output_label = Label(root, text='输出图像')
output_label.grid(row=0, column=1)

in_img = image_from_path('d:/html/images/3.jpg')
input_img = Label(root, image=in_img, bd=2, bg='#fff')
input_img.grid(row=1, column=0, sticky=N+S+W+E)


out_img = image_from_path('d:/html/images/5.jpg')
output_img = Label(root, image=out_img, bd=2, bg='#fff')
output_img.grid(row=1, column=1, sticky=N+S+W+E)


def open_file():
	path = tkinter.filedialog.askopenfilename()
	print(path)
	in_img = image_from_path(path)
	input_img.configure(image=in_img, width=20, height=20)
	input_img.image = in_img #为什么不加这个显示不出来

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='打开...', command=open_file)
file_menu.add_separator()
file_menu.add_command(label='退出', command=root.quit)


root.mainloop()