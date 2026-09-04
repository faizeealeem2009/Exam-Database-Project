import csv
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
        
        # Drop existing table if it exists to recreate with correct schema
        cursor.execute("DROP TABLE IF EXISTS students")
        
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS students (
                roll_no INT PRIMARY KEY,
                name VARCHAR(100),
                gender VARCHAR(10),
                age INT,
                city VARCHAR(50),
                class VARCHAR(20),
                Physics INT,
                Chemistry INT,
                Maths INT,
                Geography INT,
                English INT,
                Urdu INT
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
            "Database Error",f"Failed to initialize database: {err}"
        )

#get_db_connection()   
init_db()

root = Tk()

root.option_add("*Font", ("Segoe UI", 10))
root.option_add("*Label.background", "#ffffff")
root.option_add("*Label.foreground", "#30435f")
root.option_add("*Entry.font", ("Segoe UI", 10))
root.option_add("*Entry.background", "#f7f9fc")
root.option_add("*Entry.foreground", "#172b4d")
root.option_add("*Entry.borderWidth", 1)
root.option_add("*Entry.relief", "solid")
root.option_add("*Radiobutton.background", "#ffffff")
root.option_add("*Radiobutton.foreground", "#30435f")
root.option_add("*Button.background", "#2f6fed")
root.option_add("*Button.foreground", "#ffffff")
root.option_add("*Button.font", ("Segoe UI", 10, "bold"))
root.option_add("*Button.borderWidth", 0)

def create_gradient_canvas(window):
    canvas = Canvas(
        window,
        highlightthickness=0,
        bd=0,
        bg="#183b70",
    )
    canvas.pack(fill="both", expand=True)

    def draw_gradient(event=None):
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        canvas.delete("gradient")
        start = (15, 42, 82)
        end = (43, 119, 219)
        for y in range(max(height, 1)):
            ratio = y / max(height - 1, 1)
            red = int(start[0] + (end[0] - start[0]) * ratio)
            green = int(start[1] + (end[1] - start[1]) * ratio)
            blue = int(start[2] + (end[2] - start[2]) * ratio)
            canvas.create_line(
                0, y, width, y,
                fill=f"#{red:02x}{green:02x}{blue:02x}",
                tags="gradient",
            )
        canvas.tag_lower("gradient")

    canvas.bind("<Configure>", draw_gradient)
    return canvas

def prepare_form_window(window, title, geometry):
    window.title(title)
    window.geometry(geometry)
    #window.resizable(False, False)

    canvas = create_gradient_canvas(window)
    window.update_idletasks()
    content = ttk.Frame(canvas, style="Card.TFrame", padding=24)
    canvas.create_window(
        18,
        18,
        anchor="nw",
        width=max(window.winfo_width() - 36, 1),
        height=max(window.winfo_height() - 36, 1),
        window=content,
    )
    return content

