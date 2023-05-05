# Database-creation-Automated-PDF-generation-with-password-and-cracking-the-password

## **Introduction:**

The ABC Bank PDF Password Generator and Cracker is a project aimed at providing a secure and user-friendly way for clients of ABC Bank to generate and retrieve password-protected PDF documents containing their sensitive financial information. The project consists of three separate codes, each serving a unique purpose in the overall process.

### **`CreatePostgressAcc.py :`**

The first code file creates a database for ABC Bank and allows the user to input and retrieve client details. This database is an essential component of the project and is required for the remaining two codes to function correctly.

### **`CreatePDF.py :`**

The second code file uses the database created in CreatePostgressAcc.py to retrieve the names of ABC Bank clients. The user is prompted to input the name of the client for whom they wish to generate a password-protected PDF document. The code then generates a PDF file containing the random lorem sentences, with a password automatically generated based on the client's date of birth.

### **`CheckForPass.py :`**

The third code allows the user to attempt to crack the password of a password-protected PDF document. The user is prompted to input the name of the PDF file they wish to crack, and the code will search the user's computer for the file. If the file is found, the code will attempt to crack the password by iterating through all possible number combinations.

### **Installation:**

To use this project, the user must first download the code files and install Python 3.8 or higher. Additionally, the user must install the PyMuPDF and Pandas libraries.

### **Usage:**

To use the ABC Bank PDF Password Generator and Cracker, the user must first run CreatePostgressAcc.py to create the necessary database. After this step is complete, the user can run CreatePDF.py to generate a password-protected PDF document for a specific client, or CheckForPass.py to attempt to crack the password of an existing PDF document.

### **Limitations:**

While the ABC Bank PDF Password Generator and Cracker is a useful tool for ABC Bank clients, there are several limitations to the project. First, the project assumes that the user has access to the client's date of birth to generate the password. Second, the project only attempts to crack passwords consisting of numeric values. Finally, the project is only compatible with PDF documents that have been password-protected using the method employed in code 2.

### **Future Development:**

In the future, we plan to improve the ABC Bank PDF Password Generator and Cracker by adding additional password generation methods, such as using client-specific keywords, and expanding the password cracking capabilities to include non-numeric passwords. Additionally, we plan to develop a more user-friendly interface to make the project accessible to a wider range of users.


### **Conclusion:**

The ABC Bank PDF Password Generator and Cracker is a valuable tool for clients of ABC Bank who wish to protect their financial information while still having easy access to it. While there are limitations to the project, we believe that it is a useful and necessary addition to ABC Bank's suite of services. We welcome feedback and suggestions for future development and hope that this project will continue to evolve and improve in the years to come.
