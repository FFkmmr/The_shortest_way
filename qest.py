map = [[ ' ' , 'V' , ' ' , ' ' ],
[ ' ' , '*' , '*' , ' ' ],
[ ' ' , ' ' , ' ' , ' ' ],
[ ' ' , '*' , ' ' , 'O' ]]
def best_way(map):
    idx_col = -1
    idx_rows = -1
    el = -1
    iter = 0
    mod_map = [[ ' ' , ' ' , ' ' , ' ' ],
[ ' ' , ' ' , ' ' , ' ' ],
[ ' ' , ' ' , ' ' , ' ' ],
[ ' ' , ' ' , ' ' , ' ' ]]

    for col in map:
        idx_col+=1
        for rows in col:
            el+=1
            idx_rows+=1
            if rows == ' ' or rows == '*':
                continue
            if rows == 'V':
                if (idx_col!=0) and (col[idx_col-1][el] == ' '):
                    mod_map[idx_col-1][el] = iter + 1
                    iter + 1
                if (idx_col + 1 <= 4) and (col[idx_col+1][el] == ' '):
                    mod_map[idx_col+1][el] = iter + 1
                    iter + 1
                if (idx_col!=0) and (col[idx_col-1][el] == ' '):
                    mod_map[idx_col-1][el] = iter + 1
                    iter + 1
                continue






best_way(map)