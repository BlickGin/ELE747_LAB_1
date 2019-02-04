from graphics import *


class Drawing(object):
    def __init__(self, network):
        self.network = network
        self.win_length = 800
        self.win_heigth = 500
        self.points = [[]]
        self.inputs_rect = []
        self.node_cir = [[]]
        self.id_label = [[]]
        self.gene_line = [[[]]]
        self.win = GraphWin('test', self.win_length, self.win_heigth)

    def draw_network(self):
        self.win.focus_force()
        self.win.flush()
        # self.win = GraphWin('test', self.win_length, self.win_heigth)
        div_lenght = self.win_length / (self.network.nb_couches + 2)
        for i in range(self.network.nb_unit_par_couche[0]):
            div_height = self.win_heigth / (self.network.nb_unit_par_couche[0] + 1)
            pt = Point(div_lenght, (div_height * (i+1)))
            self.points[0].append(pt)

            pt1 = Point(div_lenght-20, (div_height * (i+1))-20)
            pt2 = Point(div_lenght+20, (div_height * (i+1))+20)
            rec = Rectangle(pt1, pt2)
            rec.setFill(color_rgb(200, 200, 200))
            self.inputs_rect.append(rec)

        for i in range(self.network.nb_couches):
            div_height = self.win_heigth / (self.network.nb_unit_par_couche[i+1] + 1)
            self.points.append([])
            self.id_label.append([])
            self.node_cir.append([])
            self.gene_line.append([])

            for j in range(self.network.nb_unit_par_couche[i+1]):
                pt = Point(div_lenght * (i+2), div_height * (j+1))
                self.points[i+1].append(pt)
                name = self.network.couches[i][j].unit_id
                cir = Circle(pt, 25)
                label = Text(pt, name)
                cir.setFill(color_rgb(200, 200, 200))
                self.id_label[i].append(label)
                self.node_cir[i].append(cir)
                self.gene_line[i].append([])

                for k in range(self.network.couches[i][j].nb_input):
                    gene = Line(self.points[i][k], self.points[i+1][j])
                    gene.setWidth(10)
                    color = color_rgb(0, 10, 250)
                    if self.network.couches[i][j].weights[k] < 0:
                        color = color_rgb(200, 10, 10)

                    width = abs(float(self.network.couches[i][j].weights[k]))
                    gene.setWidth(width)
                    gene.setFill(color)
                    self.gene_line[i][j].append(gene)

        for i in range(len(self.gene_line)):
            for j in range(len(self.gene_line[i])):
                for k in self.gene_line[i][j]:
                    k.undraw()
                    k.draw(self.win)

        for i in self.inputs_rect:
            i.undraw()
            i.draw(self.win)

        for i in range(self.network.nb_couches):
            for j in self.node_cir[i]:
                j.undraw()
                j.draw(self.win)


