map = [[ ' ' , 'V' , ' ' , ' ' ],
[ ' ' , '*' , '*' , ' ' ],
[ ' ' , ' ' , ' ' , ' ' ],
[ ' ' , '*' , ' ' , 'O' ]]
def best_way(map):
    idx_col = -1
    idx_rows = -1
    el = -1
    iter = 0
    mod_map = [[ ' ' , 'V' , ' ' , ' ' ],
               [ ' ' , '*' , '*' , ' ' ],
               [ ' ' , ' ' , ' ' , ' ' ],
               [ ' ' , ' ' , ' ' , 'O' ]]
    for i in range(16):
        for col in map:
            idx_col+=1
            for rows in col:
                idx_rows+=1
                if rows == ' ' or rows == '*':
                    continue
                if rows == 'V':
                    if (idx_col!=0) and (map[idx_col-1][idx_rows] == ' '):
                        mod_map[idx_col-1][idx_rows] = str(iter + 1)

                    if (idx_col + 1 < 4) and (map[idx_col+1][idx_rows] == ' '):
                        mod_map[idx_col+1][idx_rows] = str(iter + 1)

                    if (idx_rows-1>=0) and (map[idx_col][idx_rows-1] == ' '):
                        mod_map[idx_col][idx_rows-1] = str(iter + 1)

                    if (idx_rows+1<=4) and (map[idx_col][idx_rows+1] == ' '):
                        mod_map[idx_col][idx_rows+1] = str(iter + 1)

                if (rows == iter) or (rows == iter-1) or (rows == iter+1) or (rows == iter+2) or (rows == iter-2):
                    if (idx_col!=0) and (map[idx_col-1][idx_rows] == ' '):
                        mod_map[idx_col-1][idx_rows] = str(iter + 1)

                    if (idx_col + 1 < 4) and (map[idx_col+1][idx_rows] == ' '):
                        mod_map[idx_col+1][idx_rows] = str(iter + 1)

                    if (idx_rows-1>=0) and (map[idx_col][idx_rows-1] == ' '):
                        mod_map[idx_col][idx_rows-1] = str(iter + 1)

                    if (idx_rows+1<=4) and (map[idx_col][idx_rows+1] == ' '):
                        mod_map[idx_col][idx_rows+1] = str(iter + 1)
                # print(mod_map)
                for i in range(4):
                    print(mod_map[i],'\n')
                iter += 1
            idx_rows=0
        print(f'-------------------{iter} \n')
        idx_col=0
        idx_rows=0






best_way(map)
