from customtkinter import *
import customtkinter
from PIL import Image 
import PIL
import tkinter as tk
root=customtkinter.CTk(fg_color="#EEE5E0")
root.title("MY LIBRARY")
root.geometry("650x560+550+90")
#root.minsize(450,500)
root.maxsize(600,700)
root.resizable(True,True)
logo_image = customtkinter.CTkImage(Image.open("C:/Users/DELL/Downloads/book_logo_2.png"),size=(30,30))
#add .after in future
find_image = customtkinter.CTkImage(Image.open("C:/Users/DELL/Downloads/logo_image.png"),size=(20,20))
JNTUH_logo_image = customtkinter.CTkImage(Image.open("C:/Users/DELL/Downloads/jntuh logo.png"),size=(80,80))
books_image1 = customtkinter.CTkImage(Image.open("C:/Users/DELL/Downloads/books1.png"),size=(90,90))
camera_image = customtkinter.CTkImage(Image.open("C:/Users/DELL/Downloads/ccc.png"),size=(25,25))

logo_label = customtkinter.CTkLabel(root,height=40,width=534,
                                    text=" Welcome To Our Digital Library",
                                    fg_color="#A08679",
                                    image=logo_image,
                                    compound="left",padx=20,
                                    font=("Poppins",30),
                                    text_color="#3D251E",anchor="center",
                                    corner_radius=0,
                                    
                                    )
logo_label.image=logo_image
logo_label.place(x=48,y=10)

announcement_label = customtkinter.CTkLabel(root,height=35,width=530,
                                            text="New Announcement",
                                            fg_color="#A08679",text_color="#5B3E31",
                                            border_color="#BCA89F",border_width=3,
                                            font=("Poppins",20)
                                            )
announcement_label.place(x=48,y=59)

find_label = customtkinter.CTkLabel(root,text="   Find books here   ",
                                    text_color="#4C3228",
                                    font=("Poppins",25),
                                    bg_color="#8B6C5C")
find_label.place(x=170,y=100)

find_entry = customtkinter.CTkEntry(root,placeholder_text="Enter book name",
                                    placeholder_text_color="#BCA89F",
                                    fg_color="#8B6C5C",
                                    width=270,
                                    height=30,
                                    corner_radius=30,
                                    font=("Poppins",20),
                                    text_color="#D8CBC4"
                                    )
find_entry.place(x=210,y=137)

find_logo_button = customtkinter.CTkButton(root,height=30,width=30,
                                           image=find_image,text="",
                                           fg_color="#8B6C5C",
                                           hover_color="#5B3E31"
                                           )
find_logo_button.place(x=170,y=137)

camera_button = customtkinter.CTkButton(root,width=30,height=30,
                                         image=camera_image,text="",
                                         fg_color="#8B6C5C",hover_color="#5B3E31")
camera_button.place(x=490,y=137)
##############################
top_books_frame = customtkinter.CTkFrame(master=root,height=650,width=640,fg_color="#D8CBC4")
# the top books framw

def on_click_top():
    """when the top books button is clicked"""
    top_books_frame.lift()
    top_books_frame.pack(padx=8,pady=8)
    top_books_frame.pack_propagate()
def on_click_back_button():
    """when back button is clicked on the new frame"""
    top_books_frame.pack_forget()
    root.lift()
#####################################################################
final_book_frame =customtkinter.CTkFrame(master=top_books_frame,height=650,width=640,fg_color="#BCA89F") 
def on_click_final():
    final_book_frame.lift()
    final_book_frame.pack(padx=0,pady=0)
    final_book_frame.pack_propagate()
def on_click_back_button1():
    """when back button is clicked on the new frame"""
    final_book_frame.pack_forget()
    root.lift()

final_label = customtkinter.CTkLabel(master=final_book_frame,height=40,width=470,
                                         text="  THE BOOK", fg_color="#8B6C5C",text_color="#EEE5E0",
                                         font=("Poppins",19),compound="center",anchor=W)
final_label.place(y=10,x=60)
final_desp = customtkinter.CTkLabel(master=final_book_frame,height=60,width=520,
                                        fg_color="#765341",
                                        text="The boook you wanted is here.. you can look the section which is in our library and \ncheck out the 3D library or the link of the pdf of the book",
                                        font=("Poppins",13))
final_desp.place(x=10,y=60)
back_button1 = customtkinter.CTkButton(master=final_book_frame,height=40,width=40,
                                      text=">",hover=True,hover_color="#5B3E31",
                                      fg_color="#8B6C5C",command=on_click_back_button1)
