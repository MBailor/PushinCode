
# Here I am importing sql3 and os
import sqlite3
import os
#
#   Python: 3.8.3
#
#   Author: Mark C. Bailor
#
#  Purpose: To write a script that will check a 
#           specific folder to determine if any
#           of the files contained within the folder
#           end with a '.txt' extenstion. If they 
#           do the script is to print the name and
#           corresponding modified time-stamp of
#           every file ending in said extension.S



# Here I use .connect create and/or call a database I would like to use
conec = sqlite3.connect('python_sql.db')

#Here I am calling the table I want, unless it doesnt exist in which case I have instructed the table to be created
with conec:
    curs = conec.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS tbl_txt( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        Data_String TEXT \
        )")
    conec.commit()
conec.close()

# Here I use .connect create and/or call a database I would like to use
conec = sqlite3.connect('python_sql.db')

# Here I am inputting a string I would like the computer to work with
fileList = ('\ninformation.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg\n')
String1 = ("\nThese are the files the the program will have to go through\
            \nand choose from it, just the text files.\n")
print(String1)
print(fileList)

# This is where I tell the computer how I want the string handled. I would like the return just the files that end
# in '.txt' and then I would like just those files entered into the table that was created above
with conec:
    curs = conec.cursor()
    text_files = [f for f in fileList if f.endswith('.txt')]
    curs.execute("INSERT INTO tbl_txt(Data_String) VALUES (?),(?)", \
                 (text_files))
    conec.commit()
conec.close()

# This is where I print the files that were commited to the table
String2 = ("\nThese are the files that were commited to the table.\n")
print(String2)
print(text_files)

