import csv
import math

N = 43810000
R0 = 2.25
Tinf = 4.5
S = []
I = []
R = []
F = []
T = 0

beta = R0/Tinf
gamma = 1.0/Tinf

def det2(arr: list):
    return ((arr[0][0]*arr[1][1])-(arr[1][0]*arr[0][1]))

def det(arr: list, n: int):
    result = 0.0
    if(n > 2):
        for i in range(n):
            new_matrix = []
            for j in range(1,n):
                row = []
                for k in range(n):
                    if(k == i):
                        continue
                    else:
                        row.append(arr[j][k])
                new_matrix.append(row)
            result = result + (math.pow(-1, i) * arr[0][i] * det(new_matrix, n-1))
    else:
        result = det2(arr)
    return result

def kramer(arr: list, n: int):
    matrixs = []
    dets = []
    koefs = []
    for i in range(n+1):
        m = []
        if(i == n):
            for j in range(n):
                row = []
                for k in range(n):
                    row.append(arr[j][k])
                m.append(row)
        else:
            for j in range(n):
                row = []
                for k in range(n):
                    if(k == i):
                        row.append(arr[j][n])
                    else:
                        row.append(arr[j][k])
                m.append(row)
        matrixs.append(m)
    for i in range(n+1):
        dets.append(det(matrixs[i], n))
    for i in range(n):
        koefs.append((dets[i]/dets[n]))
    return koefs


if __name__ == "__main__":
    with open("ukraine_summary_data.csv", 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            S.append(N-int(row[2]))
            I.append(int(row[2]) - int(row[3]) - int(row[4]))
            R.append(int(row[4]))
            F.append(int(row[3]))
            T = T + 1
    a1 = []
    a2 = []
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    for i in range(1, T):
        temp1 = (beta*S[i]*I[i])/N
        temp2 = I[i]
        temp3 = F[i] - F[i-1]
        sum1 = sum1 + temp1
        sum2 = sum2 + temp2
        sum3 = sum3 + temp1*I[i]
        sum4 = sum4 + temp2*I[i]
        sum5 = sum5 + temp3
        sum6 = sum6 + temp3*I[i]
    arr = [[sum1, sum2, sum5], [sum3, sum4, sum6]]
    print(kramer(arr, 2))