# Pit strategy optimizer

Calculates optimal pit strategy for simracing events based on data which includes:

* Lap-times with regard to tyre-types and tyre-wear
* Limited driving range  because of finite fuel supply
* Duration of pit stops

## Install

### Install the project to your machine

```
cd ~
git clone git@gitlab.com:hallgrimur1471/pit_strategy_optimizer
cd pit_strategy_optimizer
python3.7 -m pip install --upgrade --user virtualenv
virtualenv .virtualenv
source .virtualenv/bin/activate
python3.7 -m pip install --upgrade -r requirements.txt
```

### Enable Google Sheets API

Open [this](https://developers.google.com/sheets/api/quickstart/python) link and click the "Enable the Google Sheets API" button. After accepting the terms click "Download client configuration" and save the file to `~/pit_strategy_optimizer/.credentials.json`

## Usage

Data should be logged to a spreadsheet document, using some predefined setup of the spreadsheet ([See this example WIP spreadsheet](https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit?usp=sharing)).

```
cd ~/pit_strtategy_optimizer
source .virtualenv/bin/activate
./calculate_optimal_strategy.py --help
```

## Development tools used

Fixer: [black](https://github.com/ambv/black)

## Authors

* **Hallgrímur Davíð Egilsson** - [github](https://github.com/hallgrimur1471)
* **Arnar Þór Gíslason** - [github](https://github.com/arnargisla)
