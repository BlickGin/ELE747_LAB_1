import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use("TkAgg")
import tkinter as tk
from tkinter import messagebox

import numpy as np
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import figure
from matplotlib import axes
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


def draw_graph(frame, error_values):
    fig = plt.figure(1)
    plt.ion()
    t = list(range(0, len(error_values)))
    s = error_values
    plt.plot(t, s)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    plot_widget = canvas.get_tk_widget()

    plot_widget.grid(row=0, column=0)
    tk.mainloop()


class Application:
    def __init__(self, master):
        self.nb_of_networks = 0
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('Gui.ui')

        self.builder2 = builder2 = pygubu.Builder()
        self.builder2.add_from_file('Gui.ui')

        self.mainwindow = builder.get_object('Toplevel_2', master)
        builder.connect_callbacks(self)
        master.protocol("WM_DELETE_WINDOW", self.on_close_window)

        # Gère la sélection d'un item dans la liste
        def curselect(event):
            widget = event.widget
            selection = widget.curselection()
            picked = widget.get(selection[0])
            net = load(picked)
            txt = "Nom : " + net.name + "\n\r" \
                                        "Nombre de couches : " + str(net.nb_couches) + "\n\r" \
                                                                                       "Config [Entrées, C1, C2, ..., Cn, Sorties] : " + str(
                net.nb_unit_par_couche) + " \n\r" \
                                          "Type d'activation : " + str(net.acti_type)

            self.netinfos_label.config(text=txt)
            print(net.nb_unit_par_couche)
            draw_graph(frame_13, net.error_count)

        self.networks_listbox = net_lbox = builder.get_object('Network_list')
        self.networks_listbox.bind('<<ListboxSelect>>', curselect)

        self.netinfos_label = net_infos = builder.get_object('Network_Infos')

        # self.graph_win = graph_win = builder.get_object('Graphics')
        # graph_win.pack()

        self.frame_13 = frame_13 = builder.get_object('Frame_13')

        self.list_of_networks = {}
        self.list_of_networks_name = 'Network_List.pkl'
        builder.connect_callbacks(self)

        self.list_of_networks = load(self.list_of_networks_name)
        self.nb_of_networks = len(self.list_of_networks)

        net_lbox.select_clear(tk.END)
        for i in self.list_of_networks:
            text = i
            net_lbox.insert(tk.END, text)
        net_lbox.see(tk.END)
        net_lbox.selection_set(tk.END)

    def on_close_window(self, event=None):
        print("closed")
        self.mainwindow.master.destroy()
        exit()

    def on_new_network_click(self):
        top3 = tk.Toplevel(self.mainwindow)

        frame3 = self.builder2.get_object('New_Network_Window', top3)
        self.builder2.connect_callbacks(self)

    def on_ok_click(self):
        good_data = False

        name_input = 0
        nb_layers = 0
        nb_unit_per_layer = 0
        nb_input = 0
        nb_output = 0

        name_input_entry = self.builder2.get_object('Network_Name_Entry')
        nb_layers_entry = self.builder2.get_object('Number_Of_Layer_Entry')
        nb_unit_per_layer_entry = self.builder2.get_object('Number_Of_Unit_Entry')
        nb_input_entry = self.builder2.get_object('Number_Of_Inputs_Entry')
        nb_output_entry = self.builder2.get_object('Number_Of_Outputs_Entry')
        acti_type_entry = self.builder2.get_object('Acti_Type_Menu_Button')
        name_input = name_input_entry.get()
        nb_layers = nb_layers_entry.get()
        nb_unit_per_layer = nb_unit_per_layer_entry.get()
        nb_input = nb_input_entry.get()
        nb_output = nb_output_entry.get()
        acti_type = acti_type_entry.selection_get()
        print(acti_type)

        nb_unit_per_layer = nb_unit_per_layer.split(",")

        try:
            nb_layers = int(nb_layers)
            try:
                for i in nb_unit_per_layer:
                    i = int(i)
                try:
                    nb_input = int(nb_input)
                    try:
                        nb_output = int(nb_output)
                        good_data = True
                    except ValueError:
                        messagebox.showwarning("Wrong Type Entry", "Please enter an integer for the number of outputs")
                except ValueError:
                    messagebox.showwarning("Wrong Type Entry", "Please enter an integer for the number of inputs")
            except ValueError:
                messagebox.showwarning("Wrong Type Entry",
                                       "Please enter only integers for the number of units per layers")
        except ValueError:
            messagebox.showwarning("Wrong Type Entry", "Please enter an integer for the number of layers")

        if good_data is True:
            if nb_layers is not len(nb_unit_per_layer):
                messagebox.showwarning("Wrong Type Entry",
                                       "Please enter exactly " + str(nb_layers) + " layers in number of layers")
            elif name_input is "":
                messagebox.showwarning("Wrong Type Entry", "Please enter a name")
            else:
                print("OK")
    # def on_new_network_click(self):
    #     d = Dialog(root, "Nom")
    #     root.wait_window(d.top)
    #     name = d.return_value
    #     val = None
    #     while type(val) is not int:
    #         d = Dialog(root, "Nombre de couches")
    #         root.wait_window(d.top)
    #         try:
    #             val = int(d.return_value)
    #         except ValueError:
    #             val = None
    #
    #     nb_couches = int(val)
    #     nb_unit_par_couche = []
    #     val = None
    #     for i in range(nb_couches + 1):
    #         if i == 0:
    #             while type(val) is not int:
    #                 d = Dialog(root, "Nombre d'entrées")
    #                 root.wait_window(d.top)
    #                 try:
    #                     val = int(d.return_value)
    #                 except ValueError:
    #                     val = None
    #             nb_unit_par_couche.append(val)
    #             val = None
    #         else:
    #             if i is nb_couches:
    #                 txt = "Nombre d'unités à la couche " + str(i) + " (Sortie)"
    #                 while type(val) is not int:
    #                     d = Dialog(root, txt)
    #                     root.wait_window(d.top)
    #                     try:
    #                         val = int(d.return_value)
    #                     except ValueError:
    #                         val = None
    #
    #                 nb_unit_par_couche.append(val)
    #                 val = None
    #             else:
    #                 txt = "Nombre d'unités à la couche " + str(i)
    #                 while type(val) is not int:
    #                     d = Dialog(root, txt)
    #                     root.wait_window(d.top)
    #                     try:
    #                         val = int(d.return_value)
    #                     except ValueError:
    #                         val = None
    #                 nb_unit_par_couche.append(val)
    #                 val = None
    #
    #     d = Dialog(root, "Activation Type (Enter number between 1 and 7) \n"
    #                      "0 : SIGMOID\n"
    #                      "1 : TANH\n"
    #                      "2 : SIN\n"
    #                      "3 : STEP\n"
    #                      "4 : RAMP\n"
    #                      "5 : RELU\n"
    #                      "6 : GAUSS")
    #     root.wait_window(d.top)
    #     acti = d.return_value
    #
    #     net = Network()
    #     net.nb_unit_par_couche = nb_unit_par_couche
    #     net.nb_couches = nb_couches
    #     net.acti_type = acti
    #     net.name = name
    #
    #     net.init()
    #     self.nb_of_networks += 1
    #     fname = "Network_" + str(self.nb_of_networks) + ".pkl"
    #     self.list_of_networks += [fname]
    #     save(net, fname)
    #     save(self.list_of_networks, self.list_of_networks_name)
    #
    #     self.networks_listbox.delete(0, tk.END)
    #     self.networks_listbox.select_clear(tk.END)
    #     for i in range(self.nb_of_networks):
    #         text = self.list_of_networks[i]
    #         self.networks_listbox.insert(tk.END, text)
    #     self.networks_listbox.see(tk.END)
    #     self.networks_listbox.selection_set(tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

