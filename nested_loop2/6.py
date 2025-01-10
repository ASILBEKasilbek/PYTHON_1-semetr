import time

def print_pattern(pattern):
    for line in pattern:
        print(line)
    print("\n" * 2)

def create_initial_pattern(n):
    pattern = []
    for i in range(n):
        if i < n // 2:
            pattern.append(" " * i + "*" * (n - 2 * i) + " " * i)
        elif i == n // 2:
            pattern.append(" " * i + "*")
        else:
            pattern.append(" " * (n - i - 1) + "*" + " " * (2 * i - n) + "*" + " " * (n - i - 1))
    return pattern

def fall_sand(pattern, n):
    mid = n // 2

    for step in range(n // 2):
        for i in range(mid):
            if '*' in pattern[i]:
                star_pos = pattern[i].index('*')
                pattern[i] = pattern[i][:star_pos] + ' ' + pattern[i][star_pos + 1:]
                
                for k in range(mid + 1, n):
                    if pattern[k][star_pos] == ' ':
                        pattern[k] = pattern[k][:star_pos] + '*' + pattern[k][star_pos + 1:]
                        break
                        
                print_pattern(pattern)
                time.sleep(1)
                break

def main():
    n = int(input("Qum soati o'lchamini kiriting (n): "))
    if n % 2 == 0:
        print("Iltimos, toq son kiriting.")
        return

    pattern = create_initial_pattern(n)
    print_pattern(pattern)
    fall_sand(pattern, n)

if __name__ == "__main__":
    main()
