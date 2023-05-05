
pip install --upgrade PyMuPDF

import psycopg2  # for database connection
import fitz  # for PDF manipulation
import lorem  # for generating placeholder text
import io  # for working with byte streams
import os  # for working with file paths

class PDFGenerator:
    def __init__(self, host="localhost", user="postgres", password="YourPasswordHere", port=5432, database="abcBank"):
        # establish a database connection
        self.conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        self.abc = self.conn.cursor()

    def get_client_list(self):
        # query the database to get a list of account holders
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
        # get the list of account holders and prompt the user for a name to create a PDF statement for
        client_list = self.get_client_list()
        file_for_name = input("Input the name to create a PDF statement (or 'cancel' to exit)")
        if file_for_name.lower() == 'cancel' or file_for_name.lower() == 'exit':
            print("Exiting...")
            return
        if file_for_name.lower() in client_list:
            # if the name entered matches an account holder, get their date of birth from the database
            self.abc.execute(f"SELECT dob FROM client_details WHERE LOWER(name) = LOWER('{file_for_name}')")
            x = self.abc.fetchall()
            print(x)
            for dob in x:
                date_obj = dob[0]
                date_str = date_obj.strftime("%d%m")
                print(date_str)

                font1 = "helv"  # font for the PDF
                font2 = "tiro"  # another font for the PDF

                # create a new PDF document and add a page to it
                doc = fitz.open()
                page = doc.new_page()

                # set the position and rotation of the text we will add
                point = fitz.Point(50, 50)
                point1 = fitz.Point(50, 60)
                point2 = fitz.Point(50, 70)
                matrix = fitz.Matrix(0)

                # set the permissions and encryption for the PDF
                perm = int(
                    fitz.PDF_PERM_ACCESSIBILITY
                    | fitz.PDF_PERM_PRINT
                    | fitz.PDF_PERM_COPY
                    | fitz.PDF_PERM_ANNOTATE
                )
                owner_pass = date_str  # use the date of birth as the owner password
                user_pass = date_str  # use the date of birth as the user password
                encrypt_meth = fitz.PDF_ENCRYPT_AES_256  # use AES 256-bit encryption

                # add some placeholder text to the PDF
                sentence = lorem.sentence()
                sentence1 = lorem.sentence()
                sentence2 = lorem.sentence()
                page.insert_text(point, sentence, fontsize=11, fontname=font2, color=(0, 0, 0))
                page.insert_text(point1, sentence1, fontsize=11, fontname=font2, color=(0, 0, 0))
                page.insert_text(point2, sentence2, fontsize=11, fontname=font2, color=(0, 0, 0))
                
                # define the abspath to thisfile variable, this is where the file will be saved
                thisfile = os.path.abspath(f"C:\\Users\\Rayz\\Desktop\\PDFs\\{file_for_name}_secure_pdf.pdf")
                # Save the file with permissions and passwords
                doc.save(
                    thisfile,
                    encryption=encrypt_meth,
                    owner_pw=owner_pass,
                    user_pw=user_pass,
                    permissions=perm,
                )



# initiate the class with pdf variable
pdf = PDFGenerator()
# initiate the function generate_pdf() to create the pdf with permissions and password
pdf.generate_pdf()