back_button1.place(x=10,y=10)
final_book = customtkinter.CTkButton(master=final_book_frame,height=270,width=220,
                                     text="",hover=False,fg_color="#5B3E31",
                                     corner_radius=1)
final_book.place(x=20,y=145)
final_book_section = customtkinter.CTkLabel(master=final_book_frame,height=50,width=240,
                                            text="section : 1 \n shelf : 2",fg_color="#765341",
                                            text_color="#EEE5E0",corner_radius=9,font=("Poppins",16))
final_book_section.place(x=265,y=150)
final_book_3d = customtkinter.CTkButton(master=final_book_frame,height=50,width=240,
                                        text="3D Image of the library",text_color="#EEE5E0",
                                        fg_color="#765341",hover=True,hover_color="#4C3228",
                                        corner_radius=9,font=("Poppins",19))
final_book_3d.place(x=265,y=215)
final_book_notes = customtkinter.CTkButton(master=final_book_frame,height=50,width=240,
                                           text="Notes",text_color="#EEE5E0",
                                           fg_color="#765341",hover=True,hover_color="#4C3228",
                                           corner_radius=9,font=("Poppins",19))
final_book_notes.place(x=265,y=280)
final_book_previous_year_papers = customtkinter.CTkButton(master=final_book_frame,height=50,width=240,
                                        text="3D Image of the library",text_color="#EEE5E0",
                                        fg_color="#765341",hover=True,hover_color="#4C3228",
                                        corner_radius=9,font=("Poppins",19))
final_book_previous_year_papers.place(x=265,y=348)
final_book_pdf = customtkinter.CTkButton(master=final_book_frame,height=40,width=520,
                                         text="The PDF of the Book",text_color="#EEE5E0",
                                         fg_color="#765341",hover=True,hover_color="#4C3228",
                                         corner_radius=9,font=("Poppins",19))
final_book_pdf.place(x=20,y=435)

#####################################################################
top_books_label = customtkinter.CTkLabel(master=top_books_frame,height=40,width=470,
                                         text="  TOP BOOKS", fg_color="#8B6C5C",text_color="#EEE5E0",
                                         font=("Poppins",19),compound="center",anchor=W)
top_books_label.place(y=10,x=60)
top_books_desp = customtkinter.CTkLabel(master=top_books_frame,height=60,width=520,
                                        fg_color="#765341",
                                        text="This is the page where you can the top books used by every student",
                                        font=("Poppins",15),)
top_books_desp.place(x=10,y=60)
back_button = customtkinter.CTkButton(master=top_books_frame,height=40,width=40,
                                      text=">",hover=True,hover_color="#5B3E31",
                                      fg_color="#8B6C5C",command=on_click_back_button)
back_button.place(x=10,y=10)
#teh scrollable frame for the books
top_books_scrollable_frame = customtkinter.CTkScrollableFrame(master=top_books_frame,height=450,width=489,
                                            fg_color="#A08679",border_width=5,border_color="#5B3E31",
                                            scrollbar_fg_color="#A08679",scrollbar_button_color="#3D251E",
                                            scrollbar_button_hover_color="#5B3E31")
top_books_scrollable_frame.place(x=10,y=140)

book_1 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_1.grid(row=0,column=0,padx=7,pady=7)
book_2 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_2.grid(row=0,column=1,padx=7,pady=7)
book_3 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_3.grid(row=0,column=2,padx=7,pady=7)
book_4 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_4.grid(row=1,column=0,padx=7,pady=7)
book_5 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_5.grid(row=1,column=1,padx=7,pady=7)
book_6 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_6.grid(row=1,column=2,padx=7,pady=7)
book_7 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_7.grid(row=2,column=0,padx=7,pady=7)
book_8 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_8.grid(row=2,column=1,padx=7,pady=7)
book_9 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_9.grid(row=2,column=2,padx=7,pady=7)
book_10 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_10.grid(row=3,column=0,padx=7,pady=7)
book_11 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_11.grid(row=3,column=1,padx=7,pady=7)
book_12 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_12.grid(row=3,column=2,padx=7,pady=7)
book_13 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_13.grid(row=4,column=0,padx=7,pady=7)
book_14 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_14.grid(row=4,column=1,padx=5,pady=5)
book_15 = customtkinter.CTkButton(master=top_books_scrollable_frame,height=170,width=140,
                                fg_color="#6A4A3A",text_color="#EEE5E0",text="",
                                hover=True,hover_color="#5B3E31",command=on_click_final)
book_15.grid(row=4,column=2,padx=5,pady=5)



#the buttons on the main page
buttons_frame = customtkinter.CTkFrame(master= root, height=380,width=429,
                                       fg_color="#D8CBC4")
buttons_frame.place(x=167,y=174)

top_books_button = customtkinter.CTkButton(master=buttons_frame,width=120,height=140,
                                           text="Top Books",text_color="#D8CBC4",
                                           fg_color="#6A4A3A",
                                           hover=True,hover_color="#5B3E31",
                                           font=("Poppins",19),
                                           anchor=N,
                                           image=books_image1,compound="bottom",
                                           border_spacing=5,command=on_click_top
                                           
                                           )
top_books_button.place(x=10,y=10)

another1_button = customtkinter.CTkButton(master=buttons_frame,width=120,height=140,
                                         text="Future\nButton",text_color="#D8CBC4",
                                         fg_color="#6A4a3A",
                                         hover=True,hover_color="#5B3E31",
                                         font=("Poppins",19))
another1_button.place(x=270,y=10)
recommended_books_frame = customtkinter.CTkFrame(master=root, height=550, width=640,
                                            fg_color="#D8CBC4")
def on_click_recommended():
    """when the recommeneded button is clicked"""
    recommended_books_frame.lift()
    recommended_books_frame.pack(padx=8,pady=8,fill="both",expand=True)
    recommended_books_frame.pack_propagate()
def on_click_back_button():
    """when back button is clicked on the new frame"""
    recommended_books_frame.pack_forget()
    root.lift()
recommended_label = customtkinter.CTkLabel(master=recommended_books_frame ,height=40,width=470,
                                         text="  REDOMMENDED BOOKS", fg_color="#8B6C5C",text_color="#EEE5E0",
                                         font=("Poppins",19),compound="center",anchor=W)
recommended_label.place(y=10,x=60)
recommended_desp = customtkinter.CTkLabel(master=recommended_books_frame ,height=60,width=520,
                                        fg_color="#765341",
                                        text="This is the page where we can help you to use the book",
                                        font=("Poppins",15),)
recommended_desp.place(x=10,y=60)
back_button = customtkinter.CTkButton(master=recommended_books_frame ,height=40,width=40,
                                      text=">",hover=True,hover_color="#5B3E31",
                                      fg_color="#8B6C5C",command=on_click_back_button)
back_button.place(x=10,y=10)
course_lable = customtkinter.CTkLabel(master=recommended_books_frame,height=40,
                                      text="Enter your Course",text_color="#4C3228",
                                      font=("Poppins",25),fg_color="#D8CBC4")
course_lable.place(x=140,y=130)
course_entry = customtkinter.CTkEntry(master=recommended_books_frame,height=50,width=270,
                                      corner_radius=10,fg_color="#765341",text_color="#EEE5E0",
                                      placeholder_text="Enter your course",font=("Poppins",20),
                                      border_color="#A08679",placeholder_text_color="#AB9B91")
course_entry.place(x=140,y=170)
year_lable = customtkinter.CTkLabel(master=recommended_books_frame,height=40,
                                      text="Enter your Year",text_color="#4C3228",
                                      font=("Poppins",25),fg_color="#D8CBC4")
year_lable.place(x=140,y=230)
year_entry = customtkinter.CTkEntry(master=recommended_books_frame,height=50,width=270,
                                      corner_radius=10,fg_color="#765341",text_color="#EEE5E0",
                                      placeholder_text="Enter your year",font=("Poppins",20),
                                      border_color="#A08679",placeholder_text_color="#AB9B91")
year_entry.place(x=140,y=270)
subject_lable = customtkinter.CTkLabel(master=recommended_books_frame,height=40,
                                      text="Enter your Subject",text_color="#4C3228",
                                      font=("Poppins",25),fg_color="#D8CBC4")
subject_lable.place(x=140,y=330)
subject_entry = customtkinter.CTkEntry(master=recommended_books_frame,height=50,width=270,
                                      corner_radius=10,fg_color="#765341",text_color="#EEE5E0",
                                      placeholder_text="Enter your subject",font=("Poppins",20),
                                      border_color="#A08679",placeholder_text_color="#AB9B91")
subject_entry.place(x=140,y=370)
submit_button = customtkinter.CTkButton(master=recommended_books_frame,height=45,
                                        text="Submit",text_color="#EEE5E0",font=("Poppins",20),
                                        fg_color="#765341",hover_color="#4C3228")
submit_button.place(x=140,y=440)
drawing_frame2 = customtkinter.CTkFrame(master=recommended_books_frame,height=400,width=120,
                                        fg_color="#8B6C5C",border_width=2,border_color="#BCA89F")
drawing_frame2.place(x=10,y=130)
recommended_book_button = customtkinter.CTkButton(master=buttons_frame,width=120,height=140,
                                                  text="Recom\nmended\nBooks",text_color="#D8CBC4",
                                                  fg_color="#6A4A3A",
                                                  hover=True,hover_color="#5B3E31",
                                                  font=("Poppins",19),
                                                  command=on_click_recommended)
recommended_book_button.place(x=140,y=10)


jntuh_frame = customtkinter.CTkFrame(master=root,height=550, width=64,fg_color="#D8CBC4")
def on_click_jntuh():
    """when jnuth is clicked"""
    jntuh_frame.lift()
    jntuh_frame.pack(padx=8,pady=8,fill="both",expand=True)
    jntuh_frame.pack_propagate()
def on_click_back_button():
    """when back button is clicked on the new frame"""
    jntuh_frame.pack_forget()
    root.lift()
jntuh_label = customtkinter.CTkLabel(master=jntuh_frame,height=40,width=470,
                                         text="  JNTUH", fg_color="#8B6C5C",text_color="#EEE5E0",
                                         font=("Poppins",19),compound="center",anchor=W)
jntuh_label.place(y=10,x=60)
jntuh_desp = customtkinter.CTkLabel(master=jntuh_frame,height=60,width=520,
                                        fg_color="#765341",
                                        text="This page shows the official information about the syllabus of the each course",
                                        font=("Poppins",15),)
jntuh_desp.place(x=10,y=60)
back_button = customtkinter.CTkButton(master=jntuh_frame,height=40,width=40,
                                      text=">",hover=True,hover_color="#5B3E31",
                                      fg_color="#8B6C5C",command=on_click_back_button)
back_button.place(x=10,y=10)


#the frame when you click the cse syllabus button
C_new_frame = customtkinter.CTkFrame(master=jntuh_frame,height=550, width=64,fg_color="#D8CBC4")
def computer_science_syllabus1():
    """the syllabus frame when you click the computer scrience button"""
    C_new_frame.lift()
    C_new_frame.pack(padx=2,pady=2,fill="both")
    C_new_frame.pack_propagate()
def on_click_back_button():
    """when back button is clicked on the new frame"""
    C_new_frame.pack_forget()
    root.lift()
R25_syllabus_label = customtkinter.CTkLabel(master=C_new_frame,height=40,width=470,
                                         text="  R25 syllabus CSE", fg_color="#8B6C5C",text_color="#EEE5E0",
                                         font=("Poppins",19),compound="center",anchor=W)
R25_syllabus_label.place(y=10,x=60)
back_button = customtkinter.CTkButton(master=C_new_frame,height=40,width=40,
                                      text=">",hover=True,hover_color="#5B3E31",
                                      fg_color="#8B6C5C",command=on_click_back_button)
back_button.place(x=10,y=10)
R25_syllabus_desp = customtkinter.CTkLabel(master=C_new_frame,height=60,width=520,
                                        fg_color="#765341",
                                        text="This page shows the official information about the syllabus of the CSE R25 regulation course",
                                        font=("Poppins",15),)
R25_syllabus_desp.place(x=10,y=60)
sem1_button = customtkinter.CTkButton(master=C_new_frame,height=30,width=90,
                                      text="1st SEM",text_color="#EEE5E0",
                                      fg_color="#6A4A3A",font=("Poppins",17),
                                      hover=True,hover_color="#5B3E31"
                                      )
sem2_button = customtkinter.CTkButton(master=C_new_frame,height=30,width=90,
                                      text="2nd SEM",text_color="#EEE5E0",
                                      fg_color="#6A4A3A",font=("Poppins",17),
                                      hover=True,hover_color="#5B3E31"
                                      )
def on_click_first():
    """when first year is clicked"""
    sem1_button.configure(text="1st SEM")
    sem1_button.place(x=210,y=140)
    sem2_button.configure(text="2nd SEM")
    sem2_button.place(x=210,y=175)

first_year_CSE = customtkinter.CTkButton(master=C_new_frame,height=65,width=170,
                                         text=" 1ST YEAR CSE ",text_color="#EEE5E0",
                                         hover=True,hover_color="#5B3E31",
                                         fg_color="#6A4A3A",font=("Poppins",19),
                                         command=on_click_first)
