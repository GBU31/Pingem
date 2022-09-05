import tkinter as tk
from core.isconnected import IsConnected
from core.settings.settingsApp import  *
import os
from datetime import datetime
from scapy.all import srp,Ether,ARP,conf 

    

class App(SettingsApp):
    def ping(self):
        if IsConnected(self.e1.get()).isconnected():
            self.zenity(msg=f"{self.e1.get()} is connected !")


    def notify(self, msg, **kwargs):
        os.system(f'notify-send -u low "{msg}" ')

    def zenity(self, msg, **kwargs):
        os.system(f'zenity --info --title="Show All" --text="{msg}" --no-wrap')

    
    def Show_All(self):

        start_time = datetime.now()

        conf.verb = 0 
        try:
            ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = self.settings_file()[0]), 
                    timeout = 2, 
                    iface = self.settings_file()[1],
                    inter = 0.1)
        except Exception as err:
            self.notify(msg=err)
            


        output = "\n IP - MAC\n"
        for snd,rcv in ans: 
            output += rcv.sprintf(r"%ARP.psrc% - %Ether.src%\n")
        stop_time = datetime.now()
        total_time = stop_time - start_time 
        output += f"\n[*] Scan Complete. Duration: {total_time}"
        os.system(f'zenity --info --title="Show All" --text="{output}" --no-wrap')

    def run_app(self):
        master = tk.Tk()
        master.title("PingHim")
        tk.Label(master, text="ip").grid(row=0)
        master.geometry('400x150')


        self.e1 = tk.Entry(master)

        self.e1.insert(10, "127.0.0.1")

        self.e1.grid(row=0, column=1)

        tk.Button(master,
                text='Quit', 
                command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
        tk.Button(master, text='Run', command=self.ping).grid(row=3, column=1,  sticky=tk.W, pady=4)
        tk.Button(master, text='Show All', command=self.Show_All).grid(row=3, column=2,  sticky=tk.W, pady=4)
        tk.Button(master, text='Settings', command=SettingsApp().run_app).grid(row=4, column=2,  sticky=tk.W, pady=4)

        master.mainloop()


if __name__ == '__main__':
    App().run_app()
