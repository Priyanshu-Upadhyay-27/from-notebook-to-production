# 🚀 FastAPI ML Deployment — From Notebook to Production

A hands-on learning journey of building and deploying Machine Learning models as production-ready REST APIs using FastAPI, Docker, and Cloud.

---

## 📌 What This Repo Is About

Most ML tutorials stop at the notebook. This project goes further —
taking a trained ML model and wrapping it in a real API that anyone in the world can call.

```
Jupyter Notebook  →  FastAPI  →  Docker  →  Cloud
```

---

## 🗂️ Project Structure

```
fastapi-ml-deployment/
├── main.py                  # FastAPI application
├── train_model.py           # Model training script
├── house_price_model.pkl    # Saved trained model
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker container config
└── README.md
```

---

## 🧠 What I Built

A **House Price Prediction API** that:
- Accepts house features (area, bedrooms, location, furnished)
- Validates all inputs automatically using Pydantic
- Runs a trained Linear Regression model
- Returns a predicted price in lakhs as JSON

### Sample Request
```json
POST /predict

{
  "area": 1500,
  "bedrooms": 3,
  "location": "delhi",
  "furnished": true
}
```

### Sample Response
```json
{
  "input_received": {
    "area": 1500,
    "bedrooms": 3,
    "location": "delhi",
    "furnished": true
  },
  "predicted_price_lakhs": 70.0
}
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **FastAPI** | API framework |
| **Pydantic** | Data validation |
| **Scikit-learn** | ML model |
| **Uvicorn** | ASGI server |
| **Docker** | Containerization |
| **Joblib** | Model serialization |

---

## ⚡ Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/fastapi-ml-deployment.git
cd fastapi-ml-deployment
```

**2. Create and activate virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Train and save the model**
```bash
python train_model.py
```

**5. Run the API**
```bash
uvicorn main:app --reload
```

**6. Open in browser**
```
http://127.0.0.1:8000/docs
```

---

## 🐳 Run with Docker

**1. Build the image**
```bash
docker build -t house-price-api .
```

**2. Run the container**
```bash
docker run -p 8000:8000 house-price-api
```

**3. Test at**
```
http://127.0.0.1:8000/docs
```

---

## 📚 Concepts Covered

- ✅ Type hints in Python
- ✅ FastAPI setup and routing
- ✅ Path parameters
- ✅ Query parameters
- ✅ Request body with Pydantic models
- ✅ POST vs GET methods
- ✅ Loading and serving an ML model
- ✅ Dockerizing a FastAPI app
- ⬜ Cloud deployment (coming soon)

---

## 🎯 Why I Built This

I was building ML models in Jupyter notebooks but had no idea how to make them accessible to the real world. This project bridges that gap — learning how to take any trained model and turn it into a production-ready API.

---

## 📈 What's Next

- [ ] Deploy on AWS EC2 / Render / Railway
- [ ] Add authentication to the API
- [ ] Try with a more complex ML model
- [ ] Add logging and monitoring

---

## 🙋 Author

**Priyanshu Upadhyay**

Learning ML Engineering — one API at a time.