first_year_CSE.place(x=20,y=140)
def on_click_second():
    """when first year is clicked"""
    sem1_button.configure(text="3rd SEM")
    sem1_button.place(x=210,y=225)
    sem2_button.configure(text="4th SEM")
    sem2_button.place(x=210,y=260)
second_year_CSE = customtkinter.CTkButton(master=C_new_frame,height=65,width=170,
                                         text=" 2ND YEAR CSE ",text_color="#EEE5E0",
                                         hover=True,hover_color="#5B3E31",
                                         fg_color="#6A4A3A",font=("Poppins",19),
                                         command=on_click_second
                                         )
second_year_CSE.place(x=20,y=225)
def on_click_third():
    """when first year is clicked"""
    sem1_button.configure(text="5th SEM")
    sem1_button.place(x=210,y=310)
    sem2_button.configure(text="6th SEM")
    sem2_button.place(x=210,y=345)
third_year_CSE = customtkinter.CTkButton(master=C_new_frame,height=65,width=170,
                                         text=" 3RD YEAR CSE ",text_color="#EEE5E0",
                                         hover=True,hover_color="#5B3E31",
                                         fg_color="#6A4A3A",font=("Poppins",19),
                                         command=on_click_third)
third_year_CSE.place(x=20,y=310)
def on_click_fourth():
    """when first year is clicked"""
    sem1_button.configure(text="7th SEM")
    sem1_button.place(x=210,y=395)
    sem2_button.configure(text="8th SEM")
    sem2_button.place(x=210,y=430)
fourth_year_CSE = customtkinter.CTkButton(master=C_new_frame,height=65,width=170,
                                         text=" 4TH YEAR CSE ",text_color="#EEE5E0",
                                         hover=True,hover_color="#5B3E31",
                                         fg_color="#6A4A3A",font=("Poppins",19),
                                         command=on_click_fourth)
fourth_year_CSE.place(x=20,y=395)
label_1C = customtkinter.CTkLabel(master=jntuh_frame,text="Computer Science",
                                  text_color="#3D251E",fg_color="#D8CBC4",
                                  font=("Poppins",30))
label_1C.place(x=15,y=130)
label_1C_button = customtkinter.CTkButton(master=jntuh_frame,height=40,width=520,
                                          text="JNTUH Syllabus of CSE course",
                                          fg_color="#8B6C5C",
                                          text_color="#EEE5E0",font=("Poppins",15),
                                          hover=True,hover_color="#5B3E31",
                                          command=computer_science_syllabus1
                                          )
label_1C_button.place(x=15,y=170)

E_new_frame = customtkinter.CTkFrame(master=jntuh_frame,height=550, width=64,fg_color="#D8CBC4")
def ECE_syllabus1():
    """the syllabus frame when you click the computer scrience button"""
    E_new_frame.lift()
    E_new_frame.pack(padx=2,pady=2,fill="both")
    E_new_frame.pack_propagate()
def on_click_back_button():
    """when back button is clicked on the new frame"""
    E_new_frame.pack_forget()
    root.lift()
R25_syllabus_label = customtkinter.CTkLabel(master=E_new_frame,height=40,width=470,
                                         text="  R25 syllabus ECE", fg_color="#8B6C5C",text_color="#EEE5E0",
                                         font=("Poppins",19),compound="center",anchor=W)
R25_syllabus_label.place(y=10,x=60)
back_button = customtkinter.CTkButton(master=E_new_frame,height=40,width=40,
                                      text=">",hover=True,hover_color="#5B3E31",
                                      fg_color="#8B6C5C",command=on_click_back_button)
back_button.place(x=10,y=10)
R25_syllabus_desp = customtkinter.CTkLabel(master=E_new_frame,height=60,width=520,
                                        fg_color="#765341",
                                        text="This page shows the official information about the syllabus of the ECE R25 regulation course",
                                        font=("Poppins",15),)
R25_syllabus_desp.place(x=10,y=60)
sem1_button_E = customtkinter.CTkButton(master=E_new_frame,height=30,width=90,
                                      text="1st SEM",text_color="#EEE5E0",
                                      fg_color="#6A4A3A",font=("Poppins",17),
                                      hover=True,hover_color="#5B3E31"
                                      )
