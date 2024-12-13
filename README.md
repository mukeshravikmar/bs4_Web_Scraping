# Web Scraping Project with BeautifulSoup

## 🌟 Overview
This project demonstrates how to scrape product details such as names, URLs, prices, ratings, and review counts from an e-commerce website using **BeautifulSoup** and **Requests** in Python.

---

## 🛠️ Technologies Used
- **Python 3.x**: Core programming language.
- **BeautifulSoup**: Web scraping library for parsing HTML and XML.
- **Requests**: For sending HTTP requests.
- **Pandas**: For data manipulation and storage.

---

## ⚙️ How It Works
1. **Sending Requests:** The project sends HTTP requests to the target website using the Requests library.
2. **Parsing HTML:** BeautifulSoup parses the HTML content of the requested pages.
3. **Extracting Data:** Key product details are extracted based on specified HTML tags and class names.
4. **Data Storage:** Extracted data is stored in a CSV file using Pandas.

---

## 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   ```
2. Navigate to the project directory:
   ```bash
   cd yourproject
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📋 Requirements
Create a `requirements.txt` file with the following content:
```
requests
beautifulsoup4
pandas
```

---

## 🚀 Usage
1. **Update Configuration:**
   - `#Paste Your USER_AGENT` - Add your browser's user agent.
   - `#Use_Product_Link` - Add the base product link from the target website.
   - `#Use_Main_URL_LINK` - Add the main URL for generating complete product URLs.

2. **Run the Python Script:**
   ```bash
   python scrape_products.py
   ```
3. **View Results:**
   The results will be saved in a file named `Products_1.csv`.

---

## 📄 License
This project is licensed under the MIT License.

---

## 🙌 Acknowledgements
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/)

---

## 🤝 Contributing
