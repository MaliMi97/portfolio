# Portfolio

This portfolio contains the following Python and PostgreSQL projects.

* **crypto**:  This is a personal Python project and PostgreSQL, where I play with cryptocurrencies. 
* **TASEP**: Python school project cointaining very basic models, which simulate how pedestrians walk in one dimension

## crypto

**the packages:**

* api - Contains classes for connecting to APIs.
* functions - Contains various functions, which take dataframes of prices, volumes, market caps, etc. as arguments and compute something.
* postgre_sql - Contains class, which helps to fill data into a PostgreSQL database.
* visualization - Functions, which help with the vizualization of data obtained by the APIs and functions from functions package.

**the notebooks:**
* correlation_analysis.ipynb - Shows vizualization of how some cryptocurrencies' prices and returns correlate.
* impermanent_loss.ipynb - Computes the impermanent loss of yield farming assuming that the amount of assets in the pool remains constant.
* postgre_sql.ipynb - Fills data into a PostgreSQL database.
* realized_metrics.ipynb - Vizualizes some on-chain metrics for bitcoin.
* trial-and-error.ipynb - Notebook for trying out new stuff.

**requirements:**

* PostgreSQL version 12 
* libpq-dev
* Python version 3.9.7
* ipykernel
* numpy==1.20.3
* requests==2.26.0
* python-dateutil==2.8.2
* pandas==1.3.4
* psycopg2==2.8.6
* matplotlib==3.4.3
* seaborn==0.11.2


## TASEP

**the python scripts and notebooks:**

* TASEP.py - contains two basic models, which determine how the pedestrians walk, and their parent class.
* DataProcessing.py - Processes the data obtained from the two models.
* Results.py - processes and visualizes results
* TASEP.ipynb - shows everything together

**requirements:**

* Python version 3.9.7
* numpy==1.20.3
* pandas==1.3.4
* matplotlib==3.4.3
