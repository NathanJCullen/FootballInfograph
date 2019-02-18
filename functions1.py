import maindf as mdf
import datetime
df = mdf.create_df()

def find_shot_stats(self):
	df['HomeAccuracy'] = round((df['HST'] / df['HS'] * 100), 1)
	df['AwayAccuracy'] = round((df['AST'] / df['AS'] * 100), 1)

	df['HomeConv'] = round((df['FTHG'] / df['HS'] * 100), 1)
	df['AwayConv'] = round((df['FTAG'] / df['AS'] * 100), 1)

def did_HTWinner_win(self):
	df['ftr'] = df['FTHG'] - df['FTAG'] #Positive if HomeTeam Won, 0 if draw, negative if losing
	df['htr'] = df['HTHG'] - df['HTAG'] #Positive if HomeTeam winning at HT, 0 if draw, negaitve if losing
	df['didHTWinnerWin'] = 'False' #Default to False and changes it with the next line
	df.loc[((df['ftr'] > 0) & (df['htr'] > 0)) | ((df['ftr'] < 0) & (df['htr'] < 0)), 'didHTWinnerWin'] = 'True' #If the home team were winning at HT and then won, or were losing at HT then lots: true
	df.drop(['ftr','htr'], axis=1, inplace=True)

def search_between_date(df,x,y):
	df = df.ix[x:y, :]
	return df

def write_to_file(lineToWrite):
	#Temporary function to output shit to txt file
	f_write = open('highestscorer.txt', 'w+')
	f_write.write(lineToWrite)
	f_write.close()

def most_goals(df):
	df['goals_scored'] = df['FTHG'] + df['FTAG']
	dfTemp = df.sort_values('goals_scored', ascending=False)
	dfTemp = dfTemp.iloc[0]
	dfTemp.reset_index()
	name = str(dfTemp.name).split(" ")
	output = ("The highest scoring game was %s vs %s with a %s - %s on %s" % (dfTemp['HomeTeam'], dfTemp['AwayTeam'], dfTemp['FTHG'], dfTemp['FTAG'], name[0]))
	write_to_file(output)


x = '20180810'
y = '20180817'
#df = search_between_date(df,x,y)

df.apply(find_shot_stats)
df.apply(did_HTWinner_win)

most_goals(df)
#print(df)