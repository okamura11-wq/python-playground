# ch01_mean_var.py
# 勉強時間リストから合計・平均・分散を出す超ミニ実装

from math import sqrt

def calc_mean(xs):
    return sum(xs) / len(xs)

def calc_var(xs):
    mean = calc_mean(xs)
    return sum((x - mean) ** 2 for x in xs) / len(xs)

def main():
    # 例: 1週間の勉強時間（時間）
    hours = [2.5, 3.0, 1.5, 4.0, 3.5, 2.0, 3.0]

    total = sum(hours)
    mean = calc_mean(hours)
    var = calc_var(hours)
    std = sqrt(var)

    print("=== Study stats ===")
    print(f"days   : {len(hours)}")
    print(f"total  : {total:.2f} h")
    print(f"mean   : {mean:.2f} h")
    print(f"stddev : {std:.2f} h")

if __name__ == "__main__":
    main()
