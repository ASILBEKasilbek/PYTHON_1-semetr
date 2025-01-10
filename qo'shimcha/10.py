def draw_flag_ascii():
    # Bayroq elementlarini aniqlash
    blue = "#" * 20  # Ko'k
    red = "*" * 20  # Qizil
    white = "#" * 20  # Oq
    green = "#" * 20  # Yashil

    # Bayroqni yaratish
    flag = []
    flag.extend([blue] * 3)  # Ko'k qatlam
    flag.extend([red])       # Qizil chiziq
    flag.extend([white] * 3) # Oq qatlam
    flag.extend([red])       # Qizil chiziq
    flag.extend([green] * 3) # Yashil qatlam

    # Konsolga bayroqni chiqarish
    for line in flag:
        print(line)

# Chizish
draw_flag_ascii()