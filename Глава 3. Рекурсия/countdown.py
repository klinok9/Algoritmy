def countdown(i):
    print(i)
    if i <= 0:  # базовый случай
        return
    else:  # рекурсивный случай
        countdown(i - 1)


countdown(10)
