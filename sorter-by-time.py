import csv
from datetime import datetime
import sys

# Открыть файл CSV и прочитать данные
with open(sys.argv[1], 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # сохранить заголовок

    # Создать список кортежей, содержащих преобразованные дату и время
    data = []
    for row in reader:
        date_str, time_str = row[0], row[1]
        date_time = datetime.strptime(date_str + ' ' + time_str, '%d/%m/%Y %H:%M:%S')
        data.append((date_time, row))

# Отсортировать список кортежей по дате и времени
    sorted_data = sorted(data, key=lambda x: x[0])

# ИЛИ перезаписать исходный файл CSV
    with open(sys.argv[1], 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # записать заголовок
        for date_time, row in sorted_data:
            writer.writerow(row)

