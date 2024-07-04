import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# 示例数据：房屋面积（平方英尺）和房价
data = {'Area': [1500, 2000, 2500, 3000, 3500],
        'Price': [300000, 400000, 500000, 600000, 700000]}
df = pd.DataFrame(data)

# 特征和目标变量
X = df[['Area']]  # 特征：房屋面积
y = df['Price']   # 目标变量：房价

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 进行预测
y_pred = model.predict(X_test)

# 评估模型
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# 打印预测结果
for area, price in zip(X_test['Area'], y_pred):
    print(f"Predicted price for {area} sq ft: ${price:.2f}")

# 可视化结果
plt.scatter(X_train, y_train, color='blue', label='Training data')
plt.scatter(X_test, y_test, color='green', label='Testing data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Prediction')

plt.xlabel('Area (sq ft)')
plt.ylabel('Price')
plt.legend()
plt.show()
