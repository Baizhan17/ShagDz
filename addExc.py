import pandas as pd

file_path = 'file1.xlsx'

try:
    df = pd.read_excel(file_path)
    total_sum = 0
    for column in df.columns:
        for value in df[column]:
            if pd.notna(value) and isinstance(value, (int, float)):
                total_sum += value
    print("Сумма всех числовых данных в файле:", total_sum)
except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
