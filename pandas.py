import numpy as np
import results as results

import pandas as pd
result = []
for number_of_people in np.arange(1,26):
    probability = 1
    for count in range(1, number_of_people+1):
        probability *= (365-count+1)/365
        result.append({
            'n': number_of_people,
            'p(n)': (1-probability)
        })
        print(pd.DataFrame(results))
