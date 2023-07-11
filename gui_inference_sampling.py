
# from ast import If
# import tkinter
import os
from pathlib import Path
# from tkinter import ttk
# from tkinter import messagebox
# # from tkinter.tix import Tree
# from turtle import width

# buttonClicked = False

# log_inference = Path(os.getcwd() + '/log_inference_sampling')
# log_inference.mkdir(parents=True, exist_ok=True)  # make dir

# # no_tiket_entry = 'haha'

# def save_info_truk(header, log_inference):
#     header_str = str(header) + '\n'
#     file_path = log_inference + '/log.TXT'
#     if not os.path.exists(log_inference):
#         os.makedirs(log_inference)
#     if not os.path.exists(file_path):
#         f = open(file_path, "a")
#         f.write("")
#         f.close()
#     with open(file_path, 'r') as z:
#         content = z.readlines()
#         wr = open(file_path, "a")
#         try:
#             if len(content[0].strip()) == 0 | content[0] in ['\n', '\r\n']:
#                 wr.write(header_str)
#             else:
#                 wr.write(header_str)
#         except:
#             wr.write(header_str)
#         wr.close()



# window = tkinter.Tk()
# # window.geometry("600x250")
# window.title("Sistem Pos Grading AI Sampling SKM")

# # def prevPage():
# #     window.destroy()
# #     import list_truk_sampling


# frame = tkinter.Frame(window)
# frame.pack()


# def enter_data(tiket,plat, driver, unit, divisi, blok, status):
#     global log_inference
   
    
    
#     # plat = no_plat_entry
#     # driver = driver_entry
#     # unit = unit_entry
#     # divisi = divisi_entry
#     # blok = blok_entry
#     # status = status_entry

#     print(tiket)

#     # print("No Tiket: ", tiket, "No Plat: ", status)

#     save_info_truk(str(tiket) + ";" + str(plat)+ ";" + str(driver) + ";" + str(unit)+ ";" + str(divisi) + ";" + str(blok)+ ";" + str(status), str(log_inference))


# def clear_frame():
#     for widgets in frame.winfo_children():
#         widgets.destroy()
#     homepage()

# def homepage():
#     tree = ttk.Treeview(window)

#     tree['columns'] = ('plat_estate', 'cam', 'ramp', 'jjg', 'rp', 'ur', 'ov', 'eb', 'ab','tp','status')

#     for widgets in frame.winfo_children():
#         widgets.destroy()
#     btnHome = tkinter.Button(frame, text="Tambah Data", command=lambda: tambah(tree))
#     btnHome.grid(row=0, column=0, sticky="w")


  

#     # tree.column('#0',width=120, minwidth=25)
#     tree.column('plat_estate',width=120, minwidth=25)
#     tree.column('cam',width=120, minwidth=25)
#     tree.column('ramp' ,width=120, minwidth=25)
#     tree.column('jjg',width=120, minwidth=25)
#     tree.column('rp',width=120, minwidth=25)
#     tree.column('ur',width=120, minwidth=25)
#     tree.column('ov',width=120, minwidth=25)
#     tree.column('eb',width=120, minwidth=25)
#     tree.column('ab',width=120, minwidth=25)
#     tree.column('tp',width=120, minwidth=25)
#     tree.column('status',width=120, minwidth=25)
#     tree.pack()

#     # tree.heading('#0', text='No')
#     tree.heading('plat_estate', text='Plat & Estate')
#     tree.heading('cam', text='Camera')
#     tree.heading('ramp' , text='Loading Ramp')
#     tree.heading('jjg', text='Total Janjang')
#     tree.heading('rp', text='RP')
#     tree.heading('ur', text='UR')
#     tree.heading('ov', text='OV')
#     tree.heading('eb', text='EB')
#     tree.heading('ab', text='AB')
#     tree.heading('tp', text='TP')
#     tree.heading('status', text='Status Data')

#     print('ini homepage')

    

# def tambah(x):
#     # print(x)
#     # x.delete(*x.get_children())

#     # naise = x
#     # curItem = naise.focus()
#     # print(naise.item(curItem))
#     # # for i in x.get_children():
#     # #     x.delete(i)
#     for widgets in frame.winfo_children():
#         print(widgets)
#         widgets.destroy()
#     # for col in x['columns']:
#     #     x.heading(col, text='')
#     # x.delete(*x.get_children())
    
    
#     print('ini halaman tambah data')
#     button = tkinter.Button(frame, text="Kembali", command=clear_frame)
#     button.grid(row=0, column=0, sticky="w", padx=20, pady=10)
#     # Saving User Info
#     user_info_frame =tkinter.LabelFrame(frame, text="Form Informasi Truk")
#     user_info_frame.grid(row= 1, column=0, padx=20, pady=10)

