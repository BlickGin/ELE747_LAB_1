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
import pickle
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
        self.frame_3 = None

        self.mainwindow = builder.get_object('Toplevel_2', master)
        builder.connect_callbacks(self)
        master.protocol("WM_DELETE_WINDOW", self.on_close_window)

        self.selected_acti_type = 0

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
                                          "Type d'activation : " + str(net.acti_type) + "\n\r" \
                                        "Fichier de données : " + str(net.datafile)

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
        self.builder2 = builder2 = pygubu.Builder()
        self.builder2.add_from_file('Gui.ui')
        top3 = tk.Toplevel(self.mainwindow)
        self.selected_acti_type = None

        self.frame_3 = self.builder2.get_object('New_Network_Window', top3)
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
        data_path_entry = self.builder2.get_object('Data_File_Input')

        name_input = name_input_entry.get()
        nb_layers = nb_layers_entry.get()
        nb_unit_per_layer = nb_unit_per_layer_entry.get()
        nb_input = nb_input_entry.get()
        data_path = data_path_entry.cget('path')
        acti_type = self.selected_acti_type

        nb_unit_per_layer = nb_unit_per_layer.split(",")

        try:
            nb_layers = int(nb_layers)
            try:
                for i in range(len(nb_unit_per_layer)):
                    nb_unit_per_layer[i] = int(nb_unit_per_layer[i])
                try:
                    nb_input = int(nb_input)
                    good_data = True
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
            elif self.selected_acti_type is None:
                messagebox.showwarning("Wrong Type Entry", "Please select an activation")
            elif data_path is "":
                messagebox.showwarning("Wrong Type Entry", "Please select path to data files")
            else:
                print(name_input)
                print(nb_layers)
                print(nb_unit_per_layer)
                print(nb_input)
                print(nb_output)
                print(acti_type)
                net = Network()
                net.name = name_input
                net.nb_unit_par_couche = nb_unit_per_layer
                net.nb_unit_par_couche.insert(0, nb_input)
                net.nb_couches = nb_layers
                net.acti_type = self.selected_acti_type
                net.datafile = data_path

                net.init()
                self.nb_of_networks += 1
                fname = "Network_" + str(self.nb_of_networks) + ".pkl"
                self.list_of_networks[fname] = name_input
                save(net, fname)
                save(self.list_of_networks, self.list_of_networks_name)

                self.networks_listbox.delete(0, tk.END)
                self.networks_listbox.select_clear(tk.END)
                for i in self.list_of_networks:
                    text = i
                    self.networks_listbox.insert(tk.END, text)
                self.networks_listbox.see(tk.END)
                self.networks_listbox.selection_set(tk.END)

                self.frame_3.master.destroy()

    def on_Acti(self, selection):
        if selection == 'Acti_Type_0':
            self.selected_acti_type = ACTI_TYPE_SIGMOID
        elif selection == 'Acti_Type_1':
            self.selected_acti_type = ACTI_TYPE_TANH
        elif selection == 'Acti_Type_2':
            self.selected_acti_type = ACTI_TYPE_SIN
        elif selection == 'Acti_Type_3':
            self.selected_acti_type = ACTI_TYPE_STEP
        elif selection == 'Acti_Type_4':
            self.selected_acti_type = ACTI_TYPE_RAMP
        elif selection == 'Acti_Type_5':
            self.selected_acti_type = ACTI_TYPE_RELU
        elif selection == 'Acti_Type_6':
            self.selected_acti_type = ACTI_TYPE_GAUSS

    def on_click_learn_button(self):
        Dialog(self, "Nombre d'époques")
        # vc_error = 10
        # while vc_error > 2:
        #     shuffled_input_train = inputs_train[:]
        #     shuffle(shuffled_input_train)
        #     shuffled_input_vc = inputs_vc[:]
        #     shuffle(shuffled_input_vc)
        #
        #     for i in range(nb_epoch):
        #         error = 0
        #         for j in shuffled_input_train:
        #             n.inputs = j
        #             n.outputs = output_train[inputs_train.index(j)]
        #             n.predict()
        #             n.train()
        #             # print("in : " + str(j) + " / out : " + str(n.couches[-1][0].acti) + ", " + str(n.couches[-1][1].acti) +
        #             #       " / (expexted " + str(n.outputs) + ")")
        #             out = [n.couches[-1][0].acti, n.couches[-1][1].acti]
        #
        #             if out.index(max(out)) is not n.outputs.index(max(n.outputs)):
        #                 error += 1
        #
        #         print(str(i) + " : " + str(error))
        #
        #         # if i % 50 is 0:
        #         #     d.win.flush()
        #         #     d.draw_network()
        #
        #     vc_error = 0
        #     for j in shuffled_input_vc:
        #         n.inputs = j
        #         n.outputs = output_vc[inputs_vc.index(j)]
        #         n.predict()
        #
        #         out = [n.couches[-1][0].acti, n.couches[-1][1].acti]
        #         if out.index(max(out)) is not n.outputs.index(max(n.outputs)):
        #             vc_error += 1
        #     print("VC Errors : " + str(vc_error))

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
