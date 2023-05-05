#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install PyPDF4


# In[ ]:


pip install lorem


# In[ ]:


get_ipython().system('pip install reportlab')


# In[31]:


pip install docx


# In[32]:


pip install docx2pdf


# In[35]:


pip install --upgrade PyMuPDF


# In[2]:


import psycopg2
import fitz
import lorem
import io
import os
from reportlab.pdfgen.canvas import Canvas

# Connecting to the database
conn = psycopg2.connect(host='localhost', user='postgres', password='rayz', port=5432, database='abcBank')
abc = conn.cursor()

# Retrieving the list of client names from the database
abc.execute("SELECT name FROM client_details")
x = abc.fetchall()
client_list = []
print("Account Holder Names:\n")
for i in x:
    name = i[0]
    name_low = name.lower()
    print(name)
    client_list.append(name_low)

# Requesting input for client name and creating PDF if name is valid
while True:
    file_for_name = input("Input the name to create a PDF statement (or 'cancel' to exit)")
    if file_for_name.lower() == 'cancel' or file_for_name.lower() == 'exit':
        print("Exiting...")
        break
    if file_for_name.lower() in [name.lower() for name in client_list]:
        # Retrieving date of birth from the database for the client
        abc.execute(f"SELECT dob FROM client_details WHERE LOWER(name) = LOWER('{file_for_name}')")
        x = abc.fetchall()
        print(x)
        for dob in x:
            date_obj = dob[0]
            date_str = date_obj.strftime("%d%m")
            print(date_str)

            # Defining fonts
            font1 = "helv"
            font2 = "tiro"
            # Opening a blank PDF
            doc = fitz.open()
            # Creating a new empty page
            page = doc.new_page()
            # Defining the points and matrix for the text to be inserted
            point = fitz.Point(50, 50)
            point1 = fitz.Point(50, 60)
            point2 = fitz.Point(50, 70)
            matrix = fitz.Matrix(0)

            # Defining the permissions
            perm = int(
                fitz.PDF_PERM_ACCESSIBILITY  # always use this
                | fitz.PDF_PERM_PRINT  # permit printing
                | fitz.PDF_PERM_COPY  # permit copying
                | fitz.PDF_PERM_ANNOTATE  # permit annotations
            )
            owner_pass = date_str  # owner password
            user_pass = date_str  # user password
            encrypt_meth = fitz.PDF_ENCRYPT_AES_256  # strongest algorithm

            # Generating random sentences using the Lorem library
            sentence = lorem.sentence()
            sentence1 = lorem.sentence()
            sentence2 = lorem.sentence()

            # Inserting the text into the page
            page.insert_text(point, sentence, fontsize=11, fontname=font2, color=(0, 0, 0))
            page.insert_text(point1, sentence1, fontsize=11, fontname=font2, color=(0, 0, 0))
            page.insert_text(point2, sentence2, fontsize=11, fontname=font2, color=(0, 0, 0))

            # Saving the document with permissions and filename
            thisfile = os.path.abspath(f"C:\\Users\\Rayz\\Desktop\\PDFs\\{file_for_name}_secure_pdf.pdf")
            doc.save(
                thisfile,
                encryption=encrypt_meth,  # set the encryption method
                owner_pw=owner_pass,  # set the owner password
                user_pw=user_pass,  # set the user password
                permissions=perm,  # set permissions
            )
       


# In[6]:


import psycopg2
import fitz
import lorem
import io
import os
from reportlab.pdfgen.canvas import Canvas

class PDFGenerator:
    def __init__(self, host="localhost", user="postgres", password="rayz", port=5432, database="abcBank"):
        self.conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        self.abc = self.conn.cursor()

    def get_client_list(self):
        self.abc.execute("SELECT name FROM client_details")
        x = self.abc.fetchall()
        client_list = []
        print("Account Holder Names:\n")
        for i in x:
            name = i[0]
            name_low = name.lower()
            print(name)
            client_list.append(name_low)
        return client_list

    def generate_pdf(self):
        client_list = self.get_client_list()
        file_for_name = input("Input the name to create a PDF statement (or 'cancel' to exit)")
        if file_for_name.lower() == 'cancel' or file_for_name.lower() == 'exit':
            print("Exiting...")
            return
        if file_for_name.lower() in client_list:
            self.abc.execute(f"SELECT dob FROM client_details WHERE LOWER(name) = LOWER('{file_for_name}')")
            x = self.abc.fetchall()
            print(x)
            for dob in x:
                date_obj = dob[0]
                date_str = date_obj.strftime("%d%m")
                print(date_str)

                font1 = "helv"
                font2 = "tiro"

                doc = fitz.open()
                page = doc.new_page()
                point = fitz.Point(50, 50)
                point1 = fitz.Point(50, 60)
                point2 = fitz.Point(50, 70)
                matrix = fitz.Matrix(0)

                perm = int(
                    fitz.PDF_PERM_ACCESSIBILITY
                    | fitz.PDF_PERM_PRINT
                    | fitz.PDF_PERM_COPY
                    | fitz.PDF_PERM_ANNOTATE
                )
                owner_pass = date_str
                user_pass = date_str
                encrypt_meth = fitz.PDF_ENCRYPT_AES_256

                sentence = lorem.sentence()
                sentence1 = lorem.sentence()
                sentence2 = lorem.sentence()

                page.insert_text(point, sentence, fontsize=11, fontname=font2, color=(0, 0, 0))
                page.insert_text(point1, sentence1, fontsize=11, fontname=font2, color=(0, 0, 0))
                page.insert_text(point2, sentence2, fontsize=11, fontname=font2, color=(0, 0, 0))

                thisfile = os.path.abspath(f"C:\\Users\\Rayz\\Desktop\\PDFs\\{file_for_name}_secure_pdf.pdf")
                doc.save(
                    thisfile,
                    encryption=encrypt_meth,
                    owner_pw=owner_pass,
                    user_pw=user_pass,
                    permissions=perm,
                )


# In[7]:


pdf = PDFGenerator()


# In[8]:


pdf.generate_pdf()


# In[ ]:




