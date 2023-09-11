import os

# 出力ディレクトリを作成
output_dir = '/content/drive/MyDrive/siri_choice/Pre_Finished'
os.makedirs(output_dir, exist_ok=True)

# Google ColabでGoogle Driveをマウント
from google.colab import drive
drive.mount('/content/drive')

# テキストファイルへのパスを指定
file_path = '/content/drive/MyDrive/siri_choice/test.txt'

# テキストファイルからデータを読み込む
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

audio_to_text = {}  # オーディオファイル名をキーとし、最後のRecognized Textを値とする辞書

current_audio = None
for line in lines:
    line = line.strip()
    if line.startswith("Now Playing:"):
        current_audio = line.split(": ")[1]
    elif line.startswith("Recognized Text:") and current_audio:
        parts = line.split(": ")
        if len(parts) > 1:
            audio_to_text[current_audio] = parts[1]

# 出力ファイルの番号を取得
output_files = os.listdir(output_dir)
existing_numbers = set()
for file_name in output_files:
    if file_name.startswith("output_") and file_name.endswith(".txt"):
        try:
            number = int(file_name.split("_")[1].split(".")[0])
            existing_numbers.add(number)
        except ValueError:
            pass

# 新しい番号を決定
number = 1
while number in existing_numbers:
    number += 1

# 結果をテキストファイルとして出力（ファイル名に番号を含める）
output_file_name = f"output_{number}.txt"
output_file_path = os.path.join(output_dir, output_file_name)
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for audio, text in audio_to_text.items():
        output_file.write(f"{audio}:{text}\n")

print(f"結果が {output_file_path} に保存されました。")