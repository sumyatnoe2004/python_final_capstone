# python_final_capstone
Final Capstone Project

# Mobile Phone Web Scraping Project

## Overview

This project is a Python web scraper that collects smartphone product data from AnyCall Mobile Myanmar:

https://anycallmobilemm.com/product-category/smartphone/

The scraper automatically visits every page in the smartphone category, extracts product details, and exports the data into Excel files.

This project was created for educational purposes to practice Python web scraping, data cleaning, and exporting structured data.

---

## Data Collected

The scraper collects:

- Product Name
- Product Price
- Smartphone Brand

---

## Tools & Libraries Used

- Python
- requests
- BeautifulSoup4
- pandas
- tqdm
- html5lib
- datetime

---

## How It Works

1. Requests the smartphone category page
2. Detects the total number of pages automatically
3. Visits each page one by one
4. Extracts:
   - product name
   - product price
   - smartphone brand
5. Stores the results in pandas DataFrames
6. Exports:
   - individual Excel files for each page
   - one final combined Excel file

---

## Output Files

The script generates:

### Page-by-page Excel files
```bash
Final Capstone Project Batch 4 1 YYYY-MM-DD.xlsx
Final Capstone Project Batch 4 2 YYYY-MM-DD.xlsx
```

### Final combined dataset
```bash
Final Data.xlsx
```

---

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Install required packages:

```bash
pip install requests beautifulsoup4 pandas tqdm html5lib
```

---

## Run the Script

```bash
python scraper.py
```

---

## Example Output

| Name | Price | Brand |
|------|-------:|------|
| Samsung Galaxy A15 | 750000 | Samsung |
| Redmi Note 13 | 890000 | Mi |
| Oppo Reno 12 | 1200000 | Oppo |

---

## Learning Outcomes

This project demonstrates:

- Web scraping with Python
- HTML parsing with BeautifulSoup
- Pagination scraping
- Data cleaning
- Brand extraction from text
- Working with pandas DataFrames
- Exporting data to Excel
- Basic automation

---

## Educational Purpose

This project was built for learning and academic practice only.

Please scrape responsibly and respect website policies before collecting data from any website.

---

## Author

**Su Myat Noe**  
Student at Python Myanmar Institute
