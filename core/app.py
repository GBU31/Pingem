import tkinter as tk
from core.isconnected import IsConnected
import os
from datetime import datetime
from scapy.all import srp,Ether,ARP,conf 

    

class App:
    def ping(self):
        def notify():
            msg = f"{self.e1.get()} is connected !"
            os.system(f'zenity --info --title="Show All" --text="{msg}" --no-wrap')
            # os.system(f'notify-send -u critical "{msg}" ')

        if IsConnected(self.e1.get()).isconnected():
            notify()

    def Show_All(self, interface='wlp36s0b1', ips='192.168.1.0/24'):
        
        start_time = datetime.now()

        conf.verb = 0 
        try:
            ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), 
                    timeout = 2, 
                    iface = interface,
                    inter = 0.1)
        except:
            os.system(f'notify-send -u low "Permission Error" ')


        output = "\n[*] IP - MAC\n"
        for snd,rcv in ans: 
            output += rcv.sprintf(r"%ARP.psrc% - %Ether.src%\n")
        stop_time = datetime.now()
        total_time = stop_time - start_time 
        output += f"\n[*] Scan Complete. Duration: {total_time}"
        os.system(f'zenity --info --title="Show All" --text="{output}" --no-wrap')

    def run_app(self):
        master = tk.Tk()
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

        master.mainloop()


if __name__ == '__main__':
    App().run_app()