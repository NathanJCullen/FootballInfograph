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

def write_to_file(lineToWrite, filename):
	#Temporary function to output shit to txt file
	f_write = open(filename, 'w+')
	f_write.write(lineToWrite)
	f_write.close()

def make_stat_highest(df, statname):
	dfTemp = df.sort_values(statname, ascending=False)
	dfTemp = dfTemp.iloc[0]
	name=str(dfTemp.name).split(" ")
	output = ("The highest scoring game was %s vs %s with %s from a %s - %s on %s" % (dfTemp['HomeTeam'], dfTemp['AwayTeam'], dfTemp[statname], dfTemp['FTHG'], dfTemp['FTAG'], name[0]))
	write_to_file(output, statname + ".txt")

def make_stat_total(df, statname):
	x = df[statname].sum()
	write_to_file(str(x), statname +".txt")

def get_team_stats(df, teamname, homestat, awaystat):
	tempdf = (df[(df.HomeTeam == teamname) | (df.AwayTeam == teamname)])
	tempdf.loc[(tempdf['HomeTeam'] == teamname) , teamname+homestat] = tempdf[homestat]
	tempdf.loc[(tempdf['AwayTeam'] == teamname) , teamname+homestat] = tempdf[awaystat]
	teamtotalstat = tempdf[teamname+homestat].sum()
	print(teamtotalstat)



x = '20180810'
y = '20180817'
#df = search_between_date(df,x,y)

df.apply(find_shot_stats)
df.apply(did_HTWinner_win)

get_team_stats(df, "Arsenal", "FTHG", "FTAG")

#make_stat_highest(df, 'goals_scored')
#make_stat_total(df, 'total_yellow')
#make_stat_total(df, 'total_red')
#make_stat_total(df, 'total_shots')
#make_stat_total(df, 'total_shots_target')
#print(df)