import tkinter
import hilbert


w = h = 640

h256 = hilbert.HilbertCurve(256)

scalex = w / h256.width
scaley = h / h256.height
scale = min(scalex, scaley)


master = tkinter.Tk()
canvas = tkinter.Canvas(master, width=h256.width*scale, height=h256.height*scale)
canvas.pack()


for d in h256.range():
    x,y = h256[d]
    color = '#{:02x}{:02x}{:02x}'.format(d,d,d)
    canvas.create_rectangle(x*scale,y*scale,(x+1)*scale,(y+1)*scale,fill=color)

tkinter.mainloop()
