import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import YES, showinfo
import os
from pathlib import Path


log_inference = Path(os.getcwd() + '/log_inference_sampling')
log_inference.mkdir(parents=True, exist_ok=True)  # make dir
log_dir = Path(os.getcwd() + '/log_inference_sampling/log.TXT')

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
    tiket = str(tiket)
    plat = str(plat)
    driver = str(driver)
    unit = str(unit)
    divisi = str(divisi)
    blok = str(blok)
    status = str(status)

    if tiket != '' and plat != '' and driver != '' and unit != '' and divisi != '' and blok != '' and status != '':
        save_info_truk(tiket + ";" + plat+ ";" + driver + ";" + unit+ ";" + divisi + ";" +blok+ ";" + status +';Not Start\n', str(log_inference))
    else:
        messagebox.showinfo("Warning !!!", "Semua Kolom Wajib Tidak Boleh Kosong")

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame1 = Frame1(self)
        self.frame2 = Frame2(self)
        self.current_frame = self.frame1
        self.current_frame.pack()

    def switch_frame(self, new_frame):
        self.current_frame.destroy()
        self.current_frame = new_frame(self)
        self.current_frame.pack()

class Frame1(tk.Frame):

    def statusRamp(self, id_button ,title_button, tree):
        
       
        statusNew = title_button.replace("\n", "")
        
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

                        wr.close()

        
    def __init__(self, master):
        super().__init__(master)
        self.button = tk.Button(self, text="Tambah Data",
                                 command=lambda: master.switch_frame(Frame2))
        self.button.grid(row= 0, column=0, sticky='w', padx=10, pady=10)


        
        
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

                    # self.btn = tk.Button(self, text =string.capwords(strRemoveUnderScore), style='BW.TLabel', command=lambda: self.statusRamp()) 
                    button = tk.Button(self, text=str(statusBtn) ,command=lambda id_button=no_line, title_button=statusBtn: self.statusRamp(id_button, title_button, tree))
                    
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
        scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')
       


class Frame2(tk.Frame):
    global log_dir

    def __init__(self, master):
        super().__init__(master)
        # self.label = tk.Label(self, text="This is Frame 2")
        # self.label.grid(row= 1, column=0, padx=20, pady=10)
        # self.button = tk.Button(self, text="Switch to Frame 1",
        #                          command=lambda: master.switch_frame(Frame1))
        # self.button.grid(row= 1, column=0, padx=20, pady=10)

        btnHome = tk.Button(self, text="Kembali",  command=lambda: master.switch_frame(Frame1))
  
        btnHome.grid(row = 0, column = 0, sticky='w', padx = 10, pady = 10)

        user_info_frame =tk.LabelFrame(self, text="Form Informasi Truk")
        user_info_frame.grid(row= 1, column=0, padx=20, pady=10)

        no_tiket_label = tk.Label(user_info_frame, text="No Tiket")
        no_tiket_label.grid(row=1, column=0)
        no_plat_label = tk.Label(user_info_frame, text="No Plat")
        no_plat_label.grid(row=1, column=1)
        driver_label = tk.Label(user_info_frame, text="Nama Driver")
        driver_label.grid(row=1, column=2)
        unit_label = tk.Label(user_info_frame, text="Bisnis Unit")
        unit_label.grid(row=1, column=3)
        divisi = tk.Label(user_info_frame, text="Divisi")
        divisi.grid(row=3, column=0)
        blok = tk.Label(user_info_frame, text="Blok")
        blok.grid(row=3, column=1)
        status = tk.Label(user_info_frame, text="Status")
        status.grid(row=3, column=2)

        no_tiket_entry = tk.Entry(user_info_frame)
        no_plat_entry = tk.Entry(user_info_frame)
        driver_entry = tk.Entry(user_info_frame)
        unit_entry = tk.Entry(user_info_frame)
        divisi_entry = tk.Entry(user_info_frame)
        blok_entry = tk.Entry(user_info_frame)
        status_entry = ttk.Combobox(user_info_frame, values=["Inti", "Eksternal"])


        no_tiket_entry.grid(row=2, column=0)
        no_plat_entry.grid(row=2, column=1)
        driver_entry.grid(row=2, column=2)
        unit_entry.grid(row=2, column=3)
        divisi_entry.grid(row=4, column=0)
        blok_entry.grid(row=4, column=1)
        status_entry.grid(row=4, column=2)

        # if buttonClicked == True:
        #     print('dipencet ' + no_tiket_entry.get())
        # else:
        #     print('belum dipencet')
        
        
        button = ttk.Button(self, text="Enter data", command=lambda:  enter_data(no_tiket_entry.get(), no_plat_entry.get(), driver_entry.get(), unit_entry.get(), divisi_entry.get(), blok_entry.get(), status_entry.get()))
        button.grid(row=4, column=0, sticky="news", padx=20, pady=10)


       

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()