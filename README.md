# Russell 2000

## Data

* cik_ticker.csv: File of tik-to-cik mappings, company names
* russell_2000_components.csv
* Generated: russell_2000_cik_to_ticker.csv, missing_ciks.csv, missing_cik_ticker.csv

## Scripts

* parse_russell_2000_components.py:
- Used to extract Russell 2000 components from http://www.barchart.com/stocks/russell2000.php?_dtp1=0
- Writes to russell_2000_components.csv

* extract_russell_2000.py:
- Using russell_2000_components.csv and cik_ticker.csv, gets the CIK's for each of the Russell 2000 components
- Writes to russell_2000_cik_to_ticker.csv, missing_ciks.csv

* scrape_missing_components.py
- Scrape the CIK's for companies not found in cik_ticker.csv
- Write results to missing_cik_ticker.csv





