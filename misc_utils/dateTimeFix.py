import pandas as pd

df = pd.read_csv('trip_path_mbike_start_20190114.csv')

print(df['Date_Time'].head(5))

def splitDateTime(row):
    s = row['Date_Time'].split("T")
    t = s[1].split(".")[0]
    date = s[0]
    print(date)
    return pd.Series([date, t])

df['Date'], df['Time'] = None, None
df[['Date','Time']] = df.apply(splitDateTime, axis=1)

df.to_csv('mbike.csv', index=False)

print(df.Date.head(5))
print(df.Time.head(5))
