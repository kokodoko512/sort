import tkinter as tk
import random


class RandomNumberGenerator:
    def __init__(self):
        self.reset()

    def generate(self):
        if self.index >= len(self.numbers):
            return "終了"

        number = self.numbers[self.index]
        self.index += 1
        return number

    def reset(self):
        self.numbers = list(range(1, 101))
        random.shuffle(self.numbers)
        self.index = 0


# 乱数生成器
rng = RandomNumberGenerator()


# ボタン処理
def generate_number():
    result = rng.generate()
    label.config(text=str(result))


def reset_numbers():
    rng.reset()
    label.config(text="リセットしました")


# ウィンドウ作成
root = tk.Tk()
root.title("重複なし乱数生成")
root.geometry("400x250")

# 結果表示ラベル
label = tk.Label(root, text="ボタンを押してください", font=("Arial", 24))
label.pack(pady=30)

# 生成ボタン
generate_button = tk.Button(
    root,
    text="数字を生成",
    font=("Arial", 16),
    command=generate_number
)
generate_button.pack(pady=10)

# リセットボタン
reset_button = tk.Button(
    root,
    text="リセット",
    font=("Arial", 16),
    command=reset_numbers
)
reset_button.pack(pady=10)

# 起動
root.mainloop()
