## NBA Player Performance Prediction and Lineup Optimization
Prediction of NBA player performance defined as Fantasy Points by Draft Kings

This project consists of 7 Jupyter notebooks and functionalities are described below.

  * 1.scrape_data.ipynb scrapes games data from Basketball-Reference.com and salary and position information from RotoGuru.

  * 2.preprocessing.ipynb merges the two datasets with name standardisation and preliminary preprocessing of data such as calculation of FPTS based on the key statistics.

  * 3.exploratory_analysis.ipynb visually explores relationships between; salary and actual FPTS and; expected FPTS and standard deviation of the past 10 games.

  * 4.feature_engineering.ipynb constructs the baseline model with simple average along with additional three datasets with weighted average, where several features are engineered and incorporated.

  * 5.modeling.ipynb comparatively examines the baseline model, linear regression, gradient boosting, and deep learning models with different specifications with 5-fold cross validation. Predictions for games in the month of March 2018 are written into a csv file.

  * 6.lineup_optmisation.ipynb uses Genetic Algorithms to select best combinations of players on a given set of games ans predictions. Performance of the lineups chosen by the algorithm against other DraftKings users is examined for contests held in March, 2018. Predictions from the baseline model and final model are compared to the actual performance.

  * 7.robustness_check.ipynb checks the final model's robustness and statistical significant using Gaussian noise addition and t-test.




This project is written in Python 3.6.3 as of May 21st, 2018, using Anaconda 4.4.0 (64-bit).
Main procedures are coded and explained in markdown using Jupyter Notebook. Although not requred, jupyter nbextentions are highly recommended for convenience and visibility (see link). Useful extensions are Codefolding, ExecuteTime, Collapsible Headings, and Variable Inspector. http://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html

Below is an alphabetical list of all libraries requred. The indented lines show the dependencies of the above line.Tenforflow backend is used for keras. pip3 is recommended for installation of libraries. (*) indicates dependencies of the preceding library.

bs4
colorlover
datetime
glob
keras
*pyyaml, tensorflow, six
numpy
matplotlib
*numpy, six, python-dateutil, pytz, cycler, pyparsing
os
pandas
*pytz, numpy, python-dateutil
pandas_profiling
plotly
seaborn
tqdm
urllib
sklearn
*numpy, scipy, scikit-learn
