import os

DATA_DIR = os.path.join(os.getcwd().replace('/src', ''), 'data')

# Scraping
SECONDS_SLEEP = 1

# Plotly Credentials
PLOTLY_USERNAME = 'your_username'
PLOTLY_API_KEY = 'your_api_key'

SEASON_DATES = {
    '2014-15': ['20141028', '20150415'],
    '2015-16': ['20151027', '20160413'],
    '2016-17': ['20161025', '20170412'],
    '2017-18': ['20171017', '20180411'],
    '2018-19': ['20181016', '20190410'],
    '2019-20': ['20191022', '20200410']
}

# Data for DraftKings is not available prior to 2014-15
# https://en.wikipedia.org/wiki/2018-2019_NBA_season
# TODO: automatically extract season start and end dates from wikipedia


DF_VARIABLES = ['Name', 'Date', 'Team',  'FPTS', 'Home', 'W', 'W_PTS', 'L', 'L_PTS', 'MP',
                'FG', 'FGA', 'FG_perc', '3P', '3PA', '3P_perc', 'FT', 'FTA', 'FT_perc',
                'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'DD', 'TD',
                'USG_perc', 'DRtg', 'ORtg', 'AST_perc', 'DRB_perc', 'ORB_perc', 'BLK_perc',
                'TOV_perc', 'STL_perc', 'eFG_perc']

DF_FEATURES = ['Date', 'Name', 'Team', 'Pos', 'FPTS', 'Salary',
               # Additional Features
               'Starter', 'Rest', 'Rota_All', 'Rota_Pos', 'Home',
               'PG', 'SG', 'F', 'C', 'Value', 'FPTS_std',
               # Basic Stats with weighted mean
               'PTS', '3P',  'AST', 'TRB',
               'STL', 'BLK', 'TOV', 'DD', 'TD',
               # Additional Stats with weighted mean
               'MP', 'FT', 'FTA', 'FGA', '3PA', 'DRB', 'ORB',
               # Advanced Stats with weighted mean
               'USG_perc', 'DRtg', 'ORtg', 'AST_perc', 'DRB_perc', 'ORB_perc',
               'BLK_perc', 'TOV_perc', 'STL_perc', 'eFG_perc', 'FG_perc', '3P_perc', 'FT_perc']
