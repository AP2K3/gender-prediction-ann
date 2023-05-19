import numpy as np

'''
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