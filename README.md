SLH (Small Luxury Hotels) Web Scraper
Python
Requests
Pandas

Automated tool for extracting hotel data from Small Luxury Hotels of the World (SLH) website, including names, locations, addresses, and booking URLs.

✨ Features
API-based scraping of hotel listings

Detailed data extraction for each property:

Hotel name and location

City and country classification

Full physical address

Direct booking URL

Automatic backup system (preserves previous runs)

Pandas integration for clean Excel output

🛠️ Installation
bash
git clone https://github.com/yourusername/slh-hotel-scraper.git
cd slh-hotel-scraper
pip install -r requirements.txt
🚀 Usage
bash
python slh_scraper.py
Output will be saved to SLH.xlsx with previous runs backed up as SLH_old.xlsx

📊 Sample Output
hotel_name	location	city	country	address	url
The Grand Budapest	Budapest	Hungary	Europe	12 Riverside Road...	View

⚠️ Limitations
Requires SLH website structure to remain consistent

May need header/UA updates periodically

No built-in rate limiting
