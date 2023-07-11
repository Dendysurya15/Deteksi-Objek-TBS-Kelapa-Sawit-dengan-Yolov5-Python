import tkinter as tk
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors

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
