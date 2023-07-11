import tkinter as tk
from tkinter import filedialog
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def browse_image():
    """Function to browse for an image file"""
    filename = filedialog.askopenfilename(initialdir="/", title="Select an Image",
                                          filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png")))
    if filename:
        image_path.set(filename)

def generate_pdf():
    """Function to generate the PDF"""
    # get the table data from the entries
    data = [[name_entry.get(), age_entry.get(), gender_entry.get()],
            [name_entry2.get(), age_entry2.get(), gender_entry2.get()],
            [name_entry3.get(), age_entry3.get(), gender_entry3.get()]]

    # create the table as a Table object
    table = Table(data)

    # add style to the table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ]))

    # create the PDF file
    doc = SimpleDocTemplate("example.pdf", pagesize=letter)

    # add the image to the PDF
    image = Image.open(image_path.get())
    img_width, img_height = image.size
    aspect_ratio = img_height / float(img_width)
    image = Image.open(image_path.get()).resize((400, int(400*aspect_ratio)))
    image.save("resized_image.jpg")
    table_and_image = [table, Image("resized_image.jpg", width=400, height=int(400*aspect_ratio))]

    doc.build(table_and_image)

# create the GUI
root = tk.Tk()
root.title("PDF Generator")

# create the table inputs
tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Age").grid(row=0, column=1)
tk.Label(root, text="Gender").grid(row=0, column=2)

name_entry = tk.Entry(root)
age_entry = tk.Entry(root)
gender_entry = tk.Entry(root)

name_entry2 = tk.Entry(root)
age_entry2 = tk.Entry(root)
gender_entry2 = tk.Entry(root)

name_entry3 = tk



class App:
    def __init__(self, master):
        self.master = master
        master.title("PDF Generator")

        # create widgets for input
        tk.Label(master, text="Name").grid(row=0, column=0)
        tk.Label(master, text="Age").grid(row=1, column=0)
        tk.Label(master, text="Gender").grid(row=2, column=0)
        tk.Button(master, text="Upload Image", command=self.upload_image).grid(row=3, column=0)

        self.name_entry = tk.Entry(master)
        self.age_entry = tk.Entry(master)
        self.gender_entry = tk.Entry(master)

        self.name_entry.grid(row=0, column=1)
        self.age_entry.grid(row=1, column=1)
        self.gender_entry.grid(row=2, column=1)

        # create button to generate PDF
        tk.Button(master, text="Generate PDF", command=self.generate_pdf).grid(row=4, column=0, columnspan=2)

    def upload_image(self):
        # open file dialog to choose image file
        file_path = filedialog.askopenfilename(initialdir="./", title="Select Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        self.image_path = file_path

    def generate_pdf(self):
        # get data from input
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()

        # create the table data as a list of lists
        data = [['Name', 'Age', 'Gender'],
                [name, age, gender]]

        # create the table as a Table object
        table = Table(data)

        # add style to the table
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ]))

        # create the PDF file
        doc = SimpleDocTemplate("example.pdf", pagesize=letter)
        flowables = []

        # add image to the flowables list
        if hasattr(self, 'image_path'):
            img = Image(self.image

