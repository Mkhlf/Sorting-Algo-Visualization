from tkinter import *
from tkinter import ttk
from Sortingalgo import *
import random
import time 

root = Tk()
root.title('Mohammad Alkhlifah Sorting Algorithim Visualization')
root.maxsize(1300,720)
root.config(bg='black')
# var
selected_algo = StringVar()
data  = []
class aa: 
    initial_arr = []
    final_arr = []
    used_algo =""
    s_time=0
    f_time=0
    speedd=0
    def __init__ (self, initial_arr, used_algo, speedd):
        self.initial_arr = initial_arr.copy()
        self.used_algo = used_algo
        self.s_time = time.time()
        self.speedd= speedd
    def done (self, final_arr):
        self.final_arr = final_arr
        self.f_time = time.time()
        f = open("arrInfo.txt", "w")
        f.write("The initial array is : " + str(self.initial_arr) + '\n' + "The final array is : " + str(self.final_arr) + '\n'+ "Taken time : " +  str(self.f_time - self.s_time) + " at speed : "+ str(self.speedd) +"(s)"+ '\n Used algo : ' + str(self.used_algo))
        f.close

def drawData(Data, colorArr):
    canvas.delete('all')
    c_height = 500
    c_width = 1250
    x_width = c_width/ (len (Data)+1)
    offset = 20
    spacing = 10
    normalizedData= [ i  / max(Data) for i in Data]
    for i, height in enumerate(normalizedData):
        ## top left 
        x0= i * x_width + offset + spacing
        y0= c_height - height * 350
        ## bottom right 
        x1= (i+1) * x_width +offset
        y1 = c_height

        canvas.create_rectangle (x0,y0, x1,y1,fill =colorArr[i])
        canvas.create_text(x0 +2, y0 , anchor = SW, text = str(Data[i]))
    root.update_idletasks()

def Startalgo ():
    global data
    if not data: return
    timee = speedScale.get()
    arr1 = aa(data,selected_algo.get(), timee)
    if (selected_algo.get() == 'Bubble Sort'):
        bubble_sort (data , drawData, timee)
        arr1.done(data)
    elif selected_algo.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timee)
        # print (data)
        drawData (data, ['green' for x in range (len (data))])
        arr1.done(data)
def Generate ():
    global data
    # print ('slected algo is : '+ selected_algo.get())
    minval = minvalEntry.get()
    maxval = maxvalEntry.get()
    size = sizeEntry.get()
    if minval > maxval :
        minval, maxval = maxval, minval
    data = []
    for x in range (size):
        data.append(random.randrange(minval, maxval+1))
    drawData (data, ['red' for x in range (len (data))])
# fram / base layout
UI_frame = Frame(root, width = 1280, height = 200, bg = 'grey')
UI_frame.grid (row =0, column = 0, padx = 10, pady =5)

canvas = Canvas(root, width = 1280, height = 500, bg = 'white')
canvas.grid (row =1 , column =0, padx = 10, pady =5)

# UI area
# row 0 
Label (UI_frame, text ='Algorithim', bg ='grey').grid(row =0, column =0, padx =5, pady =5, sticky = W)
algMenu = ttk.Combobox (UI_frame, textvariable = selected_algo, values = ['Bubble Sort', 'Quick Sort'])
algMenu.grid(row =0, column = 1 , padx = 5, pady = 5)
algMenu.current(0)

speedScale = Scale (UI_frame, from_ = 0.01 , to =2, length = 200, digits = 3 , resolution = 0.01, orien = HORIZONTAL, label = "Select Speed [s]")
speedScale.grid (row = 0, column = 2, padx =5, pady = 5)
Button (UI_frame, text = 'Start', command = Startalgo, bg = 'red').grid (row =0, column =3, padx =5 , pady=5)

##
#####################################
# row 1 
sizeEntry= Scale (UI_frame, from_ = 3 , to =100, length = 250, resolution = 1, orien = HORIZONTAL, label = "Size: ")
sizeEntry.grid (row= 1, column =0, padx =5, pady =5)
##
minvalEntry = Scale (UI_frame, from_ = 0 , to =1000, length = 250,resolution = 1, orien = HORIZONTAL, label = "Min Value: ")
minvalEntry.grid (row= 1, column =1, padx =5, pady =5)
##
maxvalEntry= Scale (UI_frame, from_ = 0 , to =1000, length = 250, resolution = 1, orien = HORIZONTAL, label = "Max Value: ")
maxvalEntry.grid (row= 1, column =2, padx =5, pady =5)

Button (UI_frame, text = 'Generate', command = Generate, bg = 'white').grid (row =1, column =3, padx =5 , pady=5)




root.mainloop()