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

def compare_highest_stats(df, homestat, awaystat):
	dfTempHome = df.sort_values(homestat, ascending=False)
	dfTempAway = df.sort_values(awaystat, ascending=False)
	#Dictionaries overwrite stuff. This doesn't work nicely when the same team has highest stats
	top_stats = {}
	for place in range(0,3):
		if (dfTempHome[homestat][0] >= dfTempAway[awaystat][0]):
			top_stats[dfTempHome['HomeTeam'][0]] = dfTempHome[homestat][0]
			dfTempHome.drop(dfTempHome.index[0], inplace=True)
		else:
			top_stats[dfTempAway['AwayTeam'][0]] = dfTempAway[awaystat][0]
			dfTempAway.drop(dfTempAway.index[0], inplace=True)
	print(top_stats)

def compare_lowest_stats(df, homestat, awaystat):
	dfTempHome = df.sort_values(homestat, ascending=True)
	dfTempAway = df.sort_values(awaystat, ascending=True)
	#Dictionaries overwrite stuff. This doesn't work nicely when the same team has highest stats
	low_stats = {}
	for place in range(0,3):
		if (dfTempHome[homestat][0] >= dfTempAway[awaystat][0]):
			low_stats[dfTempHome['HomeTeam'][0]] = dfTempHome[homestat][0]
			dfTempHome.drop(dfTempHome.index[0], inplace=True)
		else:
			low_stats[dfTempAway['AwayTeam'][0]] = dfTempAway[awaystat][0]
			dfTempAway.drop(dfTempAway.index[0], inplace=True)
	print(low_stats)

def find_margin(df):
	dfTemp = df.sort_values('ftr', ascending=False)
	dfTemp = dfTemp.iloc[0]
	x = int(dfTemp['ftr'])
	dfTemp2 = df.sort_values('ftr', ascending=True)
	dfTemp2 = dfTemp2.iloc[0]
	y = int(dfTemp2['ftr']) *-1
	if(x >= y):
		output = ("Biggest Margin: %s - %s by %s and %s" % (dfTemp['FTHG'], dfTemp['FTAG'], dfTemp['HomeTeam'], dfTemp['AwayTeam']))
	else:
		output = ("Biggest Margin: %s - %s by %s and %s" % (dfTemp2['FTHG'], dfTemp2['FTAG'], dfTemp2['HomeTeam'], dfTemp2['AwayTeam']))
	print(output)

x = '20180810'
y = '20180817'
#df = search_between_date(df,x,y)

df.apply(find_shot_stats)
df.apply(did_HTWinner_win)

find_margin(df)
#compare_highest_stats(df, 'FTHG', 'FTAG')
#compare_lowest_stats(df, 'HS', 'AS')
#make_stat_highest(df, 'goals_scored')
#make_stat_total(df, 'total_yellow')
#make_stat_total(df, 'total_red')
#make_stat_total(df, 'total_shots')
#make_stat_total(df, 'total_shots_target')
#print(df)