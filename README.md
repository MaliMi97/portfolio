# on-chain-analytics

This is a personal Python project and PostgreSQL, where I play with cryptocurrencies.

In src there are the following packages and jupiter notebooks.

the packages:
api - Contains classes for connecting to APIs.
functions - Contains various functions, which take dataframes of prices, volumes, market caps, etc. as arguments and compute something.
postgre_sql - Contains class, which helps to fill data into a PostgreSQL database.
visualization - Functions, which help with the vizualization of data obtained by the APIs and functions from functions package.

the notebooks:
correlation_analysis.ipynb - Shows vizualization of how some cryptocurrencies' prices and returns correlate.
impermanent_loss.ipynb - Computes the impermanent loss of yield farming assuming that the amount of assets in the pool remains constant.
postgre_sql.ipynb - Fills data into a PostgreSQL database.
realized_metrics.ipynb - Vizualizes some on-chain metrics for bitcoin.
trial-and-error.ipynb - Notebook for trying out new stuff.


I used PostgreSQL version 12 and Puthon version 3.9.7
Packages for Python can be seen in requirements.txt
In order to install the psycopg2, the postgre package libpq-dev must be installed.

