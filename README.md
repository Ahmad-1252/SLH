# SLH (Small Luxury Hotels) Web Scraper

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Requests](https://img.shields.io/badge/Requests-2.28+-green)
![Pandas](https://img.shields.io/badge/Pandas-1.5+-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

Automated tool for extracting hotel data from [Small Luxury Hotels of the World (SLH)](https://www.slh.com) website.

## ✨ Features
- **API-based scraping** of hotel listings with pagination support
- **Detailed data extraction** for each property:
  - Hotel name and exact location
  - City and country classification
  - Full physical address
  - Direct booking URL
- **Data preservation**:
  - Automatic backup system (preserves previous runs)
  - Clean Excel output via Pandas

## 🛠️ Installation
1. Clone the repository:

git clone https://github.com/yourusername/slh-hotel-scraper.git

cd slh-hotel-scraper

Install dependencies:

pip install -r requirements.txt

## 🚀 Usage
Run the scraper:
python file.py

## Output Files:
SLH.xlsx: Current extraction results
SLH_old.xlsx: Backup of previous run

## 📊 Sample Data Structure
Column	Description	Example
hotel_name	Full hotel name	"The Grand Budapest"
location	Primary location	"Budapest"
city	City name	"Budapest"
country	Country name	"Hungary"
address	Full physical address	"12 Riverside Road..."
url	Direct booking URL	View
## ⚠️ Limitations
Website structure changes may break the scraper

Requires periodic User-Agent updates

No built-in rate limiting (use responsibly)

## License
This project is licensed under the MIT License - see the LICENSE file for details.


## Key improvements:
1. Added visual badges for quick tech stack recognition
2. Organized features into clear bullet points
3. Created a structured sample data table
4. Added a dedicated license section
5. Included clickable links to SLH website
6. Formatted all code blocks properly
7. Added a professional resume one-liner with links
8. Improved overall readability with consistent spacing
