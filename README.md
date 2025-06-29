# 🧪 Python Code Quality Analyzer (בודק איכות קוד בפייתון)

A FastAPI-based project that analyzes uploaded Python code to detect common quality issues and generate charts.  
הפרויקט בודק קוד פייתון ומציג גרפים שמתארים בעיות נפוצות בקוד, כמו פונקציות ארוכות מדי, חוסר בתיעוד, ומשתנים לא בשימוש.

---

## 📌 Features (תכונות)

- ✅ Detects long functions (פונקציות מעל 20 שורות)
- ✅ Checks for missing docstrings (ללא תיעוד פנימי)
- ✅ Finds unused variables (משתנים שלא נעשה בהם שימוש)
- ✅ Counts issues and visualizes them using:
  - Histogram (היסטוגרמה)
  - Pie chart (גרף עוגה)
  - Bar chart (גרף עמודות)

---

## 📁 Project Structure (מבנה פרויקט)

```
project/
├── Main.py             # קובץ ראשי הכולל API, ניתוח וגרפים
├── requirements.txt    # קובץ התקנות תלות
└── README.md           # תיעוד
```

---

## 🛠️ Installation (התקנה)

```bash
git clone <your-repo-url>
cd project

# Create virtual environment (סביבת פיתוח מבודדת)
python -m venv .venv
# Activate:
.venv\Scripts\activate       # Windows
source .venv/bin/activate      # Linux/Mac

# Install dependencies (התקנת ספריות)
pip install -r requirements.txt
```

---

## 🚀 Running the App (הרצת המערכת)

```bash
uvicorn Main:app --reload
```

App will be live at:  
http://localhost:8000

---

## 📤 Usage (שימוש)

### ▶️ Upload a Python File (שליחת קובץ פייתון)

```bash
curl -X POST http://localhost:8000/analyze/ -F "file=@main.py"
```

### ▶️ Send raw code as string (שליחת קוד כמחרוזת טקסט)

```bash
curl -X POST http://localhost:8000/analyze/ \
     -H "Content-Type: application/json" \
     -d "{\"source_code\": \"def hello():\\n    print('hi')\"}"
```

### 📥 Download generated charts (הורדת גרפים)

```
GET /download/histogram.png
GET /download/pie_chart.png
GET /download/bar_chart.png
```

---

## 🧪 Output Explanation (פלט ניתוח)

- **histogram.png** – Shows the length of each function in the code (פונקציות לפי מספר שורות)
- **pie_chart.png** – Shows the percentage of each warning type (אחוז יחסי של בעיות)
- **bar_chart.png** – Shows how many issues were detected per type (מספר בעיות לפי סוג)

---

## 📦 Dependencies (תלויות פרויקט)

- fastapi  
- uvicorn  
- matplotlib

📄 See: `requirements.txt`

---

## 📄 License

This project is open for educational use.  
הפרויקט פתוח לצרכי למידה ופרויקטים אישיים.

---

## 👤 Author

Project by Navashechter  
Feel free to use and extend it!  
בהצלחה 😄
