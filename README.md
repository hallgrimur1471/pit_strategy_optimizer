# Pit strategy optimizer

Calculates optimal pit strategy for simracing events based on data which includes:

* Lap-times with regard to tyre-types and tyre-wear
* Limited driving range  because of finite fuel supply
* Duration of pit stops

## Usage

Data should be logged to a spreadsheet document, using some predefined setup of the spreadsheet ([See this example WIP spreadsheet](https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit?usp=sharing)).

```
./calculate_optimal_strategy.py --help
```


## Development tools used

Fixer: [black](https://github.com/ambv/black)

## Authors

* **Hallgrímur Davíð Egilsson** - [github](https://github.com/hallgrimur1471)
* **Arnar Þór Gíslason** - [github](https://github.com/https://github.com/arnargisla)
