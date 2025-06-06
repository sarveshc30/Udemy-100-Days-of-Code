import random
names = ['alex', 'bortoletto', 'carlos', 'daniel']
dictionary = {key: random.randint(1, 100) for key in names}
print(dictionary)

passed = {key:value for (key, value) in dictionary.items() if value > 40}
print(passed)

import pandas as pd
new_dict = {
    'Student': names,
    'score': [value for (key, value) in dictionary.items()]
}
df = pd.DataFrame(new_dict)

for (index, row) in df.iterrows():
    #print(index)
    print(row.Student)