sem2_button_E = customtkinter.CTkButton(master=E_new_frame,height=30,width=90,
                                      text="2nd SEM",text_color="#EEE5E0",
                                      fg_color="#6A4A3A",font=("Poppins",17),
                                      hover=True,hover_color="#5B3E31"
                                      )
def on_click_first_E():
    """when first year is clicked"""
    sem1_button_E.place(x=210,y=140)
    sem2_button_E.place(x=210,y=175)

first_year_ECE = customtkinter.CTkButton(master=E_new_frame,height=65,width=170,
                                         text=" 1ST YEAR ECE ",text_color="#EEE5E0",
                                         hover=True,hover_color="#5B3E31",
                                         fg_color="#6A4A3A",font=("Poppins",19),
                                         command=on_click_first_E)
first_year_ECE.place(x=20,y=140)
def on_click_second_E():
    """when first year is clicked"""
    sem1_button_E.configure(text="3rd SEM")
    sem1_button_E.place(x=210,y=225)
    sem2_button_E.configure(text="4th SEM")
    sem2_button_E.place(x=210,y=260)
second_year_ECE = customtkinter.CTkButton(master=E_new_frame,height=65,width=170,
                                         text=" 2ND YEAR ECE ",text_color="#EEE5E0",
                                         hover=True,hover_color="#5B3E31",
                                         fg_color="#6A4A3A",font=("Poppins",19),
                                         command=on_click_second_E
                                         )
second_year_ECE.place(x=20,y=225)
def on_click_third_E():
    """when first year is clicked"""
    sem1_button_E.configure(text="5th SEM")
    sem1_button_E.place(x=210,y=310)
    sem2_button_E.configure(text="6th SEM")
    sem2_button_E.place(x=210,y=345)
third_year_ECE = customtkinter.CTkButton(master=E_new_frame,height=65,width=170,
                                         text=" 3RD YEAR ECE ",text_color="#EEE5E0",
                                         hover=True,hover_color="#5B3E31",
                                         fg_color="#6A4A3A",font=("Poppins",19),
                                         command=on_click_third_E)
third_year_ECE.place(x=20,y=310)
def on_click_fourth_E():
    """when first year is clicked"""
    sem1_button_E.configure(text="7th SEM")
    sem1_button_E.place(x=210,y=395)
    sem2_button_E.configure(text="8th SEM")
    sem2_button_E.place(x=210,y=430)
fourth_year_ECE = customtkinter.CTkButton(master=E_new_frame,height=65,width=170,
                                         text=" 4TH YEAR ECE ",text_color="#EEE5E0",
                                         hover=True,hover_color="#5B3E31",
                                         fg_color="#6A4A3A",font=("Poppins",19),
                                         command=on_click_fourth_E)
fourth_year_ECE.place(x=20,y=395)

label_1E = customtkinter.CTkLabel(master=jntuh_frame,text="Electronics and Communication",
                                  text_color="#3D251E",fg_color="#D8CBC4",
                                  font=("Poppins",30))
label_1E.place(x=15,y=220)
label_1E_button = customtkinter.CTkButton(master=jntuh_frame,height=40,width=520,
                                          text="JNTUH Syllabus of ECE course",
                                          fg_color="#8B6C5C",
                                          text_color="#EEE5E0",font=("Poppins",15),
                                          hover=True,hover_color="#5B3E31",
                                          command=ECE_syllabus1
                                          )
label_1E_button.place(x=15,y=260)
A_new_frame = customtkinter.CTkFrame(master=jntuh_frame,height=550, width=64,fg_color="#D8CBC4")
def AIML_syllabus1():
    """the syllabus frame when you click the computer scrience button"""
    A_new_frame.lift()
    A_new_frame.pack(padx=2,pady=2,fill="both")
    A_new_frame.pack_propagate()
def on_click_back_button():
    """when back button is clicked on the new frame"""
    A_new_frame.pack_forget()
    root.lift()
R25_syllabus_label = customtkinter.CTkLabel(master=A_new_frame,height=40,width=470,
                                         text="  R25 syllabus AIML", fg_color="#8B6C5C",text_color="#EEE5E0",
                                         font=("Poppins",19),compound="center",anchor=W)
R25_syllabus_label.place(y=10,x=60)
back_button = customtkinter.CTkButton(master=A_new_frame,height=40,width=40,
                                      text=">",hover=True,hover_color="#5B3E31",
                                      fg_color="#8B6C5C",command=on_click_back_button)
