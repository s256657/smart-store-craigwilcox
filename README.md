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

To be continued......