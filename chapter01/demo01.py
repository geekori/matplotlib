import matplotlib.pyplot as plt

'''
a = [1,2,3,4]
b = [6,7,8,9]

plt.plot(a,b)
plt.show()
'''
# y = x^2

X = range(-100,101)
Y = [x ** 2 for x in X]
plt.plot(X,Y)
plt.savefig('result1.jpg')
plt.show()
