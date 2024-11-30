from tkinter import*
import time
from winsound import*
from playsound import playsound
#creating main application window
r=Tk()
r.title("Alarm Clock")
r.geometry('450x450')

#1st usage
class AlarmApp:
    def __init__(self):
        #creating and placing UI elements
        title=Label(r,text="Alarm Clock",font=('Helvetica',22,'bold'))
        title.grid(row=0,column=2,pady=10)
        
        current_date=time.strftime("%a,%d %b,%Y")
        
        date_label=Label(r,background="black",foreground="cyan",font=("Arial",16,"bold"),relief="flat",anchor="center")
        date_label.grid(row=1,column=2,pady=5)
        date_label.configure(text=current_date)
        
        self.clock_label=Label(r,background="magenta4",foreground="yellow",font=("Arial",16,"bold"),relief="flat",anchor="center")
        self.clock_label.grid(row=2,column=2,pady=10)
        self.update_time()
        
        alarm_name_l=Label(r,text="Alarm Name",foreground="maroon",font=('Helvetica',14,'bold'))
        alarm_name_l.grid(row=3,column=1,pady=10)
        
        alarm_time_l=Label(r,text="HH:MM:SS",foreground="maroon",font=('Helvetica',14,'bold'))
        alarm_time_l.grid(row=4,column=1,pady=10)
        
        self.AlarmName=Entry(r,justify='center',width=16,font=('Helvetica',12),bd=4)
        self.AlarmName.grid(row=3,column=2,padx=10)
        
        self.InputAlarm=Entry(r,justify='center',width=16,font=('Helvetica',12),bd=4)
        self.InputAlarm.grid(row=4,column=2,padx=20)
        
        set_alarm=Button(r,text="Set Alarm",command=self.set_alarm,width=10,bg='green',fg='white',font=('Helvetica',12,'bold'))
        set_alarm.grid(row=5,column=2,pady=10)
        
        self.status=Label(r,text="",font=("Helvetica",12,"bold"))
        self.status.grid(row=6,column=2,pady=10)
        
        stop_alarm=Button(r,text="Dismiss",command=self.stop_alarm,width=10,bg='red',fg='white',font=('Helvetica',12,'bold'))
        stop_alarm.grid(row=7,column=2,pady=10)
        
        close_btn=Button(r,text="Close",command=r.destroy,width=10,bg='dark blue',fg='white',font=('Helvetica',12,'bold'))
        close_btn.grid(row=7,column=3)
        
    def set_alarm(self):
        alarm_time=self.InputAlarm.get()
        alarm_name=self.AlarmName.get()
        local_time=time.strftime("%H:%M:%S")
        while local_time!=alarm_time:
            local_time=time.strftime("%H:%M:%S")
            r.update()
        self.status.config(text="Alarm:"+alarm_name)
        playsound('alarm.mp3',SND_LOOP|SND_ASYNC)

    def stop_alarm(self):
        playsound(None,SND_FILENAME)

    def update_time(self):
        cur_time=time.strftime('%H:%M:%S')
        self.clock_label.config(text=cur_time)
        self.clock_label.after(1000,self.update_time)

app=AlarmApp()

r.mainloop()