import pandas as pd
import sys
df = pd.read_csv(sys.argv[1])
df_sorted = df.sort_values(by=list(df.columns))
df_sorted.to_csv(sys.argv[2], index=False)

