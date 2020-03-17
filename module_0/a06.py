>>> import numpy as np
>>> def game_core_v1(n):
    a = 1
    b = 100   
    count = 0
    rand = np.random.randint(a, b) 
    while rand != n:
    	if rand > n:
       	 b = rand
    	elif rand < n:
         a = rand
    rand = np.random.randint(a, b)
    return(rand)
    
>>> def score_game(game_core_v1):
    count_ls = []
    np.random.seed(1) 
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

>>> score_game(game_core_v1)
