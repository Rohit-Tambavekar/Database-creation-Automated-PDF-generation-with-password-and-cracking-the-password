#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# install pyscopg2 
pip install psycopg2


# In[1]:


# import the psycopg2 module for PostgreSQL database connection
import psycopg2
# import pprint module to display the data in a pretty format
import pprint


# In[2]:


# connect to the PostgreSQL database using the credentials
conn = psycopg2.connect(host='localhost', user ='postgres',password='rayz',port=5432,database='abcBank')


# In[3]:


# create a cursor object to interact with the database
abc = conn.cursor()


# In[ ]:


# create a table in the database named client_details with four columns - id, name, DOB, and acc_no
abc.execute("create table client_details(id int,name varchar(50),DOB date NOT NULL, acc_no int);")


# In[ ]:


# commit the changes made to the database
conn.commit()


# In[ ]:


#Insert query
abc.execute("insert into client_details values(23,'Ravi','1996-12-12','112233')")


# In[ ]:


# commit the changes made to the database
conn.commit()


# In[ ]:


# insert a single row of data into the table using the INSERT query
abc.execute("insert into client_details values(24,'Manish','1995-11-10','124568'),(25,'Pratik','1993-03-07','325687'),(26,'Pallavi','1997-11-12','458965'),(27,'Pooja','1991-02-04','125978'),(28,'Rupesh','1989-01-18','659832'),(29,'Amit','1988-07-22','124578'),(30,'Rajesh','1996-08-30','235689'),(31,'Mary','1989-04-04','457889'),(32,'Sid','1999-05-20','457856'),(33,'Ahana','1985-01-11','895623'),(34,'Rutvi','1991-02-17','124589'),(35,'Aravind','1990-03-21','567812'),(36,'Shreyas','1986-04-02','234589'),(37,'Tanvi','1984-05-03','234556'),(38,'Chintan','1988-06-08','128797'),(39,'Marco','1997-07-29','985435')")


# In[ ]:


# commit the changes made to the database
conn.commit()


# In[4]:


# select the name column data from the table using the SELECT query
abc.execute("select name from client_details")
# fetch all the rows returned by the SELECT query
x=abc.fetchall()
# create an empty Python list named client_list
client_list=[]
# iterate over the fetched rows and append the name data to the client_list
for i in x:
    client_list.append(*i)


# In[5]:


# print the client_list to display the name data fetched from the table
client_list


# In[ ]:




