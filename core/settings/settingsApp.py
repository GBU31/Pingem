import tkinter as tk
import json

class SettingsApp:
    def change(self):
        hm = {"interface":self.interface.get(), "ips":self.ips.get()}
        f = open('settings.json', 'w')
        d = json.dumps(hm)
        f.write(d)
        f.close

    def settings_file(self):
        f = open('settings.json', 'r')
        l = json.loads(f.read())
        f.close()
        return l['ips'], l['interface']
        
        
    def run_app(self):

        master = tk.Tk()
        master.title("Settings")
        tk.Label(master, text="ips").grid(row=0)
        tk.Label(master, text="interface").grid(row=1)

        master.geometry('400x250')


        self.ips = tk.Entry(master)
        self.ips.insert(10, self.settings_file()[0])
        self.ips.grid(row=0, column=1)

        self.interface = tk.Entry(master)
        self.interface.insert(10, self.settings_file()[1])
        self.interface.grid(row=1, column=1)

        # tk.Button(master,
        #         text='Quit',
        #         command=master.quit).grid(row=6, column=2, sticky=tk.W, pady=4)
        tk.Button(master, text='Change', command=self.change).grid(row=5, column=2,  sticky=tk.W, pady=5)

        master.mainloop()

if __name__ == '__main__':
    SettingsApp().run_app()