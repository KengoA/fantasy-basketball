## NBA Player Performance Prediction and Lineup Optimization

Prediction of NBA player performance defined as Fantasy Points by Draft Kings.
This project was done as part of Machine Learning Engineer Nanodegree by Udacity. See the final report [here](https://github.com/KengoA/fantasy-basketball/blob/master/report.pdf) for overview.

## This project is under major refactoring as of May 2019 (1/7 done)

This project consists of 7 Jupyter notebooks and functionalities are described below.

- [1.data_scraping.ipynb](notebooks/1.data_scraping.ipynb) scrapes games data from Basketball-Reference.com and salary and position information from RotoGuru.

- [2.preprocessing.ipynb](notebooks/2.preprocessing.ipynb) merges the two datasets with name standardisation and preliminary preprocessing of data such as calculation of FPTS based on the key statistics.

- [3.exploratory_analysis.ipynb](notebooks/3.exploratory_analysis.ipynb) visually explores relationships between; salary and actual FPTS and; expected FPTS and standard deviation of the past 10 games.

- [4.feature_engineering.ipynb](notebooks/4.feature_engineering.ipynb) constructs the baseline model with simple average along with additional three datasets with weighted average, where several features are engineered and incorporated.

- [5.modeling.ipynb](notebooks/5.modeling.ipynb) comparatively examines the baseline model, linear regression, gradient boosting, and deep learning models with different specifications with 5-fold cross validation. Predictions for games in the month of March 2018 are written into a csv file.

- [6.lineup_optmisation.ipynb](notebooks/6.lineup_optmisation.ipynb) uses Genetic Algorithms to select best combinations of players on a given set of games ans predictions. Performance of the lineups chosen by the algorithm against other DraftKings users is examined for contests held in March, 2018. Note that the contest data is manually obtained from Rotogrindrs' ResultsDB page without scraping. Predictions from the baseline model and final model are compared to the actual performance.

- [7.robustness_check.ipynb](notebooks/7.robustness_check.ipynb) checks the final model's robustness and statistical significant using Gaussian noise addition and t-test.

Main procedures are coded and explained in markdown using Jupyter Notebook. Although not requred, jupyter nbextentions are highly recommended for convenience and visibility (see link). Useful extensions are Codefolding, ExecuteTime, Collapsible Headings, and Variable Inspector. http://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html
