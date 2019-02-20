import time

nb2output = {0.0: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             1.0: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             2.0: [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             3.0: [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             4.0: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             5.0: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             6.0: [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             7.0: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             8.0: [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             9.0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}

def readfile(filename, choix):


    #choix/ 1240: statiques/40 ; 1250: statiques/50 ; 1260: statiques/60 ; 2640: tous/40; 2650: tous/50; 2660: tous/60;
    data = []


    for line in open(filename):
        csv_row = line.split(";")
        csv_data_row = []
        for column, item in enumerate(csv_row):
            csv_row[column] = float(item)
        csv_data_row.append(csv_row[0])
        if choix == 1240:
            csv_row = csv_row[:(1+40*26)]
            csv_row = csv_row[1:]
            while len(csv_row) != 0:
                for index in range(12):
                    csv_data_row.append(csv_row[index])
                csv_row = csv_row[26:]
        elif choix == 1250:
            csv_row = csv_row[:(1 + 50 * 26)]
            csv_row = csv_row[1:]
            while len(csv_row) != 0:
                for index in range(12):
                    csv_data_row.append(csv_row[index])
                csv_row = csv_row[26:]
        elif choix == 1260:
            csv_row = csv_row[1:]
            while len(csv_row) != 0:
                for index in range(12):
                    csv_data_row.append(csv_row[index])
                csv_row = csv_row[26:]
        elif choix == 2640:
            csv_data_row = csv_row[:(1 + 40 * 26)]
        elif choix == 2650:
            csv_data_row = csv_row[:(1 + 50 * 26)]
        elif choix == 2660:
            csv_data_row = csv_row
        else:
                print("Erreur: config mal choisie")
        csv_data_row[0] = nb2output[csv_data_row[0]]
        
        data.append(csv_data_row)

    return data
