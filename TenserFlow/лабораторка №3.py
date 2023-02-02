import math

arr_y = []
h_8 = 0.1
h_4 = 0.2

for i in range(1, 10):
    x = i / 10
    arr_y.append((1 - math.cos(x)) / x)

I_pr_8 = h_8 * sum(arr_y)
I_pr_4 = h_4 * sum(arr_y[::2])

I_8_tr = h_8 * (sum(arr_y[1:-1:1]) + (arr_y[0] + arr_y[-1]) / 2)
I_4_tr = h_4 * (sum(arr_y[2:-1:2]) + (arr_y[0] + arr_y[-1]) / 2)
R_tr = (abs(I_4_tr - I_8_tr) / 2)

I_8_s = (h_8 / 3) * (arr_y[0] + arr_y[-1] + (4 * sum(arr_y[1:-1:2])) + (2 * sum(arr_y[2:-1:2])))
I_4_s = (h_4 / 3) * (arr_y[0] + arr_y[-1] + 4 * (arr_y[2] + arr_y[6]) + 2 * arr_y[4])
R_s = (abs(I_8_s - I_4_s) / 15)

print(f"Прямоугольник - n = 8 -> {I_pr_8}    n = 4 -> {I_pr_4}")
print(f"Трапеция - n = 8 -> {I_8_tr}    n = 4 -> {I_4_tr}    погрешность ->{R_tr}")
print(f"Симпсон - n = 8 -> {I_8_s}    n = 4 -> {I_4_s}    погрешность ->{R_s}")
