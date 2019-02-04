from random import shuffle

inputs_train = [[0, 0], [0, 2], [0, 4], [0, 5], [0, 7],
                [1, 0], [1, 1], [1, 3], [1, 6], [1, 7], [1, 8], [1, 9],
                [2, 3], [2, 4], [2, 6],
                [3, 1], [3, 2], [3, 4], [3, 8],
                [4, 0], [4, 2], [4, 4], [4, 7], [4, 8], [4, 9],
                [5, 0], [5, 1], [5, 3], [5, 5], [5, 6], [5, 7], [5, 9],
                [6, 1], [6, 2], [6, 3], [6, 5], [6, 8],
                [7, 0], [7, 2], [7, 4], [7, 6], [7, 7], [7, 9],
                [8, 0], [8, 4], [8, 5],
                [9, 2], [9, 3], [9, 5], [9, 7], [9, 8], [9, 9]]

output_train = [[0, 1], [0, 1], [0, 1], [0, 1], [1, 0],
                [0, 1], [0, 1], [0, 1], [1, 0], [1, 0], [1, 0], [1, 0],
                [0, 1], [1, 0], [1, 0],
                [0, 1], [0, 1], [1, 0], [1, 0],
                [0, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                [0, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                [1, 0], [1, 0], [1, 0],
                [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]

inputs_vc = [[0, 1], [0, 6], [0, 9],
             [1, 2], [1, 5],
             [2, 0], [2, 2], [2, 5], [2, 8], [2, 9],
             [3, 0], [3, 5], [3, 6], [3, 9],
             [4, 1], [4, 3], [4, 6],
             [5, 4], [5, 8],
             [6, 0], [6, 6], [6, 9],
             [7, 1], [7, 5], [7, 8],
             [8, 2], [8, 3], [8, 7], [8, 8],
             [9, 0], [9, 1], [9, 6]]

output_vc = [[0, 1], [1, 0], [1, 0],
             [0, 1], [1, 0],
             [0, 1], [0, 1], [1, 0], [1, 0], [1, 0],
             [0, 1], [1, 0], [1, 0], [1, 0],
             [0, 1], [1, 0], [1, 0],
             [1, 0], [1, 0],
             [1, 0], [1, 0], [1, 0],
             [1, 0], [1, 0], [1, 0],
             [1, 0], [1, 0], [1, 0], [1, 0],
             [1, 0], [1, 0], [1, 0]]

output_vc = [[0, 1], [1, 0], [1, 0],
             [0, 1], [1, 0],
             [0, 1], [0, 1], [1, 0], [1, 0], [1, 0],
             [0, 1], [1, 0], [1, 0], [1, 0],
             [0, 1], [1, 0], [1, 0],
             [1, 0], [1, 0],
             [1, 0], [1, 0], [1, 0],
             [1, 0], [1, 0], [1, 0],
             [1, 0], [1, 0], [1, 0], [1, 0],
             [1, 0], [1, 0], [1, 0]]

input_test = [[0, 3], [0, 8],
              [1, 4],
              [2, 1], [2, 7],
              [3, 3], [3, 7],
              [4, 5],
              [5, 2],
              [6, 4], [6, 7],
              [7, 3],
              [8, 1], [8, 6], [8, 9],
              [9, 4]]
