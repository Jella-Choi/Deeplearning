## linear regression practice
# 최소 제곱법(method of least squares)
import numpy as np

x = [2,4,6,8]
y = [81,93,91,97]

mx = np.mean(x)
my = np.mean(y)
print("x의 평균: ", mx)
print("y의 평균: ", my)

## 최소 제곱법의 분모 : (x각 원소 -x평균값)의 제곱 gkq
divisor = sum([(mx - i)**2 for i in x])

## 최소 제곱법의 분자
def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i] - my)
    return d

dividend = top(x, mx, y, my)

print("분모: ", divisor)
print("분자: ", dividend)

## 기울기와 y절편 구하기 [ y=ax+b ]
a = dividend / divisor
b = my - (mx*a)
print("기울기 a = ", a)
print("y절편 b = ", b)
