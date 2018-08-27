from Tkinter import *
import RPi.GPIO as GPIO
root=Tk()

pi_s=StringVar()
md=StringVar()
pi_s.set('17')
md.set('High')
def sw_t(pin_id,val):
    GPIO.setup(int(pin_id),GPIO.OUT)
    if val.lower()=='on' or val=='1'or val.lower()=='high':
        GPIO.output(int(pin_id),GPIO.HIGH)
    elif val.lower()=='off' or val=='0'or val.lower()=='low':
        GPIO.output(int(pin_id),GPIO.LOW)

pin_sel=OptionMenu(root,pi_s,'17','18','27','22','23','24','25','5','6','13','19','26','21','20','16','12')
pin_sel.grid(column=1,row=1)

mode_sel=OptionMenu(root,md,'High','Low')
mode_sel.grid(column=3,row=1)

Button(root,text='Set',command=lambda: sw_t(pi_s.get(),md.get())).grid(column=4,row=1)
Label(root,text='Pin Number(Board)').grid(column=0,row=1)
Label(root,text='Value').grid(column=2,row=1)
Label(root,text='Change Value').grid(column=0,row=0)
GPIO.setmode(GPIO.BCM)
root.mainloop()
GPIO.cleanup()