#     no_tiket_label = tkinter.Label(user_info_frame, text="No Tiket")
#     no_tiket_label.grid(row=1, column=0)
#     no_plat_label = tkinter.Label(user_info_frame, text="No Plat")
#     no_plat_label.grid(row=1, column=1)
#     driver_label = tkinter.Label(user_info_frame, text="Nama Driver")
#     driver_label.grid(row=1, column=2)
#     unit_label = tkinter.Label(user_info_frame, text="Bisnis Unit")
#     unit_label.grid(row=1, column=3)
#     divisi = tkinter.Label(user_info_frame, text="Divisi")
#     divisi.grid(row=3, column=0)
#     blok = tkinter.Label(user_info_frame, text="Blok")
#     blok.grid(row=3, column=1)
#     status = tkinter.Label(user_info_frame, text="Status")
#     status.grid(row=3, column=2)

#     no_tiket_entry = tkinter.Entry(user_info_frame)
#     no_plat_entry = tkinter.Entry(user_info_frame)
#     driver_entry = tkinter.Entry(user_info_frame)
#     unit_entry = tkinter.Entry(user_info_frame)
#     divisi_entry = tkinter.Entry(user_info_frame)
#     blok_entry = tkinter.Entry(user_info_frame)
#     status_entry = ttk.Combobox(user_info_frame, values=["Inti", "Eksternal"])


#     no_tiket_entry.grid(row=2, column=0)
#     no_plat_entry.grid(row=2, column=1)
#     driver_entry.grid(row=2, column=2)
#     unit_entry.grid(row=2, column=3)
#     divisi_entry.grid(row=4, column=0)
#     blok_entry.grid(row=4, column=1)
#     status_entry.grid(row=4, column=2,)

#     # if buttonClicked == True:
#     #     print('dipencet ' + no_tiket_entry.get())
#     # else:
#     #     print('belum dipencet')
    
#     button = tkinter.Button(frame, text="Enter data", command=lambda:  enter_data(no_tiket_entry.get(), no_plat_entry.get(), driver_entry.get(), unit_entry.get(), divisi_entry.get(), blok_entry.get(), status_entry.get()))
#     button.grid(row=4, column=0, sticky="news", padx=20, pady=10)



# homepage()
# window.mainloop()



# from tkinter import *
# from tkinter import ttk


# class app:
#     def __init__(self, master):
#         self.master = master
#         self.master.geometry("200x200")
#         self.login()
    
#     def login(self):
#         for i in self.master.winfo_children():
#             i.destroy()
#         self.frame1 = Frame(self.master, width=300, height=300)
#         self.frame1.pack()
#         self.reg_txt = ttk.Label(self.frame1, text='Ini halaman homepage')
#         self.reg_txt.pack()
#         self.register_btn = ttk.Button(self.frame1, text="Tambah", command=self.register)
#         self.register_btn.pack()
    
#     def register(self):
#         for i in self.master.winfo_children():
#             i.destroy()
#         self.frame2 = Frame(self.master, width=300, height=300)
#         self.frame2.pack()
#         self.reg_txt2 = ttk.Label(self.frame2, text='ini halaman tambah')
#         self.reg_txt2.pack()
#         self.login_btn = ttk.Button(self.frame2, text="Homepage", command=self.login)
#         self.login_btn.pack()

#         user_info_frame =ttk.LabelFrame(self.frame2, text="Form Informasi Truk")
#         user_info_frame.grid(row= 1, column=0, padx=20, pady=10)

#         no_tiket_label = ttk.Label(user_info_frame, text="No Tiket")
#         no_tiket_label.grid(row=1, column=0)

# root = Tk()
# app(root)
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# root = tk.Tk()
# root.title('Treeview demo')
# root.geometry('620x200')

# # define columns
# columns = ('first_name', 'last_name', 'email')

# tree = ttk.Treeview(root, columns=columns, show='headings')

# # define headings
# tree.heading('first_name', text='First Name')
# tree.heading('last_name', text='Last Name')
# tree.heading('email', text='Email')

# # generate sample data
# contacts = []
# for n in range(1, 100):
#     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# # add data to the treeview
# for contact in contacts:
#     tree.insert('', tk.END, values=contact)


# def item_selected(event):
#     for selected_item in tree.selection():
#         item = tree.item(selected_item)
#         record = item['values']
#         # show a message
#         showinfo(title='Information', message=','.join(record))


# tree.bind('<<TreeviewSelect>>', item_selected)

# tree.grid(row=0, column=0, sticky='nsew')

# # add a scrollbar
# scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.grid(row=0, column=1, sticky='ns')

# # run the app
# root.mainloop()

