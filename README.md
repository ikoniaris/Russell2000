# Russell 2000

## Data

Source data:
* cik_ticker.csv: Database of tik-to-cik mappings, company names. 13738 companies.
* russell2000.html: Web page which contains the russell 2000 ticker symbols.

Generated files:
* russell_2000_components.csv (ticker, name) - 1909 companies
* russell_2000_cik_to_ticker.csv (1635 companies)
* missing_ciks.csv (Tickers for 274 companies)
* missing_cik_ticker.csv (Ticker, CIK, Name for 274 companies): 

## Scripts

* parse_russell_2000_components.py:
- Used to extract Russell 2000 components from http://www.barchart.com/stocks/russell2000.php?_dtp1=0 (russell2000.html)
- Writes to russell_2000_components.csv

* extract_russell_2000.py:
- Using russell_2000_components.csv and cik_ticker.csv, gets the CIK's for each of the Russell 2000 components
- Writes to russell_2000_cik_to_ticker.csv, missing_ciks.csv

* scrape_missing_components.py
- Scrape the CIK's for companies not found in cik_ticker.csv
- Write results to missing_cik_ticker.csv





