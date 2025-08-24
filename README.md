# 💱 Currency Converter (Python)

A simple Python command-line currency converter that uses **[FreeCurrencyAPI](https://freecurrencyapi.com/)** to fetch real-time exchange rates.  
This tool allows you to **list available currencies, check exchange rates, and convert amounts** between different currencies in real time.

---

## 🚀 Features
- 📋 Get a list of all supported currencies  
- 💹 Check live exchange rates between two currencies  
- 🔄 Convert any amount from one currency to another  
- 💻 Simple command-line interface (CLI)  

---

## 📌 Requirements
- Python 3.x
- `requests` library

Install dependencies with:
```bash
pip install requests
```

---

## ▶️ Usage
Run the program:
```bash
python main.py
```

Available commands:
- `list` → Shows all supported currencies  
- `rate` → Get exchange rate between two currencies  
- `convert` → Convert an amount from one currency to another  
- `q` → Quit the program  

### Example:
```
Welcome to the currency converter!
List - lists the different currencies
Convert - convert from one currency to another
Rate - get the exchange rate of two currencies

Enter a command (q to quit): convert
Enter a base currency: USD
Enter an amount in USD: 100
Enter a currency to convert to: INR
100.0 USD is equal to 8321.45 INR
```

---

## ⚡ API
This project uses [FreeCurrencyAPI](https://freecurrencyapi.com/) for real-time exchange rates.  

👉 You need your own API key.  
Replace the value of `API_KEY` inside `main.py` with your key:
```python
API_KEY = "your_api_key_here"
```

---

## 📂 Project Structure
```
.
├── main.py         # Main program
├── README.md       # Documentation
```

---

## 🛠️ Future Improvements
- Add caching to reduce API calls  
- Show top 10 most-used currencies by default  
- Add error handling for API downtime  
- Build a GUI version using Tkinter or React frontend  

---

## 👨‍💻 Author
**Shubham Bhatt**  
- [LinkedIn](https://www.linkedin.com/in/codingshubham)  
- [GitHub](https://github.com/code-shubhambhatt)  

---
