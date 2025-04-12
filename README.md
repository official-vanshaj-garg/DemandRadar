# 🚀 DemandRadar

**DemandRadar** is a platform that bridges the gap between community needs and business opportunities. It empowers citizens to report missing services in their area and helps businesses make data-driven decisions using real-time geo-tagged insights.

---

## 🌟 Features

- ✅ **Community Needs Reporting** – Citizens can report missing services like gyms, banks, or ATMs.
- 📊 **Business Intelligence Dashboard** – Businesses access heatmaps and data insights for strategic expansion.
- 🔥 **Heatmap Visualization** – Interactive heatmaps show demand density using Leaflet.js.
- 💬 **Review & Testimonial System** – Users can share experiences and feedback.
- 🌐 **Live Insights** – Track emerging trends in different areas.
- 🧭 **Location-based Analysis** – All insights are geo-tagged and mapped in real-time.

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (Flask)  
- **Database**: MongoDB  
- **Maps**: Leaflet.js + Heatmap.js  
- **Icons**: Font Awesome  
- **Others**: dotenv, Flask extensions  

---

## 📦 Prerequisites

- Python 3.8+
- MongoDB installed and running locally or on cloud (MongoDB Atlas)
- Git

---

## ⚙️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/DemandRadar.git
cd DemandRadar
```

2. **Create and Activate Virtual Environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Environment Variables**

Create a `.env` file in the root directory and add:

```
SECRET_KEY=your_secret_key
MONGO_URI=your_mongodb_connection_string
```

5. **Create Required Directories**

```bash
mkdir app/static/uploads
```

---

## 🚀 Running the Application

1. Ensure MongoDB is running.
2. Activate the virtual environment:

```bash
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. Run the app:

```bash
python run.py
```

4. Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🧾 Project Structure

```plaintext
DemandRadar/
├── app/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── uploads/
│   ├── templates/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── venv/
├── .env
├── .gitignore
├── requirements.txt
└── run.py
```

---

## 📡 API Endpoints

| Method | Endpoint                | Description                         |
|--------|-------------------------|-------------------------------------|
| POST   | `/submit-report`        | Submit a missing service report     |
| POST   | `/submit-review`        | Submit a user review                |
| GET    | `/get-reviews`          | Fetch recent user reviews           |
| POST   | `/send-referral`        | Send referral invitation via email  |
| POST   | `/subscribe-newsletter` | Subscribe to newsletter             |

---

## 👨‍💻 Development Setup

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Set up pre-commit hooks:

```bash
pre-commit install
```

---

## 🚢 Deployment Tips

To deploy on services like Heroku, Railway, or Render:

- Configure `.env` variables on the platform
- Set up MongoDB Atlas or hosted MongoDB
- Ensure static files are served correctly
- Configure email/referral APIs if applicable

---

## 🔐 Environment Variables

Your `.env` file should contain:

```env
SECRET_KEY=your_secret_key
MONGO_URI=your_mongo_uri
```

Add any others as needed (e.g., EMAIL_API_KEY if email features are used).

---



## 🙌 Contact

**Jaineesh**  
📧 jaineeshpatel73@gmail.com  
🔗 [GitHub Repo](https://github.com/jaineeshx/DemandRadar)

---

> ✨ Don't forget to ⭐ star the repo if you like the project!
