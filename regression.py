from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures


# Q1,Q2,Q3,Q4,dff = wp.readData()


def train(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
    #    regr = linear_model.LinearRegression()
    #    # Train the model using the training sets
    #    regr.fit(X_train, y_train)
    #
    #    # Make predictions using the testing set
    #    y_pred = regr.predict(X_test)
    #    # Alpha (regularization strength) of LASSO regression
    #    polynomial_features= PolynomialFeatures(degree=2)
    #    x_poly = polynomial_features.fit_transform(X_train)
    #    x_poly_test = polynomial_features.fit_transform(X_test)
    #
    #    model = linear_model.LinearRegression()
    #    model.fit(x_poly, y_train)
    #    y_poly_pred = model.predict(x_poly_test)
    #
    #    rmse = np.sqrt(mean_squared_error(y_test,y_poly_pred))
    #    r2 = r2_score(y_test,y_poly_pred)
    #    print(rmse)
    #    print(r2)

    polynomial_features = PolynomialFeatures(degree = 1)
    x_poly_train = polynomial_features.fit_transform(X_train)
    x_poly_test = polynomial_features.fit_transform(X_test)
    # y_poly_train = polynomial_features.fit_transform(y_train)
    # y_poly_test = polynomial_features.fit_transform(y_test)

    model = linear_model.LinearRegression()
    model.fit(x_poly_train, y_train)
    y_poly_pred = model.predict(x_poly_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_poly_pred))
    #    r2 = r2_score(y_test,y_poly_pred)
    print(rmse)
    #    print('r2',r2)

    return X_test, y_test, y_poly_pred


def plots(X_test, y_test, y_pred, x):
    plt.figure(figsize = (8, 8))
    plt.scatter(X_test, y_test, color = 'red')
    plt.plot(X_test, y_pred, color = 'blue', linewidth = 3)
    plt.xticks(np.linspace(X_test.min(), X_test.max(), 15))
    plt.yticks(np.linspace(X_test.min(), X_test.max(), 15))
    plt.xlabel('Austria')
    plt.ylabel('Deutschland')
    plt.title(x)
    plt.show()


def main(df1, df2):
    X = df1.values.reshape(-1, 1)
    y = df2.values.reshape(-1, 1)

    return train(X, y)

# correlation matrix
# corr = df[df.columns[:-1]].corr()
# corr.style.background_gradient(cmap="coolwarm")
