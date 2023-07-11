
import os
from pathlib import Path
import time
import subprocess
import tkinter as tk
import string
from tkinter import ttk
from functools import partial
from tkinter.messagebox import YES, showinfo
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from tkinter import *
from tkinter import filedialog


log_inference = Path(os.getcwd() + '/log_inference_sampling')
log_inference.mkdir(parents=True, exist_ok=True)  # make dir
log_dir = Path(os.getcwd() + '/log_inference_sampling/log.TXT')

# no_tiket_entry = 'haha'

def save_info_truk(header, log_inference):
    header_str = str(header) 
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


                
                    

def enter_data(tiket,plat, driver, unit, divisi, blok, status):

#     global log_inference
    
    # plat = no_plat_entry
    # driver = driver_entry
    # unit = unit_entry
    # divisi = divisi_entry
    # blok = blok_entry
    # status = status_entry

    # print(tiket)

    # print("No Tiket: ", tiket, "No Plat: ", status)

    # if(tiket != '' and plat != '' and driver != '' and unit != '' and blok != '' and status !=''):
    #     save_info_truk(' ; ; ; ; ; ;', str(log_inference))    
    # else:
    save_info_truk(str(tiket) + ";" + str(plat)+ ";" + str(driver) + ";" + str(unit)+ ";" + str(divisi) + ";" + str(blok)+ ";" + str(status) +';Not Start', str(log_inference))

 
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

    # def refresh_gui(self):
    #     # update the widget display
    #     self.update()
  
# first window frame startpage
  
class Homepage(tk.Frame):
    global log_dir

    # def refresh_gui(self):
    #     # update the widget display
    #     self.update()
    #     # tkinterApp.update_idletasks()

    
    # def btnProccess(self,status, no_line,  koorX, koorY):

    #     button = ttk.Button(self, text=str(status) ,command=lambda id_button=no_line, title_button=str(status): self.updateDataBtn(str(status), title_button, id_button))            
    #     button.place(x = koorX, y = koorY)

    # def updateDataBtn(self,status, title_button, id_button ):

    #     if(status == 'Not Start'):
    #         self.buttons[id_button].config(text="Started")
            
    #     elif(status == 'Started'):
    #         self.buttons[id_button].config(text="Stop")
            
    #     elif(status == 'Stop'):
    #         self.buttons[id_button].config(text="Stop")
                        

    def statusRamp(self, id_button ,title_button, tree):
        
        # print(tree)

        # self.buttons[id_button].destroy()

        # self.btnProccess()

        

       
        # for row in tree.get_children():
        #         tree.delete(row)
        # time.sleep(10) 
        # pytonProcess = subprocess.check_output("ps -ef | grep python",shell=True).decode()
        # pytonProcess = pytonProcess.split('\n')
        
        # for process in pytonProcess:
        #     print(process)
        # print(number, state)


        # print(self.btn)
        # print(self.statusLodingRamp)

        # self.btn.config(text='good?')
        statusNew = title_button.replace("\n", "")
        # print(statusNew)
        no_line = id_button
        if(statusNew == 'Not Start'):
            os.popen('sh /home/grading/run_script_sampling.sh')
            if os.path.exists(log_dir):
                    with open(log_dir, 'r') as z:
                        content = z.readlines()
                        targetLine = content[no_line]
                        
                        wr = open(log_dir, "w")
                        content[no_line]  = targetLine.replace("Not Start", "Started;running")
                        self.buttons[id_button].config(text="Started")
                        wr.writelines(content)

                        # content[no_line] = ';running'
                        # wr.writelines(content)
                        wr.close()

                        # wAppend = open(log_dir, "a")
                        # content[no_line]  = ';running'
                        # wAppend.writelines(content)
                        # wAppend.close()
            
        # app.update()
        # newApp = tkinterApp()
        # newApp.mainloop()
        # tkinterApp.refresh_gui(self)

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
                self.buttons = []
                for line in content:

                    # print(line)
                    count += 1
                    no_line += 1
                    lenString = len(line.split(';'))
                    # print(lenString)
                    strStatus = line.split(';')[lenString - 1]
                    statusBtn = strStatus.replace('\n','')  
                    
                    # self.buttons.append(self.btnProccess(statusBtn,no_line, defX, defY))

                    # self.btn = ttk.Button(self, text =string.capwords(strRemoveUnderScore), style='BW.TLabel', command=lambda: self.statusRamp()) 
                    button = ttk.Button(self, text=str(statusBtn) ,command=lambda id_button=no_line, title_button=statusBtn: self.statusRamp(id_button, title_button, tree))
                    
                    button.place(x = defX, y = defY)

                    # print(line.split(';')[4])
                    self.buttons.append(button)

                    #split data kemudian masukkan
                    arrData.append((count,line.split(';')[1] + ' / ' + line.split(';')[3]  + ' ' + '', ''))
                    # print(line.split(';'))
                    defY += 35
                   
                # print(arrData)
        # generate sample data  
        # contacts = []
        # for n in range(1, 100):
        #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))


        # # print(contacts)


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

# def generate_report(filename):
#     # Create a canvas object
#     c = canvas.Canvas(filename, pagesize=A4)

#     # Add text to the canvas
#     c.drawString(100, 750, "Hello World")

#     # Save the PDF file
#     c.save()

# def export_report():
#     # Open a file dialog to select the export location
#     filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

#     # Generate the PDF report
#     generate_report(filename)

# root = Tk()
# root.title("Export PDF Report")

# # Add a button to export the PDF report
# export_button = Button(root, text="Export Report", command=export_report)
# export_button.pack()

# root.mainloop()