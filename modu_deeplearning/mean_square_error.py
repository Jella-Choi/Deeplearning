## linear regression practice
# 평균 제곱 오차(MSE, mean squared error)
import numpy as np

# 기울기 a, y 절편 b (임의로 값을 정해줌)
fake_a_b = [3,76]

# x,y 데이터 값
data = [[2,81],[4,93],[6,91],[8,97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

# y = ax+b에 a,b 대입하여 결과 출력
def predict(x):
    return fake_a_b[0]*x + fake_a_b[1]

# MSE 함수
def mse(y_hat, y):
    return ((y_hat - y)**2).mean()

# MSE 함수를 각 y값에 대입
def mse_val(predict_result, y):
    return mse(np.array(predict_result), np.array(y))

predict_result = []

# 모든 x값 대임
for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부한 시간 = %.f, 실제 점수 = %.f, 예측 점수 = %.f," %(x[i], y[i], predict(x[i])))

# 최종 MSE
print("mse 최종값: " + str(mse_val(predict_result,y)))


## 결과 해석: 처음 가정한 (a=3, b=76)은 오차가 약 11