# FORM 1: ENTER STUDENT DATA
def open_form1():
    g=StringVar()
    roll=StringVar()
    name=StringVar()
    city=StringVar()
    age=StringVar()
    clas=StringVar(value="Select Class")
    s1=StringVar()
    s2=StringVar()
    s3=StringVar()
    s4=StringVar()
    s5=StringVar()
    s6=StringVar()
    F1=Toplevel(root)
    form = prepare_form_window(F1, "Enter Student Data", "440x650")
    #Labels and Entries
    Label(form,text="Roll No:").grid(
        row=0,column=0,padx=5,pady=5,sticky="e"
    )
    e_roll=Entry(form,textvariable=roll)
    e_roll.grid(row=0,column=1,padx=5,pady=5)

    Label(form,text="Name:").grid(
        row=1,column=0,padx=5,pady=5,sticky="e"
    )
    e_name=Entry(form,textvariable=name)
    e_name.grid(row=1,column=1,padx=5,pady=5)

    Label(form,text="Gender:").grid(
        row=2,column=0
    )
    
    e_gender1=Radiobutton(form,variable=g,value="Male",text="Male")
    e_gender1.grid(row=2, column=1
    )

    e_gender2=Radiobutton(form,variable=g,value="Female",text="Female")
    e_gender2.grid(row=3, column=1
    )

    Label(form,text="Age:").grid(
        row=4,column=0,padx=5,pady=5,sticky="e"
    )
    e_age=Entry(form,textvariable=age)
    e_age.grid(row=4, column=1, padx=5, pady=5)

    Label(form,text="City:").grid(
        row=5,column=0,padx=5,pady=5,sticky="e"
    )
    e_city=Entry(form,textvariable=city)
    e_city.grid(row=5, column=1, padx=5, pady=5)

    Label(form, text="Class:").grid(         
        row=6, column=0, padx=5, pady=5, sticky="e"
             )     
    e_class=ttk.Combobox(
        form,
        values=["Select Class","5th","6th","7th","8th","9th","10th","11th","12th"],
        state="normal",
        style="Modern.TCombobox",
        width=13,
    )
    e_class.grid(row=6,column=1,padx=1,pady=5,columnspan=2,sticky="w")
    e_class.insert(0, "Select Class")
    e_class.configure(state="readonly")
    
    Label(form, text="Physics:").grid(
        row=7, column=0, padx=5, pady=5, sticky="e"
            )
    e_s1 = Entry(form,textvariable=s1)
    e_s1.grid(row=7, column=1, padx=5, pady=5) 
 
    Label(form, text="Chemistry:").grid(
        row=8, column=0, padx=5, pady=5, sticky="e"     
            )
    e_s2 =Entry(form,textvariable=s2)
    e_s2.grid(row=8, column=1, padx=5, pady=5) 
 
    Label(form, text="Maths:").grid(
        row=9, column=0, padx=5, pady=5, sticky="e"     
            )     
    e_s3 =Entry(form,textvariable=s3)
    e_s3.grid(row=9, column=1, padx=5, pady=5) 
 
    Label(form, text="Geography:").grid(
        row=10, column=0, padx=5, pady=5, sticky="e"     
            )     
    e_s4 =Entry(form,textvariable=s4)
    e_s4.grid(row=10, column=1, padx=5, pady=5)

    Label(form, text="English:").grid(
        row=11, column=0, padx=5, pady=5, sticky="e"     
            )     
    e_s5 =Entry(form,textvariable=s5)
    e_s5.grid(row=11, column=1, padx=5, pady=5)

    Label(form, text="Urdu:").grid(
        row=12, column=0, padx=5, pady=5, sticky="e"     
            )     
    e_s6 =Entry(form,textvariable=s6)
    e_s6.grid(row=12, column=1, padx=5, pady=5)

    def save_data():
        try:
            conn=get_db_connection()
            cursor=conn.cursor()
            query='''INSERT INTO students
                    (roll_no,name,gender,age,city,class,Physics,Chemistry,Maths,Geography,English,Urdu)
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            vals=(
                int(e_roll.get()),
                e_name.get(),
                g.get(),
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
    
    Button(
        form,
        text="Save Student",
        bg="#16a34a",
        activebackground="#15803d",
        fg="White",
        command=save_data,
    ).grid(
        row=13,column=0,columnspan=2,padx=5,pady=5
    )

# FORM 2: Display Student Data

def open_form2():
    F2=Toplevel(root)
    form = prepare_form_window(F2, "Display Student Data", "430x520")
    Label(form,text="Enter Roll No:").grid(
        row=0,column=0,padx=5,pady=5,sticky="e"
    )
    e_search_roll=Entry(form)
    e_search_roll.grid(row=0,column=1,padx=5,pady=5)

    #Frame to show Detais
    display_frame=Frame(form, bg="#ffffff")
    display_frame.grid(row=2,column=0,columnspan=2,pady=10)

    def search_student():
        for widget in display_frame.winfo_children():
            widget.destroy()
        try:
            conn=get_db_connection()
            cursor=conn.cursor()
            cursor.execute(
                "SELECT * FROM students WHERE roll_no=%s",
                (e_search_roll.get(),)
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
                    "Physics",
                    "Chemistry",
                    "Maths",
                    "Geography",
                    "English",
                    "Urdu",
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
    Button(form, text="Search", command=search_student).grid(
        row=1, column=1,columnspan=2,pady=5
        )


# FORM 3: Update Student Data

def open_form3():
    F3 = Toplevel(root)
    form = prepare_form_window(F3, "Update Student Data", "500x680")

    Label(form, text="Enter Roll No:").grid(
        row=0, column=0, padx=5, pady=5, sticky="e"
    )

    e_search = Entry(form)
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
                    "Physics", "Chemistry", "Maths", "Geography", "English", "Urdu",
                ]

                for i, field in enumerate(fields):
                    Label(form, text=f"{field}:").grid(
                        row=i + 2, column=0, padx=5, pady=2, sticky="e"
                    )

                    ent = Entry(form)
                    ent.grid(row=i + 2, column=1, padx=5, pady=2)
                    ent.insert(0, str(row[i]))

                    if i == 0:
                        # Roll No Primary Key should remain disabled
                        ent.config(state="disabled")

                    entries[field] = ent

                Button(
                    form,
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

            query = """UPDATE students SET name=%s, gender=%s, age=%s, city=%s, class=%s, Physics=%s, Chemistry=%s, Maths=%s, Geography=%s, English=%s, Urdu=%s WHERE roll_no=%s"""

            vals = (
                entries["Name"].get(),
                entries["Gender"].get(),
                int(entries["Age"].get()),
                entries["City"].get(),
                entries["Class"].get(),
                int(entries["Physics"].get()),
                int(entries["Chemistry"].get()),
                int(entries["Maths"].get()),
                int(entries["Geography"].get()),
                int(entries["English"].get()),
                int(entries["Urdu"].get()),
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
        form,
        text="Fetch Record",command=fetch_and_populate,bg="green",fg="White",font=("Arial",10,"bold")
    ).grid(
        row=1, column=0, columnspan=2, pady=5
    )



# FORM 4: Delete Student Data

def open_form4():
    F4 = Toplevel(root)
    form = prepare_form_window(F4, "Delete Student Data", "550x700")
    
    # Configure grid weights for proper layout
    form.grid_rowconfigure(2, weight=1)
    form.grid_columnconfigure(0, weight=1)
    form.grid_columnconfigure(1, weight=1)

    Label(form, text="Enter Roll No to Delete:").grid(
        row=0, column=0, padx=5, pady=10, sticky="e"
    )

    e_del_roll = Entry(form)
    e_del_roll.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

    # Frame to show Student Details
    display_frame = Frame(form, bg="#ffffff")
    display_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=5, sticky="nsew")

    # Buttons frame for Confirm and Cancel
    buttons_frame = Frame(form, bg="#111c32")
    buttons_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew", padx=5)

    def fetch_student():
        # Clear previous data
        for widget in display_frame.winfo_children():
            widget.destroy()
        # Clear previous buttons
        for widget in buttons_frame.winfo_children():
            widget.destroy()
        
        roll = e_del_roll.get()

        if not roll:
            messagebox.showwarning("Warning", "Please enter a Roll Number!")
            return

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM students WHERE roll_no = %s",
                (roll,)
            )
            row = cursor.fetchone()
            conn.close()

            if row:
                labels = [
                    "Roll No", "Name", "Gender", "Age", "City", "Class",
                    "Physics", "Chemistry", "Maths", "Geography", "English", "Urdu",
                ]
                for i in range(len(labels)):
                    Label(
                        display_frame,
                        text=f"{labels[i]}:",
                        font=("Arial", 10, "bold"),
                        bg="#ffffff"
                    ).grid(row=i, column=0, padx=5, pady=2, sticky="e")
                    Label(
                        display_frame,
                        text=str(row[i]),
                        bg="#ffffff"
                    ).grid(row=i, column=1, sticky="w", padx=5, pady=2)
                
                # Show delete and cancel buttons after data is displayed
                Button(
                    buttons_frame,
                    text="✓ Confirm Delete",
                    command=confirm_delete,
                    bg="#dc2626",
                    fg="White",
                    font=("Arial", 10, "bold"),
                ).pack(side="left", padx=5, pady=5, fill="x", expand=True)
                
                Button(
                    buttons_frame,
                    text="✕ Cancel",
                    command=cancel_delete,
                    bg="#6b7280",
                    fg="White",
                    font=("Arial", 10, "bold"),
                ).pack(side="left", padx=5, pady=5, fill="x", expand=True)
            else:
                messagebox.showwarning(
                    "Not Found",
                    "Roll Number does not exist!"
                )

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch record: {e}")

    def cancel_delete():
        for widget in display_frame.winfo_children():
            widget.destroy()
        for widget in buttons_frame.winfo_children():
            widget.destroy()
        e_del_roll.delete(0, "end")

    def confirm_delete():
        roll = e_del_roll.get()
        
        confirm = messagebox.askyesno(
            "Confirm Deletion",
            f"Are you sure you want to delete Roll No: {roll}?\nThis action cannot be undone!"
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
                conn.close()

                messagebox.showinfo(
                    "Success",
                    "Student record deleted successfully!"
                )
                F4.destroy()

            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"Deletion failed: {e}"
                )

    # Now create the button after functions are defined
    Button(
        form,
        text="🔍 Search & View",
        command=fetch_student,
        bg="#2563eb",
        fg="White",
        font=("Arial", 11, "bold"),
    ).grid(row=1, column=0, columnspan=2, pady=10, sticky="ew", padx=5)



# FORM 5: DISPLAY ALL DATA & EXPORT TO CSV

def open_form5():
    F5 = Toplevel(root)
    form = prepare_form_window(F5, "All Students and Export CSV", "1220x820")

    # Scrollable Table Frame setup
    table_frame = Frame(form, bg="#ffffff")
    table_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    scroll_x = ttk.Scrollbar(table_frame, orient="horizontal")
    scroll_y = ttk.Scrollbar(table_frame, orient="vertical")

    cols = (
        "Roll No",
        "Name",
        "Gender",
        "Age",
        "City",
        "Class",
        "Physics",
        "Chemistry",
        "Maths",
        "Geography",
        "English",
        "Urdu",
    )

    tree = ttk.Treeview(
        table_frame,
        columns=cols,
        show="headings",
        style="Modern.Treeview",
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set,
    )

    scroll_x.pack(side="bottom", fill="x")
    scroll_y.pack(side="right", fill="y")
    scroll_x.config(command=tree.xview)
    scroll_y.config(command=tree.yview)

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=90, anchor="center")

    tree.pack(fill="both", expand=True)

    # Fetch and load data into Treeview
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        for row in rows:
            tree.insert("", "end", values=row)

        conn.close()

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Failed to fetch data: {e}"
        )

    # Export to CSV logic
    def export_to_csv():
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()

            with open(
                "student_data.csv",
                "w",
                newline="",
                encoding="utf-8"
            ) as file:
                writer = csv.writer(file)
                writer.writerow(cols)  # Write header row
                writer.writerows(rows)  # Write data rows

            conn.close()

            messagebox.showinfo(
                "Success",
                "Data exported successfully to 'student_data.csv'!"
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Export failed: {e}"
            )

    Button(
        form,
        text="Export All Data to CSV",command=export_to_csv,bg="green",fg="White",font=("Arial",10,"bold")
    ).grid(
        row=1, column=0
    )

# Main Application Window
root.title("Exam Management System")
#root.geometry("760x620")
#root.minsize(680, 560)
root.configure(bg="#0f172a")

style = ttk.Style(root)
style.theme_use("clam")
style.configure("Main.TFrame", background="#0f172a")
style.configure("Card.TFrame", background="#111c32")
style.configure(
    "Title.TLabel",
    background="#0f172a",
    foreground="#ffffff",
    font=("Segoe UI", 28, "bold"),
)
style.configure(
    "Subtitle.TLabel",
    background="#0f172a",
    foreground="#cbd5e1",
    font=("Segoe UI", 10),
)
style.configure(
    "Menu.TButton",
    background="#2f6fed",
    foreground="#ffffff",
    font=("Segoe UI", 11, "bold"),
    padding=(18, 13),
    borderwidth=0,
)
style.map(
    "Menu.TButton",
    background=[("active", "#2458bd"), ("pressed", "#1d479a")],
)
for name, color, active in (
    ("Green", "#16a34a", "#15803d"),
    ("Blue", "#2563eb", "#1d4ed8"),
    ("Orange", "#ea580c", "#c2410c"),
    ("Red", "#dc2626", "#b91c1c"),
    ("Purple", "#7c3aed", "#6d28d9"),
):
    style.configure(
        f"{name}.Menu.TButton",
        background=color,
        foreground="#ffffff",
        font=("Segoe UI", 10, "bold"),
        padding=(16, 13),
        borderwidth=0,
    )
    style.map(
        f"{name}.Menu.TButton",
        background=[("active", active), ("pressed", active)],
    )
style.configure(
    "Exit.TButton",
    background="#1e293b",
    foreground="#cbd5e1",
    font=("Segoe UI", 10, "bold"),
    padding=(12, 8),
    borderwidth=1,
    relief="solid",
)
style.configure(
    "Modern.Treeview",
    background="#f7f9fc",
    fieldbackground="#f7f9fc",
    foreground="#30435f",
    rowheight=30,
    font=("Segoe UI", 9),
)
style.configure(
    "Modern.TCombobox",
    foreground="#172b4d",
    fieldbackground="#f7f9fc",
    background="#f7f9fc",
    arrowcolor="#172b4d",
    padding=5,
)
style.map(
    "Modern.TCombobox",
    fieldbackground=[("readonly", "#f7f9fc")],
    foreground=[("readonly", "#172b4d")],
)
style.configure(
    "Modern.Treeview.Heading",
    background="#172b4d",
    foreground="#ffffff",
    font=("Segoe UI", 9, "bold"),
    padding=8,
)
style.map(
    "Modern.Treeview",
    background=[("selected", "#dbe8ff")],
    foreground=[("selected", "#172b4d")],
)
style.map(
    "Exit.TButton",
    background=[("active", "#334155")],
    foreground=[("active", "#ffffff")],
)

main_frame = ttk.Frame(root, style="Main.TFrame", padding=(36, 32, 36, 24))
main_frame.pack(fill="both", expand=True)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

ttk.Label(main_frame, text="EXAM MANAGEMENT SYSTEM", style="Title.TLabel").grid(
    row=0, column=0, columnspan=2, sticky="w", pady=(0, 4)
)
ttk.Label(
    main_frame,
    text="Student records  •  Marks  •  Database management",
    style="Subtitle.TLabel",
).grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 28))

Frame(main_frame, bg="#2563eb", height=3).grid(
    row=2, column=0, columnspan=2, sticky="ew", pady=(0, 28)
)

ttk.Label(main_frame, text="Dashboard", style="Title.TLabel").grid(
    row=3, column=0, columnspan=2, sticky="w", pady=(0, 4)
)
ttk.Label(
    main_frame,
    text="Choose an operation to continue",
    style="Subtitle.TLabel",
).grid(row=4, column=0, columnspan=2, sticky="w", pady=(0, 22))

menu_items = (
    ("1  •  Enter Student Data", open_form1, "Green"),
    ("2  •  Display Student Data", open_form2, "Blue"),
    ("3  •  Update Student Data", open_form3, "Orange"),
    ("4  •  Delete Student Data", open_form4, "Red"),
    ("5  •  Display All & Export Data", open_form5, "Purple"),
)

for index, (label, command, color) in enumerate(menu_items[:4]):
    ttk.Button(
        main_frame,
        text=label,
        command=command,
        style=f"{color}.Menu.TButton",
    ).grid(
        row=5 + index // 2,
        column=index % 2,
        sticky="ew",
        padx=(0, 8) if index % 2 == 0 else (8, 0),
        pady=6,
    )

ttk.Button(
    main_frame,
    text="5  •  Display All & Export Data",
    command=open_form5,
    style="Purple.Menu.TButton",
).grid(row=7, column=0, columnspan=2, sticky="ew", pady=(6, 0))

ttk.Button(main_frame, text="Close", command=root.destroy, style="Exit.TButton").grid(
    row=8, column=0, columnspan=2, pady=(30, 0)
)

ttk.Label(
    main_frame,
    text="Exam Management System  •  MySQL Database",
    style="Subtitle.TLabel",
).grid(row=9, column=0, columnspan=2, pady=(34, 0))

root.mainloop()