# ---------------------------------------------------------------------------------

import tkinter as tk
import string
from tkinter import ttk
from functools import partial
from tkinter.messagebox import YES, showinfo

log_inference = Path(os.getcwd() + '/log_inference_sampling')
log_inference.mkdir(parents=True, exist_ok=True)  # make dir
log_dir = Path(os.getcwd() + '/log_inference_sampling/log.TXT')

# no_tiket_entry = 'haha'

def save_info_truk(header, log_inference):
    header_str = str(header) + '\n'
    file_path = log_inference + '/log.TXT'
    if not os.path.exists(log_inference):
        os.makedirs(log_inference)
    if not os.path.exists(file_path):
        f = open(file_path, "a")
        f.write("")
        f.close()
    with open(file_path, 'r') as z:
        content = z.readlines()
        wr = open(file_path, "a")
        try:
            if len(content[0].strip()) == 0 | content[0] in ['\n', '\r\n']:
                wr.write(header_str)
            else:
                wr.write(header_str)
        except:
            wr.write(header_str)
        wr.close()

def statusRamp(no_line, status_ramp):

    print(no_line, status_ramp)
    # if os.path.exists(log_dir):
    #         with open(log_dir, 'r') as z:
    #             content = z.readlines()
    #             targetLine = content[no_line]
    #             wr = open(log_dir, "w")
                
    #             if(status_ramp == 'not_start'):
    #                 wr.write(targetLine.replace(status_ramp, 'started'))

    #             if(status_ramp == 'started'):
    #                 wr.write(targetLine.replace(status_ramp, 'stop'))

    #             wr.close()

                
                    

def enter_data(tiket,plat, driver, unit, divisi, blok, status):

#     global log_inference
    
    # plat = no_plat_entry
    # driver = driver_entry
    # unit = unit_entry
    # divisi = divisi_entry
    # blok = blok_entry
    # status = status_entry

    print(tiket)

    # print("No Tiket: ", tiket, "No Plat: ", status)

    # if(tiket != '' and plat != '' and driver != '' and unit != '' and blok != '' and status !=''):
    #     save_info_truk(' ; ; ; ; ; ;', str(log_inference))    
    # else:
    save_info_truk(str(tiket) + ";" + str(plat)+ ";" + str(driver) + ";" + str(unit)+ ";" + str(divisi) + ";" + str(blok)+ ";" + str(status) +';not_start', str(log_inference))

 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self)
        self.winfo_toplevel().title("Sistem Pos Grading Sampling AI SKM")
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Homepage, HalamanTambah):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Homepage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class Homepage(tk.Frame):
    global log_dir
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
  
        button1 = ttk.Button(self, text ="Tambah Data",
        command = lambda : controller.show_frame(HalamanTambah))
     
        
        # using grid
        button1.grid(row = 0, column = 0,sticky='w', padx = 10, pady = 10)

        # button2 = ttk.Button(self, text ="coba",
        # command = lambda : controller.show_frame(HalamanTambah))
     
        # # using grid
        # button2.grid(row = 1, column = 1,sticky='w', padx = 10, pady = 10)


        columns =('no','plat_estate', 'cam', 'ramp', 'jjg', 'rp', 'ur', 'ov', 'eb', 'ab','tp','status')

        s = ttk.Style()
        s.configure('Treeview', rowheight=35) # repace 40 with whatever you need
        s.configure("BW.TLabel", background="GREEN", relief="flat")
        
        tree = ttk.Treeview(self, columns=columns, show='headings')

        tree.column('no',width=50, minwidth=25, stretch=YES)
        tree.column('plat_estate',width=120, minwidth=25)
        tree.column('cam',width=120, minwidth=25)
        tree.column('ramp' ,width=120, minwidth=25)
        tree.column('jjg',width=120, minwidth=25)
        tree.column('rp',width=120, minwidth=25)
        tree.column('ur',width=120, minwidth=25)
        tree.column('ov',width=120, minwidth=25)
        tree.column('eb',width=120, minwidth=25)
        tree.column('ab',width=120, minwidth=25)
        tree.column('tp',width=120, minwidth=25)
        tree.column('status',width=120, minwidth=25)

        # define headings
        tree.heading('no', text='No')
        tree.heading('plat_estate', text='Plat & Estate')
        tree.heading('cam', text='Camera')
        tree.heading('ramp' , text='Loading Ramp')
        tree.heading('jjg', text='Total Janjang')
        tree.heading('rp', text='RP')
        tree.heading('ur', text='UR')
        tree.heading('ov', text='OV')
        tree.heading('eb', text='EB')
        tree.heading('ab', text='AB')
        tree.heading('tp', text='TP')
        tree.heading('status', text='Status Data')

        if os.path.exists(log_dir):
            with open(log_dir, 'r') as z:
                content = z.readlines()

                # print(content[0]) 

                no_line = -1
                count = 0
                arrData = []
                defX = 315
                defY = 68
                btn = ''
                for line in content:

                    count += 1
                    no_line += 1
                    lenString = len(line.split(';'))
                    strStatus = line.split(';')[lenString - 1]  
                    strRemoveUnderScore = strStatus.replace("_", " ")
                    
                    btn = ttk.Button(self, text =string.capwords(strRemoveUnderScore), style='BW.TLabel', command= partial(statusRamp, no_line, line.split(';')[6]))
                    
                    btn.place(x = defX, y = defY)

                    #split data kemudian masukkan
                    arrData.append((count,line.split(';')[0] + ' ' + line.split(';')[4],'', ''))
                    # print(line.split(';'))
                    defY += 35
                   
                # print(arrData)
        # generate sample data  
        contacts = []
        for n in range(1, 100):
            contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))


        # print(contacts)


        # add data to the treeview
        for data in arrData:
            tree.insert('', tk.END, values=data)


        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                # show a message
                showinfo(title='Information', message=','.join(record))


        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=1, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')
  
          
  
  
