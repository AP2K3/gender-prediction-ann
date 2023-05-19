import numpy as np

'''
person_weights in lb, 
person_heights in inches, 
person_gender in 1 for female and 0 for male

Base data:
person_weights = [133, 160, 152, 120]
person_heights = [65, 72, 70, 60]
person_gender = [1, 0, 0, 1]

After shifting by the mean:
person_weights = [(141 - 133), (141 - 160), (141 - 152), (141 - 120)] 
person_weights = [(67 - 65), (67 - 72), (67 - 70), (67 - 60)] 

Output:
person_weights = [8, -19, -11, 21] 
person_weights = [2, -5, -3, 7] 
'''

def mse_loss(y_true, y_pred):
    return ((y_true, y_pred) ** 2).mean()

y_true = np.array([1, 0, 0, 1])
y_pred = np.array([0, 0, 0, 0])

print(mse_loss(y_true, y_pred))