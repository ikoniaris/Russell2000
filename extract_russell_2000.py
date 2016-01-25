import csv

__author__ = 'reedn'

# Read CIK's, Names into ticker_info, dictionary of ticker to CIK and Name
tickers_to_ciks = {}
with open("cik_ticker.csv", "r") as cik_ticker_in:
    reader = csv.DictReader(cik_ticker_in, delimiter='|')
    for row in reader:
        cik = row['CIK']
        ticker = row['Ticker']
        name = row['Name']
        tickers_to_ciks[ticker] = cik

missing_ciks = []

# Read Russell 2000 components (ticker, Name) and for each one,
# get the CIK, either from ticker_info, if it exists, or scrape
# it from the web

row_count = 0
with open("russell_2000_components.csv", "r") as components_in:
    reader = csv.DictReader(components_in)
    with open("russell_2000_cik_to_ticker.csv", "w") as cik_ticker_out:
        writer = csv.DictWriter(cik_ticker_out, ['CIK', 'Ticker', 'Name'])
        writer.writeheader()
        for row in reader:
            row_count += 1
            print(row)
            company_name = row['Name']
            ticker = row['Ticker']
            output_row = dict()
            output_row['Ticker'] = ticker
            cik = tickers_to_ciks.get(ticker)
            # Scrape
            #if not cik:
            #    print("No CIK for " + ticker)
                #cik = scrape_company_cik(company_name)
            if cik:
                output_row['CIK'] = cik
                output_row['Name'] = company_name
                writer.writerow(output_row)
            else:
                missing_ciks.append({'Ticker' : ticker, 'Name' : company_name})

print "%d components processed." % row_count

with open("missing_ciks.csv", "w") as missing_ciks_out:
    writer = csv.DictWriter(missing_ciks_out, ['Ticker', 'Name'])
    writer.writeheader()
    for missing_info in missing_ciks:
        writer.writerow(missing_info)
