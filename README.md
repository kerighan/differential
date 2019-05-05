# Richguys

Wanna get rich huh ?

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

miniconda 3.


### Installing

Create a clean python environment
```
conda create -n {name} python=3.7
source activate {name}
```
or
```
conda activate {name}
```

Install cython
```
pip install cython
```
Go to the convectors clone folder (where the setup.py is)
```
pip install .
```

Go to the richguys clone folder (where the setup.py is)
```
pip install .
```


## Getting data from Google Sheets

First you have to add the following environment variables to your .bashrc:
```
export RICHGUYS_CREDENTIALS=/path/to/your/credentials.json
export RICHGUYS_SHEETS=/path/to/your/sheets_credentials.json
```

Now you can directly download the bettings data:
```
from richguys import save_betting, load_betting

save_betting()  # will create a dataframe from google sheets data
df = load_betting(only_results=True)  # `False` to get all results
```

## Train a Neural Net

Training can be done in one simple step:

```
from richguys import load_betting
from richguys.predictor.nn import train

df = load_betting(only_results=True)
train(df)
```

Note that it will create a `models/` folder in your current directory with one file : `predictor.p` the pickled class of choice.


## Use a Neural Net


```
import pickle

with open("predictor.p", "rb") as f:
    pred = pickle.load(f)

test_data = {
    "id": "2487455",
    "id_sportradar": "17393485",
    "date": "2019-04-11",
    "type": "baseball",
    "cote_1": 1.75,
    "cote_2": 1.6,
    "o_actual_1": 48,
    "o_expected_1": 53,
    "o_actual_2": 65,
    "o_expected_2": 57,
    "vote_1": 12,
    "vote_2": 53,
    "vote_n": 32,
    "country": "australia"
}
print(pred.predict_match(test_data, p_min=.2, ev_min=.2))  # which bet to make
print(pred.predict_match(test_data, return_results=True))  # get probabilistic data
```

## Authors

* **Rich Guy 1** - *cool dude*
* **Rich Guy 2** - *another cool dude*
