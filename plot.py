import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open("ukraine_new_data.csv", 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    date = []
    sick = []
    for row in reader:
        dt = datetime.strptime(row[0], "%m/%d/%Y")
        date.append(dt)
        sick.append(int(row[4]))
    plt.plot(date, sick, color='green')
    plt.show()