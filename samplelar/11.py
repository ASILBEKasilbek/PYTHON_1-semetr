n = int(input("Garage o'lchamini kiriting: "))
a = [[0] * n for _ in range(n)]
while True:
    r = input("Mashina nomini kiriting (yoki 'stop' to'xtatish uchun): ")
    if r.lower() == 'stop':
        break
    col = int(input("Ustunni kiriting: "))
    row = int(input("Qatorni kiriting: "))
    col -= 1
    row -= 1
    if a[row][col] == 0:
        a[row][col] = r
    else:
        min_distance = float('inf')
        best_spot = None
        for i in range(n):
            for j in range(n):
                if a[i][j] == 0:
                    distance = abs(i - row) + abs(j - col)
                    if distance < min_distance:
                        min_distance = distance
                        best_spot = (i, j)
        if best_spot:
            print("Siz hozirda bu yerga mashina qo'ya olmaysiz. Mana bu koordinatalarga mashina qo'ysayiz bo'ladi:")
            print(best_spot[0] + 1, best_spot[1] + 1)
        else:
            print("Garage to'la, boshqa joy yo'q.")
        print(f"Bu yerda {a[row][col]} bor")
        continue
    for row in a:
        print(*row)
