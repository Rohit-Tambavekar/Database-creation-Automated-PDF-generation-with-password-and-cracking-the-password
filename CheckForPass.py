#!/usr/bin/env python
# coding: utf-8

# In[21]:


import fitz, numpy as np, os, shutil

class PDFPasswordCracker:
    def __init__(self):
        self.doc_pass = np.arange(0,10000)
    
    def find_file(self, file_for_name):
        """
        Searches for a file in all available drives and returns its path
        """
        for drive in range(ord('A'), ord('Z') + 1):
            drive_letter = chr(drive)
            drive_path = os.path.join(drive_letter + ":", os.sep)
            if os.path.exists(drive_path):
                for root, dirs, files in os.walk(drive_path):
                    for file in files:
                        if file == file_for_name:
                            # If a file is found, return its location
                            file_path = os.path.join(root, file)
                            # Printing the file location
                            print(f"File {file} found at: {file_path}")
                            return file_path
        return None
    
    def crack_password(self, file_path):
        """
        Attempts to crack the password of a given PDF file
        """
        doc = fitz.open(file_path)
        if doc.needs_pass:
            for x in self.doc_pass:
                if len(str(x)) < 4:
                    x = str(x).zfill(4)  # add leading zeros to make it 4 digits
                if doc.authenticate(str(x)):
                    print(x)
                    print('User password authentication succeeded')
                    print('User password is: ', x)
                    return True
        else:
            print("No Authentication Required")
        return False
    
    def start(self):
        """
        Starts the PDF password cracking process by prompting the user for input
        """
        while True:
            file_for_name = input("Input the pdf name to crack the password on this PC(): ")
            
            # If user inputs 'cancel' or 'exit', terminate the program
            if file_for_name.lower() == 'cancel' or file_for_name.lower() == 'exit':
                print("Exiting...")
                break
            
            # Search for the file and get its absolute path
            file_path = self.find_file(file_for_name)
            if file_path is None:
                print(f"File {file_for_name} not found.")
                continue
                
            # Attempt to crack the password
            if self.crack_password(file_path):
                break


# In[22]:


cracker = PDFPasswordCracker()
cracker.start()


# In[ ]:




