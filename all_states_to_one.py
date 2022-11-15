import csv

with open("ukraine.csv", 'r', newline='', encoding="utf-8") as fr:
    with open("ukraine_summary_data.csv", 'w', newline='', encoding="utf-8") as fw:
        reader = csv.reader(fr)
        writer = csv.writer(fw)
        prew_date = ""
        sum_comfirmed = 0
        sum_deaths = 0
        sum_recovered = 0
        for row in reader:
            new_row = []
            if row[2] == prew_date:
                sum_comfirmed = sum_comfirmed + int(float(row[6]))
                sum_deaths = sum_deaths + int(float(row[7]))
                sum_recovered = sum_recovered + int(float(row[8]))
            else:
                new_row.append(row[1])
                new_row.append(prew_date)
                new_row.append(str(sum_comfirmed))
                new_row.append(str(sum_deaths))
                new_row.append(str(sum_recovered))
                writer.writerow(new_row)
                prew_date = row[2]
                sum_comfirmed = int(float(row[6]))
                sum_deaths = int(float(row[7]))
                sum_recovered = int(float(row[8]))
            