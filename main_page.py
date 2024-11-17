from tkinter import *
from tkinter import messagebox, filedialog
from db_connect import get_f_l_name
from datetime import datetime

def main_page(username, password):
    x = get_f_l_name(username, password)[0]
    today_datetime = datetime.today()
    formatted_date = today_datetime.strftime("%m/%d/%Y")
    def upload_photo():
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        if file_path:
            messagebox.showinfo("Photo Selected", f"Selected photo: {file_path}")

    def logout():
        frame.destroy()
        from login import login_register
        login_register()

    def calculate_duration():
        pass

    duration = calculate_duration()
    global frame
    frame = Tk()
    frame.geometry("900x500")
    frame.title("Main Page")
    frame.resizable(False, False)

    # header
    header = Frame(frame, bg='spring green', width=900, height=75).pack(side=TOP)
    Label(header, text='SWEEPIFY', font=('Times', '30', 'bold italic'), bg='spring green').place(x=25, y=15)

    # sub-header
    Label(frame, text='USER PROFILE', font=('Times', '20', 'bold')).place(x=25, y=90)

    # Name Display
    Label(frame, text='Name: ', font=('Times', '15', 'bold')).place(x=25, y=130)
    output1 = Label(frame, text=x[0].title()).place(x=150, y=130)
    output2 = Label(frame, text=x[1].title()).place(x=200, y=130)

    # Schedule
    Label(frame, text='Schedule: ', font=('Times', '15', 'bold')).place(x=25, y=175)

    Label(frame, text='Date: ', font=('Times', '10', 'bold')).place(x=45, y=200)
    output3 = Label(frame, text=formatted_date).place(x=150, y=200)
    Label(frame, text='Start Time: ', font=('Times', '10', 'bold')).place(x=45, y=225)
    output4 = Label(frame, text='').place(x=150, y=225)
    Label(frame, text='End Time: ', font=('Times', '10', 'bold')).place(x=45, y=250)
    output5 = Label(frame, text='').place(x=150, y=250)

    # Location Assignment
    Label(frame, text='Location/s Assigned: ', font=('Times', '15', 'bold')).place(x=25, y=275)
    loc_output1 = Label(frame, text='').place(x=300, y=275)

    # Photo Verification
    Label(frame, text='Photo Verification:', font=('Times', '15', 'bold')).place(x=25, y=325)
    photo_btn = Button(frame, text='Upload Photo', width=20, bd=5, command=upload_photo).place(x=25, y=350)

    # Logout
    logout_btn = Button(frame, text='Log out', width=20, bd=5, command=logout).place(x=700, y=450)

    frame.mainloop()