# second window frame page1
# class Page1(tk.Frame):
     
#     def __init__(self, parent, controller):
         
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
#         label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
#         # button to show frame 2 with text
#         # layout2
#         button1 = ttk.Button(self, text ="StartPage",
#                             command = lambda : controller.show_frame(StartPage))
     
#         # putting the button in its place
#         # by using grid
#         button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
#         # button to show frame 2 with text
#         # layout2
#         button2 = ttk.Button(self, text ="Page 2",
#                             command = lambda : controller.show_frame(Page2))
     
#         # putting the button in its place by
#         # using grid
#         button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
# third window frame page2
class HalamanTambah(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        # label.grid(row = 0, column = 0, padx = 10, pady = 10)
        btnHome = ttk.Button(self, text="Kembali",  command = lambda : controller.show_frame(Homepage))
  
        btnHome.grid(row = 0, column = 0, sticky='w', padx = 10, pady = 10)

        user_info_frame =ttk.LabelFrame(self, text="Form Informasi Truk")
        user_info_frame.grid(row= 1, column=0, padx=20, pady=10)

        no_tiket_label = ttk.Label(user_info_frame, text="No Tiket")
        no_tiket_label.grid(row=1, column=0)
        no_plat_label = ttk.Label(user_info_frame, text="No Plat")
        no_plat_label.grid(row=1, column=1)
        driver_label = ttk.Label(user_info_frame, text="Nama Driver")
        driver_label.grid(row=1, column=2)
        unit_label = ttk.Label(user_info_frame, text="Bisnis Unit")
        unit_label.grid(row=1, column=3)
        divisi = ttk.Label(user_info_frame, text="Divisi")
        divisi.grid(row=3, column=0)
        blok = ttk.Label(user_info_frame, text="Blok")
        blok.grid(row=3, column=1)
        status = ttk.Label(user_info_frame, text="Status")
        status.grid(row=3, column=2)

        no_tiket_entry = ttk.Entry(user_info_frame)
        no_plat_entry = ttk.Entry(user_info_frame)
        driver_entry = ttk.Entry(user_info_frame)
        unit_entry = ttk.Entry(user_info_frame)
        divisi_entry = ttk.Entry(user_info_frame)
        blok_entry = ttk.Entry(user_info_frame)
        status_entry = ttk.Combobox(user_info_frame, values=["Inti", "Eksternal"])


        no_tiket_entry.grid(row=2, column=0)
        no_plat_entry.grid(row=2, column=1)
        driver_entry.grid(row=2, column=2)
        unit_entry.grid(row=2, column=3)
        divisi_entry.grid(row=4, column=0)
        blok_entry.grid(row=4, column=1)
        status_entry.grid(row=4, column=2,)

        # if buttonClicked == True:
        #     print('dipencet ' + no_tiket_entry.get())
        # else:
        #     print('belum dipencet')
        
        button = ttk.Button(self, text="Enter data", command=lambda:  enter_data(no_tiket_entry.get(), no_plat_entry.get(), driver_entry.get(), unit_entry.get(), divisi_entry.get(), blok_entry.get(), status_entry.get()))
        button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

  
        # button to show frame 3 with text
        # layout3
        # button2 = ttk.Button(self, text ="Startpage",
        #                     command = lambda : controller.show_frame(StartPage))
     
        # # putting the button in its place by
        # # using grid
        # button2.grid(row = 2, column = 0, padx = 10, pady = 10)

  
  
# Driver Code
app = tkinterApp()
app.mainloop()