import pandas as pd
import sys

filename = sys.argv[1]
print(filename)

data = pd.io.stata.read_stata(filename)
data.to_csv(f'{filename}.csv')
