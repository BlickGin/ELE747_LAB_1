from input_data import *
import numpy as np
from Network import *
from Defines import *
from Dataset import *
from random import shuffle
from save_load import *
# from Gui import *
from tkinter import *
from tkinter import filedialog

# save = Tk()
# save.withdraw()
# save.filename = filedialog.askdirectory(initialdir="/", title="Select Directory")
#
# openf = Tk()
# openf.withdraw()
# openf.filename = filedialog.askopenfilename(initialdir="/", title="Select file")

# print(root.filename)
# f = open(root.filename)
# print(f.read())
# f.flush()
# f.close()
# file_path = filedialog.askopenfilename()
# file = filedialog.askopenfile("r")
#
# file.writelines("test ecriture")
# filedialog.asksaveasfile(file)

# print(file_path)
# f = open(file_path, "w+")
# for i in range(10):
#     f.write("This is line %d\r\n" % (i+1))
#
# f.close()


nb_epoch = 10

n = Network()
# d = Drawing(n)
n.acti_type = ACTI_TYPE_SIGMOID

n.setup()
n.init()

shuffled_input_train = readfile('data_train.csv', STATIC_60)
print("finished reading")
# shuffled_input_vc = readfile('data_vc.csv', STATIC_60)
# shuffled_input_test = readfile('data_test.csv', STATIC_60)

# d.draw_network()

# vc_error = 10
# while vc_error > 2:
#     shuffled_input_train = inputs_train[:]
#     shuffle(shuffled_input_train)
#     shuffled_input_vc = inputs_vc[:]
#     shuffle(shuffled_input_vc)
#
for i in range(nb_epoch):
        error = 0
        count = 1
        for j in shuffled_input_train:
            n.inputs = j[1:]
            n.outputs = j[0]
            n.predict()
            n.train()
            # print("in : " + str(j) + " / out : " + str(n.couches[-1][0].acti) + ", " + str(n.couches[-1][1].acti) +
            #       " / (expexted " + str(n.outputs) + ")")
            out = []
            for h in range(10):
                out.append(n.couches[-1][h].acti)

            if out.index(max(out)) is not n.outputs.index(max(n.outputs)):
                error += 1
            # print("Trainig succesful, weight: ")
            print(str(count) + " / " + str(len(shuffled_input_train)))
            count += 1

        print(str(i) + " : " + str(error))

        print(n.outputs)
        print(out)
        random.shuffle(shuffled_input_train)
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
#
# print("_______________________________________________________________________________________")
# for i in input_test:
#     n.inputs = i
#     n.predict()
#     if n.couches[-1][0].acti > n.couches[-1][1].acti:
#         if i[1] + i[0] > 5:
#             print("in : " + str(i) + " / trouvé plus que 5 (vraiment plus que 5)")
#         else:
#             print("in : " + str(i) + " / trouvé plus que 5 (ERREUR)")
#     else:
#         if i[1] + i[0] < 5:
#             print("in : " + str(i) + " / trouvé moins que 5 (vraiment moins que 5)")
#         else:
#             print("in : " + str(i) + " / trouvé moins que 5 (ERREUR)")

