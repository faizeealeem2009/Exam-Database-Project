import mysql.connector
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",user="root",password="bismillah",database="Exam"
    )

def init_db():
    try:
        conn=mysql.connector.connect(
            host="localhost",user="root",password="bismillah"
        )
        cursor=conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS Exam")
        cursor.execute("USE Exam")
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS students (
                roll_no INT PRIMARY KEY,
                name VARCHAR(100),
                gender VARCHAR(10),
                age INT,
                city VARCHAR(50),
                class VARCHAR(20),
                sub1 INT,
                sub2 INT,
                sub3 INT,
                sub4 INT,
                sub5 INT,
                sub6 INT
                )
            '''
        )
        conn.commit()
        cursor.execute("SHOW TABLES")
        for c in cursor.fetchall():
            print(c)
        conn.close()
        
    except mysql.connector.Error as err:
        messagebox.showerror(
            "Dabase Error",f"Failed to initialize database: {err}"
        )
        
init_db()

#Main Application Window
root=Tk()
root.title("Exam Management System")
root.geometry("400x300")

# FORM 1: ENTER STUDENT DATA
def open_form1():
    g=StringVar()
    F1=Toplevel(root)
    F1.title("Form 1 - Enter Student Data")
    #Labels and Entries
    Label(F1,text="Roll No:").grid(
        row=0,column=0,padx=5,pady=5,sticky="e"
    )
    e_roll=Entry(F1)
    e_roll.grid(row=0,column=1,padx=5,pady=5)

    Label(F1,text="Name:").grid(
        row=1,column=0,padx=5,pady=5,sticky="e"
    )
    e_name=Entry(F1)
    e_name.grid(row=1,column=1,padx=5,pady=5)

    Label(F1,text="Gender:").grid(
        row=2,column=0
    )
    
    e_gender1=Radiobutton(F1,variable=g,value="Male",text="Male")
    e_gender1.grid(row=2, column=1
    )

    e_gender2=Radiobutton(F1,variable=g,value="Female",text="Female")
    e_gender2.grid(row=3, column=1
    )

    Label(F1,text="Age:").grid(
        row=4,column=0,padx=5,pady=5,sticky="e"
    )
    e_age=Entry(F1)
    e_age.grid(row=4, column=1, padx=5, pady=5)

    Label(F1,text="City:").grid(
        row=5,column=0,padx=5,pady=5,sticky="e"
    )
    e_city=Entry(F1)
    e_city.grid(row=5, column=1, padx=5, pady=5)

    Label(F1, text="Class:").grid(         
        row=6, column=0, padx=5, pady=5, sticky="e"
             )     
    e_class=ttk.Combobox(F1,values=["5th","6th","7th","8th","9th","10th","11th","12th"],state="readonly")
    e_class.grid(row=6,column=1,padx=1,pady=5,columnspan=2,sticky="w")
    e_class.set("Select Class")
    
    Label(F1, text="Subject 1:").grid(
        row=7, column=0, padx=5, pady=5, sticky="e"
            )
    e_s1 = Entry(F1)     
    e_s1.grid(row=7, column=1, padx=5, pady=5) 
 
    Label(F1, text="Subject 2:").grid(
        row=8, column=0, padx=5, pady=5, sticky="e"     
            )
    e_s2 =Entry(F1)
    e_s2.grid(row=8, column=1, padx=5, pady=5) 
 
    Label(F1, text="Subject 3:").grid(
        row=9, column=0, padx=5, pady=5, sticky="e"     
            )     
    e_s3 =Entry(F1)     
    e_s3.grid(row=9, column=1, padx=5, pady=5) 
 
    Label(F1, text="Subject 4:").grid(
        row=10, column=0, padx=5, pady=5, sticky="e"     
            )     
    e_s4 =Entry(F1)     
    e_s4.grid(row=10, column=1, padx=5, pady=5)

    Label(F1, text="Subject 5:").grid(
        row=11, column=0, padx=5, pady=5, sticky="e"     
            )     
    e_s5 =Entry(F1)     
    e_s5.grid(row=11, column=1, padx=5, pady=5)

    Label(F1, text="Subject 6:").grid(
        row=12, column=0, padx=5, pady=5, sticky="e"     
            )     
    e_s6 =Entry(F1)     
    e_s6.grid(row=12, column=1, padx=5, pady=5)

    def save_data():
        try:
            conn=get_db_connection()
            cursor=conn.cursor()
            query='''INSERT INTO students
                    (roll_no,name,gender,age,city,class,sub1,sub2,sub3,sub4,sub5,sub6)
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)'''
            vals=(
                int(e_roll.get()),
                e_name.get(),
                e_gender1.get(),
                e_gender2.get(),
                int(e_age.get()),
                e_city.get(),
                e_class.get(),
                int(e_s1.get()),
                int(e_s2.get()),
                int(e_s3.get()),
                int(e_s4.get()),
                int(e_s5.get()),
                int(e_s6.get()),
            )
            cursor.execute(query,vals)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Students Saved Successfully!")
            F1.destroy()
        except Exception as e:
            messagebox.showerror("Error",f"Failed to save data: {e}")
    
    Button(F1,text="Save Student",command=save_data).grid(
        row=13,column=0,columnspan=2,padx=5,pady=5
    )

Button(root,text="Enter Student Data",width=30,command=open_form1).grid(row=0,column=0,pady=5)


# FORM 2: Display Student Data

def open_form2():
    F2=Toplevel(root)
    F2.title("Form 2 - Display Student Data")
    Label(F2,text="Enter Roll No:").grid(
        row=0,column=0,padx=5,pady=5,sticky="e"
    )
    e_search_roll=Entry(F2)
    e_search_roll.grid(row=0,column=1,padx=5,pady=5)

    #Frame to show Detais
    display_frame=Frame(F2)
    display_frame.grid(row=1,column=0,columnspan=2,pady=10)

    def search_student():
        for widget in display_frame.winfo_children():
            widget.destroy()
        try:
            conn=get_db_connection()
            cursor=conn.cursor()
            cursor.execute(
                "SELECT * FROM students WHERE roll_no=%s",
                (e_search_roll.get(),),
            )
            row=cursor.fetchone()
            conn.close()

            if row:
                labels=[
                    "Roll No",
                    "Name",
                    "Gender",
                    "Age",
                    "City",
                    "Class",
                    "Sub 1",
                    "Sub 2",
                    "Sub 3",
                    "Sub 4",
                    "Sub 5",
                    "Sub 6",
                ]
                for i in range(len(labels)):
                    Label(
                        display_frame,
                        text=f"{labels[i]}:",
                        font=("Arial", 10, "bold"),
                    ).grid(row=i, column=0, padx=5, pady=2, sticky="e")
                    Label(
                        display_frame,
                        text=str(row[i])).grid(
                            row=i, column=1, sticky="w", padx=5, pady=2
                        )
                        
                else:
                    messagebox.showwarning(
                        "Not Found", "No record found for this Roll Number."
                    )
        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {e}")
    Button(F2, text="Search", command=search_student).grid(
        row=1, column=2,columnspan=2, pady=5
        )

Button(root,text="Display Student Data",width=30,command=open_form2).grid(row=1,column=0,pady=5) 

# FORM 3: Update Student Data

def open_form3():
    F3 = Toplevel(root)
    F3.title("Form 3 - Update Student Data")

    Label(F3, text="Enter Roll No:").grid(
        row=0, column=0, padx=5, pady=5, sticky="e"
    )

    e_search = Entry(F3)
    e_search.grid(row=0, column=1, padx=5, pady=5)

    # Placeholders for entry widgets
    entries = {}

    def fetch_and_populate():
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM students WHERE roll_no = %s",
                (e_search.get(),)
            )
            row = cursor.fetchone()
            conn.close()

            if row:
                fields = [
                    "Roll No", "Name", "Gender", "Age", "City", "Class",
                    "Sub 1", "Sub 2", "Sub 3", "Sub 4", "Sub 5", "Sub 6",
                ]

                for i, field in enumerate(fields):
                    Label(F3, text=f"{field}:").grid(
                        row=i + 2, column=0, padx=5, pady=2, sticky="e"
                    )

                    ent = Entry(F3)
                    ent.grid(row=i + 2, column=1, padx=5, pady=2)
                    ent.insert(0, str(row[i]))

                    if i == 0:
                        # Roll No Primary Key should remain disabled
                        ent.config(state="disabled")

                    entries[field] = ent

                Button(
                    F3,
                    text="Update Data",
                    command=update_data
                ).grid(
                    row=15, column=0, columnspan=2, pady=10
                )

            else:
                messagebox.showwarning(
                    "Not Found",
                    "Roll Number not found!"
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Failed to fetch record: {e}"
            )

    def update_data():
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = """UPDATE students SET name=%s, gender=%s, age=%s, city=%s, class=%s, sub1=%s, sub2=%s, sub3=%s, sub4=%s, sub5=%s, sub6=%s WHERE roll_no=%s"""

            vals = (
                entries["Name"].get(),
                entries["Gender"].get(),
                int(entries["Age"].get()),
                entries["City"].get(),
                entries["Class"].get(),
                int(entries["Sub 1"].get()),
                int(entries["Sub 2"].get()),
                int(entries["Sub 3"].get()),
                int(entries["Sub 4"].get()),
                int(entries["Sub 5"].get()),
                int(entries["Sub 6"].get()),
                int(entries["Roll No"].get()),
            )

            cursor.execute(query, vals)
            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Success",
                "Record updated successfully!"
            )

            F3.destroy()

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Failed to update record: {e}"
            )

    Button(
        F3,
        text="Fetch Record",
        command=fetch_and_populate
    ).grid(
        row=1, column=0, columnspan=2, pady=5
    )

Button(root,text="Update Student Data",width=30,command=open_form3).grid(row=2,column=0,pady=5)


# FORM 4: Delete Student Data

def open_form4():
    F4 = Toplevel(root)
    F4.title("Form 4 - Delete Student Data")

    Label(F4, text="Enter Roll No to Delete:").grid(
        row=0, column=0, padx=5, pady=10, sticky="e"
    )

    e_del_roll = Entry(F4)
    e_del_roll.grid(row=0, column=1, padx=5, pady=10)

    def delete_data():
        roll = e_del_roll.get()

        if not roll:
            messagebox.showwarning(
                "Warning",
                "Please enter a Roll Number!"
            )
            return

        confirm = messagebox.askyesno(
            "Confirm",
            f"Are you sure you want to delete Roll No: {roll}?"
        )

        if confirm:
            try:
                conn = get_db_connection()
                cursor = conn.cursor()

                cursor.execute(
                    "DELETE FROM students WHERE roll_no = %s",
                    (roll,)
                )

                conn.commit()

                if cursor.rowcount > 0:
                    messagebox.showinfo(
                        "Success",
                        "Student record deleted successfully!"
                    )
                    F4.destroy()
                else:
                    messagebox.showwarning(
                        "Not Found",
                        "Roll Number does not exist!"
                    )

                conn.close()

            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"Deletion failed: {e}"
                )

    Button(
        F4,
        text="Delete Record",
        command=delete_data
    ).grid(
        row=1, column=0, columnspan=2, pady=10
    )

Button(root,text="Delete Student Data",width=30,command=open_form4).grid(row=3,column=0,pady=5)
root.mainloop()