back_button.place(x=10,y=10)
R25_syllabus_desp = customtkinter.CTkLabel(master=A_new_frame,height=60,width=520,
                                        fg_color="#765341",
                                        text="This page shows the official information about the syllabus of the AIML R25 regulation course",
                                        font=("Poppins",15),)
R25_syllabus_desp.place(x=10,y=60)
sem1_button_A = customtkinter.CTkButton(master=A_new_frame,height=30,width=90,
                                      text="1st SEM",text_color="#EEE5E0",
                                      fg_color="#6A4A3A",font=("Poppins",17),
                                      hover=True,hover_color="#5B3E31"
                                      )
sem2_button_A = customtkinter.CTkButton(master=A_new_frame,height=30,width=90,
                                      text="2nd SEM",text_color="#EEE5E0",
                                      fg_color="#6A4A3A",font=("Poppins",17),
                                      hover=True,hover_color="#5B3E31"
                                      )
def on_click_first_A():
    """when first year is clicked"""
    sem1_button_A.place(x=210,y=140)
    sem2_button_A.place(x=210,y=175)

first_year_AIML = customtkinter.CTkButton(master=A_new_frame,height=65,width=170,
                                         text=" 1ST YEAR AIML ",text_color="#EEE5E0",
                                         hover=True,hover_color="#5B3E31",
                                         fg_color="#6A4A3A",font=("Poppins",19),
                                         command=on_click_first_A)
first_year_AIML.place(x=20,y=140)
def on_click_second_A():
    """when first year is clicked"""
    sem1_button_A.configure(text="3rd SEM")
    sem1_button_A.place(x=210,y=225)
    sem2_button_A.configure(text="4th SEM")
    sem2_button_A.place(x=210,y=260)
second_year_AIML = customtkinter.CTkButton(master=A_new_frame,height=65,width=170,
                                         text=" 2ND YEAR AIML ",text_color="#EEE5E0",
                                         hover=True,hover_color="#5B3E31",
                                         fg_color="#6A4A3A",font=("Poppins",19),
                                         command=on_click_second_A
                                         )
second_year_AIML.place(x=20,y=225)
def on_click_third_A():
    """when first year is clicked"""
    sem1_button_A.configure(text="5th SEM")
    sem1_button_A.place(x=210,y=310)
    sem2_button_A.configure(text="6th SEM")
    sem2_button_A.place(x=210,y=345)
third_year_AIML = customtkinter.CTkButton(master=A_new_frame,height=65,width=170,
                                         text=" 3RD YEAR AIML ",text_color="#EEE5E0",
                                         hover=True,hover_color="#5B3E31",
                                         fg_color="#6A4A3A",font=("Poppins",19),
                                         command=on_click_third_A)
third_year_AIML.place(x=20,y=310)
def on_click_fourth_A():
    """when first year is clicked"""
    sem1_button_A.configure(text="7th SEM")
    sem1_button_A.place(x=210,y=395)
    sem2_button_A.configure(text="8th SEM")
    sem2_button_A.place(x=210,y=430)
fourth_year_AIML = customtkinter.CTkButton(master=A_new_frame,height=65,width=170,
                                         text=" 4TH YEAR AIML ",text_color="#EEE5E0",
                                         hover=True,hover_color="#5B3E31",
                                         fg_color="#6A4A3A",font=("Poppins",19),
                                         command=on_click_fourth_A)
fourth_year_AIML.place(x=20,y=395)

label_1A = customtkinter.CTkLabel(master=jntuh_frame,text="Artificial Intelligence and Machine Learning",
                                  text_color="#3D251E",fg_color="#D8CBC4",
                                  font=("Poppins",30))
label_1A.place(x=15,y=310)
label_1A_button = customtkinter.CTkButton(master=jntuh_frame,height=40,width=520,
                                          text="JNTUH Syllabus of AIML course",
                                          fg_color="#8B6C5C",
                                          text_color="#EEE5E0",font=("Poppins",15),
                                          hover=True,hover_color="#5B3E31",
                                          command=AIML_syllabus1
                                          )
label_1A_button.place(x=15,y=350)
#wanted to add more our clg has this much courses only

JNTUH_syllabus_button = customtkinter.CTkButton(master=buttons_frame,width=120,height=140,
                                                text="JNTUH",text_color="#D8CBC4",
                                                anchor=N,
                                                fg_color="#6A4A3A",
                                                hover=True,hover_color="#5B3E31",
                                                font=("Poppins",19),
                                                image=JNTUH_logo_image,compound="bottom",
                                                command=on_click_jntuh)
