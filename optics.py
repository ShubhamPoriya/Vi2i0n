from tkinter import *
from PIL import ImageTk,Image

root = Tk()

#making a title and icon for window
root.title(string="VISION ACUITY SYSTEM")
root.iconbitmap(r"/Users/adadelcid/Documents/MakeUC_Hackathon/Tkinter_app/iconfinder_glasses-eye-vision-search-look_3209345.ico")


image1 = ImageTk.PhotoImage(Image.open(r"/Users/adadelcid/Documents/MakeUC_Hackathon/Tkinter_app/E_20_200.png"))
image2 = ImageTk.PhotoImage(Image.open(r"/Users/adadelcid/Documents/MakeUC_Hackathon/Tkinter_app/FP_20_100.png"))
image3 = ImageTk.PhotoImage(Image.open(r"/Users/adadelcid/Documents/MakeUC_Hackathon/Tkinter_app/TOZ_20_70.png"))
image4 = ImageTk.PhotoImage(Image.open(r"/Users/adadelcid/Documents/MakeUC_Hackathon/Tkinter_app/LPED_20_50.png"))
image5 = ImageTk.PhotoImage(Image.open(r"/Users/adadelcid/Documents/MakeUC_Hackathon/Tkinter_app/PECFD_20_40.png"))
image6 = ImageTk.PhotoImage(Image.open(r"/Users/adadelcid/Documents/MakeUC_Hackathon/Tkinter_app/EDFCZP_20_30.png"))
image7 = ImageTk.PhotoImage(Image.open(r"/Users/adadelcid/Documents/MakeUC_Hackathon/Tkinter_app/FELOPZD_20_25.png"))
image8 = ImageTk.PhotoImage(Image.open(r"/Users/adadelcid/Documents/MakeUC_Hackathon/Tkinter_app/DEFPOTEC_20_20.png"))




img_list = [image1, image2, image3, image4, image5, image6, image7, image8]

status = Label(root, text = "Stage 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

my_label = Label(image = image1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_num):
    global my_label
    global button_forward

    my_label.grid_forget()
    my_label = Label(image = img_list[image_num - 1])
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward = Button(root, text = "Next Stage >>", command = lambda: forward(image_num+1))

    status = Label(root, text = "Stage " + str(image_num) +  "of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
    if image_num > 7 :
        button_forward = Button(root, text = "Next Stage >>", state = DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    


button_forward = Button(root, text = "Next Stage >>", command = lambda: forward(2))
button_quit = Button(root, text = "Exit Program", command = root.quit)

button_forward.grid(row=1, column=2, pady = 10)
button_quit.grid(row=1, column=1)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()