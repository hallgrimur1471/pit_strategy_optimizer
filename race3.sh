#!/usr/bin/env bash

set -e

pit_time=15
sed -i 's/last_tyre_type = \"RS\"/last_tyre_type = \"RH\"/g' src/optimizer.py
sed -i 's/average_pit_stop_time = 40/average_pit_stop_time = 15/g' src/optimizer.py
echo "TYRES: RH, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
sed -i 's/last_tyre_type = \"RH\"/last_tyre_type = \"RM\"/g' src/optimizer.py
echo "TYRES: RM, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
sed -i 's/last_tyre_type = \"RM\"/last_tyre_type = \"RS\"/g' src/optimizer.py
echo "TYRES: RS, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0


pit_time=20
sed -i 's/last_tyre_type = \"RS\"/last_tyre_type = \"RH\"/g' src/optimizer.py
sed -i 's/average_pit_stop_time = 15/average_pit_stop_time = 20/g' src/optimizer.py
echo "TYRES: RH, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
sed -i 's/last_tyre_type = \"RH\"/last_tyre_type = \"RM\"/g' src/optimizer.py
echo "TYRES: RM, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
sed -i 's/last_tyre_type = \"RM\"/last_tyre_type = \"RS\"/g' src/optimizer.py
echo "TYRES: RS, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0

pit_time=25
sed -i 's/last_tyre_type = \"RS\"/last_tyre_type = \"RH\"/g' src/optimizer.py
sed -i 's/average_pit_stop_time = 20/average_pit_stop_time = 25/g' src/optimizer.py
echo "TYRES: RH, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
sed -i 's/last_tyre_type = \"RH\"/last_tyre_type = \"RM\"/g' src/optimizer.py
echo "TYRES: RM, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
sed -i 's/last_tyre_type = \"RM\"/last_tyre_type = \"RS\"/g' src/optimizer.py
echo "TYRES: RS, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0

pit_time=30
sed -i 's/last_tyre_type = \"RS\"/last_tyre_type = \"RH\"/g' src/optimizer.py
sed -i 's/average_pit_stop_time = 25/average_pit_stop_time = 30/g' src/optimizer.py
echo "TYRES: RH, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
sed -i 's/last_tyre_type = \"RH\"/last_tyre_type = \"RM\"/g' src/optimizer.py
echo "TYRES: RM, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
sed -i 's/last_tyre_type = \"RM\"/last_tyre_type = \"RS\"/g' src/optimizer.py
echo "TYRES: RS, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0

pit_time=35
sed -i 's/last_tyre_type = \"RS\"/last_tyre_type = \"RH\"/g' src/optimizer.py
sed -i 's/average_pit_stop_time = 30/average_pit_stop_time = 35/g' src/optimizer.py
echo "TYRES: RH, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
sed -i 's/last_tyre_type = \"RH\"/last_tyre_type = \"RM\"/g' src/optimizer.py
echo "TYRES: RM, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
sed -i 's/last_tyre_type = \"RM\"/last_tyre_type = \"RS\"/g' src/optimizer.py
echo "TYRES: RS, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0

pit_time=40
sed -i 's/last_tyre_type = \"RS\"/last_tyre_type = \"RH\"/g' src/optimizer.py
sed -i 's/average_pit_stop_time = 35/average_pit_stop_time = 40/g' src/optimizer.py
echo "TYRES: RH, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
sed -i 's/last_tyre_type = \"RH\"/last_tyre_type = \"RM\"/g' src/optimizer.py
echo "TYRES: RM, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
sed -i 's/last_tyre_type = \"RM\"/last_tyre_type = \"RS\"/g' src/optimizer.py
echo "TYRES: RS, PIT_TIME: ${pit_time}"
./calculate_optimal_strategy.py https://docs.google.com/spreadsheets/d/1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit#gid=0