JNTUH_syllabus_button.place(x=10,y=160)

exam_button = customtkinter.CTkButton(master=buttons_frame,height=140,width=120,
                                      text="Exam \n Dates",text_color="#D8CBC4",
                                       fg_color="#6A4A3A",
                                      hover=True,hover_color="#5B3E31",
                                      font=("Poppins",19))
exam_button.place(x=140,y=160)

another2_button = customtkinter.CTkButton(master=buttons_frame,width=120,height=140,
                                         text="Future\nButton",text_color="#D8CBC4",
                                         fg_color="#6A4a3A",
                                         hover=True,hover_color="#5B3E31",
                                         font=("Poppins",19))
another2_button.place(x=270,y=160)

drawing_frame = customtkinter.CTkFrame(master=root, height=400, width=113,
                                       fg_color="#8B6C5C",
                                       border_width=3, border_color="#4C3228")
drawing_frame.place(x=48,y=100)


is_sidebar_open = False # to track whether menu is open or not

#the sidebar frame
side_bar_frame = customtkinter.CTkFrame(root, 
                                        width=40, corner_radius=0,
                                        fg_color="#8B6C5C")
side_bar_frame.pack(side="left",fill="y")
#Ignore the size of the buttons inside me; stick strictly to the width I assign."
side_bar_frame.pack_propagate(False)

def toggle_sidebar():
    global is_sidebar_open

    if not is_sidebar_open:
        # Expand sidebar width
        side_bar_frame.configure(width=200)
        scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
        toggle_btn.configure(text="<")
        is_sidebar_open = True
    else:
        # Collapse sidebar width
        side_bar_frame.configure(width=40)
        
        # Hide scrollable frame & overlay
        scroll_frame.pack_forget()
        toggle_btn.configure(text=">")
        is_sidebar_open = False
#the button on the side frame
toggle_btn = customtkinter.CTkButton(
    master=side_bar_frame,
    width=30,
    height=30,
    text=">",
    fg_color="#765341",
    hover_color="#BCA89F",
    command=toggle_sidebar
)

toggle_btn.pack(pady=10, padx=5)

scroll_frame = customtkinter.CTkScrollableFrame(side_bar_frame, fg_color="transparent")

menu_label = customtkinter.CTkLabel(master=scroll_frame,height=30,width=195,
                                    text="Menu",text_color="#D8CBC4",fg_color="#4C3228",
                                    font=("Poppins",14)
                                    )
menu_label.pack(pady=10)
find_books_frame = customtkinter.CTkFrame(master=root,height=500,width=500)
def find_books_frame():
    """"""

find_books_button = customtkinter.CTkButton(master=scroll_frame,
                                            height=40,width=180,hover=True,
                                            hover_color="#5B3E31",fg_color="#4C3228",
                                            text="Find Books",text_color="#D8CBC4",
                                            font=("Poppins",14),command=find_books_frame)
find_books_button.pack(pady=1,padx=1)
author_name_button = customtkinter.CTkButton(master=scroll_frame,
                                            height=40,width=180,
                                            hover_color="#5B3E31",fg_color="#4C3228",
                                            text="Author Name",text_color="#D8CBC4",
                                            font=("Poppins",14))
author_name_button.pack(pady=1,padx=1)

subject_button = customtkinter.CTkButton(master=scroll_frame,
                                            height=40,width=180,
                                            hover_color="#5B3E31",fg_color="#4C3228",
                                            text="Subject",text_color="#D8CBC4",
                                            font=("Poppins",14))
subject_button.pack(pady=1,padx=1)

course_button = customtkinter.CTkButton(master=scroll_frame,
                                            height=40,width=180,
                                            hover_color="#5B3E31",fg_color="#4C3228",
                                            text="Course",text_color="#D8CBC4",
                                            font=("Poppins",14))
course_button.pack(pady=1,padx=1)

library_3D_button = customtkinter.CTkButton(master=scroll_frame,
                                            height=40,width=180,
                                            hover_color="#5B3E31",fg_color="#4C3228",
                                            text="Library 3D",text_color="#D8CBC4",
                                            font=("Poppins",14))
library_3D_button.pack(pady=1,padx=1)

feedback_button = customtkinter.CTkButton(master=scroll_frame,
                                            height=40,width=180,
                                            hover_color="#5B3E31",fg_color="#4C3228",
                                            text="FeedBack",text_color="#D8CBC4",
                                            font=("Poppins",14))
feedback_button.pack(pady=1,padx=1)
root.mainloop()