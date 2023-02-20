import os

DATA_DIR = os.path.join(os.getcwd().replace("/notebooks", ""), "data")

# Scraping
SECONDS_SLEEP = 3

# Plotly Credentials
PLOTLY_USERNAME = "your_username"
PLOTLY_API_KEY = "your_api_key"

# Scraping Basketball Reference
URL_BBREF = "https://www.basketball-reference.com"
BOXSCORE_FORMAT = "/boxscores/?month={month}&day={day}&year={year}"

# Scrating RotoGuru
URL_ROTO_FORMAT = "http://rotoguru1.com/cgi-bin/hyday.pl?mon={month}&day={day}&year={year}&game=dk"


SEASON_DATES = {
    "2014-15": ["20141028", "20150415"],
    "2015-16": ["20151027", "20160413"],
    "2016-17": ["20161025", "20170412"],
    "2017-18": ["20171017", "20180411"],
    "2018-19": ["20181016", "20190410"],
    "2019-20": ["20191022", "20200410"],
    "2020-21": ["20201222", "20210516"],
    "2021-22": ["20211019", "20220410"],
    "2022-23": ["20221018", "20230409"],
}

# Data for DraftKings is not available prior to 2014-15
# https://en.wikipedia.org/wiki/2018-2019_NBA_season
# TODO: automatically extract season start and end dates from wikipedia
DF_VARIABLES = [
    "Name",
    "Date",
    "Team",
    "FPTS",
    "Home",
    "W",
    "W_PTS",
    "L",
    "L_PTS",
    "MP",
    "FG",
    "FGA",
    "FG_perc",
    "3P",
    "3PA",
    "3P_perc",
    "FT",
    "FTA",
    "FT_perc",
    "ORB",
    "DRB",
    "TRB",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "PF",
    "PTS",
    "DD",
    "TD",
    "USG_perc",
    "DRtg",
    "ORtg",
    "AST_perc",
    "DRB_perc",
    "ORB_perc",
    "BLK_perc",
    "TOV_perc",
    "STL_perc",
    "eFG_perc",
]

COLUMN_HEADERS = [
    "Name",
    "Date",
    "Team",
    "Home",
    "W",
    "W_PTS",
    "L",
    "L_PTS",
    "MP",
    "FG",
    "FGA",
    "FG_perc",
    "3P",
    "3PA",
    "3P_perc",
    "FT",
    "FT_perc",
    "ORB",
    "DRB",
    "TRB",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "PF",
    "PTS",
    "+-",
    "TS_perc",
    "eFG_perc",
    "3PAr",
    "FTA",
    "FTr",
    "ORB_perc",
    "DRB_perc",
    "TRB_perc",
    "AST_perc",
    "STL_perc",
    "BLK_perc",
    "TOV_perc",
    "USG_perc",
    "ORtg",
    "DRtg",
    "BPM",
]

DF_FEATURES = [
    "Date",
    "Name",
    "Team",
    "Pos",
    "FPTS",
    "Salary",
    # Additional Features
    "Starter",
    "Rest",
    "Rota_All",
    "Rota_Pos",
    "Home",
    "PG",
    "SG",
    "F",
    "C",
    "Value",
    "FPTS_std",
    # Basic Stats with weighted mean
    "PTS",
    "3P",
    "AST",
    "TRB",
    "STL",
    "BLK",
    "TOV",
    "DD",
    "TD",
    # Additional Stats with weighted mean
    "MP",
    "FT",
    "FTA",
    "FGA",
    "3PA",
    "DRB",
    "ORB",
    # Advanced Stats with weighted mean
    "USG_perc",
    "DRtg",
    "ORtg",
    "AST_perc",
    "DRB_perc",
    "ORB_perc",
    "BLK_perc",
    "TOV_perc",
    "STL_perc",
    "eFG_perc",
    "FG_perc",
    "3P_perc",
    "FT_perc",
]

# Scoring rules based on https://www.draftkings.co.uk/help/rules/4
MULTIPLIERS = {
    "PTS": 1,
    "3P": 0.5,
    "TRB": 1.25,
    "AST": 1.5,
    "STL": 2,
    "BLK": 2,
    "TOV": -0.5,
}
