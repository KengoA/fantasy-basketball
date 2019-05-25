## NBA Player Performance Prediction and Lineup Optimization

Prediction of NBA player performance defined as Fantasy Points by Draft Kings.
This project was conducted and approved by a reviewer as part of Machine Learning Engineer Nanodegree by Udacity. See the final report [here](https://github.com/KengoA/fantasy-basketball/blob/master/report.pdf) for overview.

### [This project is under major refactoring as of May 2019]

### What We'll Do

The end goal of this project is to generate a series of lineups for a fantasy basketball website [DraftKings](https://www.draftkings.com/). To achieve that, we'll scrape player statististics from each regular season game starting in the 2014-15 season as well as past fantasy salary information. First, we'll build a predictive model for player performance, and then we will use genetic algorithm to construct fantasy lineups to maximize the total fantasy points while satisfying the salary constraint.

### What We Won't Do

Given the complexity of the series structure and difference in nature, we won't be considering playoff games. In addition, a major factor omitted from our analysis is the opponent's defensive ability as a team or at a givne position (for instance, Paul George is excellent at stealing the ball), which arguably is one of the most important factors of the game. Tackling this aspect will be an easy improvement to this project.

### Exploratory Data Analysis

The key to select a good fantasy lineup is to identify players that are consistent performers. This basic intuition comes from [Modern Portfolio Theory](https://www.investopedia.com/terms/m/modernportfoliotheory.asp), and the following scatter plot looks at the relationship between risk and return, where return is the average fantasy points over a given range of games (in this case, past 10 games) and risk is its standard deviation. For a given level of risk, a player with a better return is considered to be superior. The plot is based on the late 2018-19 season statistics, where Lebron James with a 10-game average of a whopping 58.1 fantasy points and a 7.4 standard deviation. In general, players on the outer left of the cluster are considered as good assets with low risk and high return. Players are color coded based on rough positions of PG, SG, F (SF, PF, SF/PF), and C (PF/C, C).

![10-game risk-return](assets/risk_return.gif)

### Project Structure

This project consists of 7 Jupyter notebooks and functionalities are described below.

- [1.data_scraping.ipynb](src/1.data_scraping.ipynb) scrapes games data from Basketball-Reference.com and salary and position information from RotoGuru.

- [2.merging_data.ipynb](src/2.preprocessing.ipynb) merges the two datasets with name standardisation and preliminary preprocessing of data such as calculation of FPTS based on the key statistics.

- [3.exploratory_analysis.ipynb](src/3.exploratory_analysis.ipynb) visually explores relationships between; salary and actual FPTS and; expected FPTS and standard deviation of the past 10 games.

- [4.feature_engineering.ipynb](src/4.feature_engineering.ipynb) constructs the baseline model with simple average along with additional three datasets with weighted average, where several features are engineered and incorporated.

- [5.modeling.ipynb](src/5.modeling.ipynb) comparatively examines the baseline model, linear regression, gradient boosting, and deep learning models with different specifications with 5-fold cross validation. Predictions for games in the month of March 2018 are written into a csv file.

- [6.lineup_optmisation.ipynb](src/6.lineup_optmisation.ipynb) uses Genetic Algorithms to select best combinations of players on a given set of games ans predictions. Performance of the lineups chosen by the algorithm against other DraftKings users is examined for contests held in March, 2018. Note that the contest data is manually obtained from Rotogrindrs' ResultsDB page without scraping. Predictions from the baseline model and final model are compared to the actual performance.

- [7.robustness_check.ipynb](src/7.robustness_check.ipynb) checks the final model's robustness and statistical significant using Gaussian noise addition and t-test.

Main procedures are coded and explained in markdown using Jupyter Notebook. Although not requred, jupyter nbextentions are highly recommended for convenience and visibility (see link). Useful extensions are Codefolding, ExecuteTime, Collapsible Headings, and Variable Inspector. http://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html
