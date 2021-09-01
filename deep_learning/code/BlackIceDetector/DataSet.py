total_x = [
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5], 
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5], 
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5], 
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5], 
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5], 
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5], 
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5], 
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5], 
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5], 
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5], 
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5], 
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5], 
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 3, 1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5]
    ]
    # 50개 data

total_y = [
    [1],
    [0],
    [0],
    [0],
    [1],
    [1],
    [1],
    [0],
    [0],
    [0],
    [1],
    [1],
    [1],
    [0],
    [0],
    [0],
    [1],
    [1],
    [1],
    [0],
    [0],
    [0],
    [1],
    [0],
    [0],
    [0],
    [1],
    [1],
    [0],
    [0],
    [0],
    [1],
    [1],
    [0],
    [0],
    [0],
    [1],
    [0],
    [0],
    [0],
    [1],
    [0],
    [0],
    [0],
    [1],
    [0],
    [0],
    [0],
    [1],
    [1]
    ]
# 50개