import maindf as mdf
df = mdf.create_df()

def find_shot_stats(self):
	df['HomeAccuracy'] = round((df['HST'] / df['HS'] * 100), 1)
	df['AwayAccuracy'] = round((df['AST'] / df['AS'] * 100), 1)

	df['HomeConv'] = round((df['FTHG'] / df['HS'] * 100), 1)
	df['AwayConv'] = round((df['FTAG'] / df['AS'] * 100), 1)

def did_HTWinner_win(self):
	df['ftr'] = df['FTHG'] - df['FTAG']
	df['htr'] = df['HTHG'] - df['HTAG']
	df.loc[(df['htr'] > 0) & (df['ftr'] > 0), 'didHTWinnerWin'] = 'True' 
	df.loc[(df['htr'] < 0) & (df['ftr'] < 0), 'didHTWinnerWin'] = 'True'
	df.loc[(df['htr'] < 0) & (df['ftr'] > 0), 'didHTWinnerWin'] = 'False'
	df.loc[(df['htr'] > 0) & (df['ftr'] < 0), 'didHTWinnerWin'] = 'False'
	df.loc[(df['htr'] == 0) & (df['ftr'] == 0), 'didHTWinnerWin'] = 'False'

df.apply(find_shot_stats)
df.apply(did_HTWinner_win)

# x = '20180810'
# y = '20180817'
# df = df.loc[x:y, :]
#df.loc[df['didHTWinnerWin'] == 'True']
#df[df['HTHG'] == df['HTHG'].max()]
print(df)