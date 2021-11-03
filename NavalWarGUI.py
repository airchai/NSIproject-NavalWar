import tkinter as tk

def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, 333, 33):
        c.create_line([(i, 0), (i, 333)], tag='grid_line')
    

    # Creates all horizontal lines at intevals of 100
    for i in range(0, 333, 33):
        c.create_line([(0, i), (333, i)], tag='grid_line')

    # Creates all vertical lines at intevals of 100
    for i in range(500, 833, 33):
        c.create_line([(i, 0), (i, 333)], tag='grid_line')
    

    # Creates all horizontal lines at intevals of 100
    for i in range(500, 833, 33):
        i=i-500
        c.create_line([(500, i), (833, i)], tag='grid_line')

def create_circle(x, y, r, canvasName,color): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill=color)

root = tk.Tk()

c = tk.Canvas(root, height=1000, width=1000, bg='LightBlue1')
c.pack(fill=tk.BOTH, expand=False)


c.bind('<Configure>', create_grid,)
create_circle(16.5, 314.5, 14, c,"black")

#CODER CONVERTISSEUR CASE VERS POSITION VERS
# + INTEGRATION

root.mainloop()