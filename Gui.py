import tkinter as tk
import pygubu
from save_load import *
from Network import *


class Dialog:
    def __init__(self, master, text):
        top = self.top = tk.Toplevel(master)
        self.return_value = 0

        tk.Label(top, text=text).pack()

        self.e = tk.Entry(top)
        self.e.pack(padx=5)

        b = tk.Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        self.return_value = self.e.get()
        self.top.destroy()


class Application:
    def __init__(self, master):
        self.nb_of_networks = 0
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('Gui.ui')
        self.mainwindow = builder.get_object('Toplevel_2', master)
        self.dict_of_networks = {}
        self.dict_of_networks_name = 'Network_List.pkl'
        builder.connect_callbacks(self)

        load(self.dict_of_networks_name)

    def on_new_network_click(self):
        val = None
        while type(val) is not int:
            d = Dialog(root, "Nombre de couches")
            root.wait_window(d.top)
            try:
                val = int(d.return_value)
            except ValueError:
                val = None

        nb_couches = int(val)
        nb_unit_par_couche = []
        val = None
        for i in range(nb_couches + 1):
            if i == 0:
                while type(val) is not int:
                    d = Dialog(root, "Nombre d'entrées")
                    root.wait_window(d.top)
                    try:
                        val = int(d.return_value)
                    except ValueError:
                        val = None
                nb_unit_par_couche.append(val)
                val = None
            else:
                if i is nb_couches:
                    txt = "Nombre d'unités à la couche " + str(i) + " (Sortie)"
                    while type(val) is not int:
                        d = Dialog(root, txt)
                        root.wait_window(d.top)
                        try:
                            val = int(d.return_value)
                        except ValueError:
                            val = None

                    nb_unit_par_couche.append(val)
                    val = None
                else:
                    txt = "Nombre d'unités à la couche " + str(i)
                    while type(val) is not int:
                        d = Dialog(root, txt)
                        root.wait_window(d.top)
                        try:
                            val = int(d.return_value)
                        except ValueError:
                            val = None
                    nb_unit_par_couche.append(val)
                    val = None

        d = Dialog(root, "Activation Type (Enter number between 1 and 7) \n"
                         "0 : SIGMOID\n"
                         "1 : TANH\n"
                         "2 : SIN\n"
                         "3 : STEP\n"
                         "4 : RAMP\n"
                         "5 : RELU\n"
                         "6 : GAUSS")
        root.wait_window(d.top)
        acti = d.return_value

        net = Network()
        net.nb_unit_par_couche = nb_unit_par_couche
        net.nb_couches = nb_couches
        net.acti_type = acti

        net.init()
        self.nb_of_networks += 1
        fname = "Network_" + str(self.nb_of_networks) + ".pkl"
        self.dict_of_networks[fname] = net
        save(net, fname)




if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)

    root.mainloop()

