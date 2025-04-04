# smart-store-craigwilcox
## Purpose
The purpose of this project is to have a space for experimenting and learning about Business Intellegence.

- Note: all commands are using macOS if using project as a guide with another operating system execution commands may be different.

## Project initialization
1. Create new project in github named smart-store-"yourname"
2. Pull project to local machine
```
cd ~
mkdir Projects
cd Projects
git clone https://github.com/s256657/smart-store-craigwilcox
cd smart-store-craigwilcox
code .
```
3. Added .gitignore and requirements.txt folders
4. created and activate virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```
5. Installed dependencies
```
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt
```

## Organize and add raw data
1. Create folders for use later: data/raw, scripts, utils/logger.py
2. Create files within data/raw
   - customer_data.csv
   - products_data.csv
   - sales_data.csv
3. Add raw data to newly created files (see examples to gather data)

## Add basic scripts and log
1. Create utils/logger.py
- Create file named logger.py in utils folder
- Copy code from repo into new logger.py file
2. Create scripts/data_prep.py
- Create folder named scripts
- Create new file in scripts folder named data_prep.py
- Copy code from repo into new data_prep.py
3. Execute python script
```
python3 scripts/data_prep.py
```

## Add Additional Data
- Added unique data to dataset 
1. Download raw data to excel to add columns
2. If following project on own can use any columns headings or data you would like I used the data below
   - Customers - TotalTransactions and LoyaltyStatus
   - Product - Daystoreceive and Customizable
   - Sales - LoyaltyPercentage and BillType
3. Load data back to corresponding raw files

## Clean and prepare data
1. Create prep scripts
   - In scripts folder create data_preperation subfolder
   - Create 3 separate "prepare" files 
2. Run scripts
```
python3 scripts/data_preparation/prepare_customers_data.py
python3 scripts/data_preparation/prepare_products_data.py
python3 scripts/data_preparation/prepare_sales_data.py
```
3. After scripts have run new prepared data should appear as new files named customers_prepared_data.csv

## Generic data scrub and test
- Though not needed as data is clean added generic data scubber as this is a learning module
1. Create data_scrubber.py file in scripts and copy code
2. Create tests folder and the test_data_scrubber.py 
3. Run test to ensure code works properly
```
python3 tests/test_data_scrubber.py
```

## Create and load data warehouse
1. Create two files in scripts folder create_dw.py and etl_to_dw.py
   - I created two files for organization purposes create_dw.py to make sure the data warehouse is formatted properly and etl_to_dw.py it to load data
   - See specific files for code
2. Create data warehouse
'''
python3 scripts/create_dw.py
'''
3. Load data to data warehouse
'''
python3 scripts/etl_to_dw.py
'''

To be continues....