import time

nb2output = {"0.0": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             "1.0": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             "2.0": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             "3.0": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             "4.0": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             "5.0": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             "6.0": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             "7.0": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             "8.0": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             "9.0": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}

def readfile(filename):
    data = []
    #row = 0
    for line in open(filename):
        csv_row = line.split(";")
    #3dim arrays geht, lines reorganisieren, dann casten zurzeit 27*60, du musst den eingang immer wiederholen oder dir ne geile liste einfallen lassen

        for column, item in enumerate(csv_row):
            csv_row[column] = float(item)
        #print(row)
        data.append(csv_row)
        #data+=csv_row
        #print(data_row[row])
    return data
    #print(data_row[0][1])

start = time.time()
data = readfile('data_test.csv')

end = time.time()
print(end-start)
print(data[0])

# import csv, sys
# filename = 'test.csv'
# def readtableau(filename):
#     with open(filename) as f:
#         reader = csv.excel(f)
#     try:
#         for row in reader:
#             print(row)
#     except csv.Error as e:
#         sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))