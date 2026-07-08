# 🚗 CarValue AI
## AI-Powered Used Car Price Prediction Platform

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![XGBoost](https://img.shields.io/badge/XGBoost-Machine%20Learning-orange?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn)

CarValue AI is an end-to-end Machine Learning web application that predicts the fair market value of used cars using an advanced **XGBoost Regression Model**. The application combines Machine Learning, Flask, and a modern responsive frontend to provide users with instant and accurate used car price predictions.

The model has been trained on the **Cardekho Used Car Dataset** containing over **15,000+ vehicle records**, enabling accurate predictions based on vehicle specifications and historical market trends.

---

# 🌟 Features

- 🚗 AI-Powered Used Car Price Prediction
- ⚡ Real-Time Price Estimation
- 📊 XGBoost Regression Model
- 🌐 Flask Backend API
- 🎨 Modern Responsive User Interface
- 📄 Downloadable PDF Valuation Report
- 📈 AI Market Insights
- 🔥 Premium Dark Theme
- 📱 Mobile Friendly
- ⚙️ Fast Prediction Engine
- 🧠 Machine Learning Powered Decision Making

---

# 📸 Application Overview

### Home Page

- Modern Landing Page
- Premium UI
- Workflow Explanation
- FAQ Section

### Prediction Page

- Vehicle Details Form
- Technical Specifications
- AI Price Prediction

### Result Dashboard

- Estimated Market Value
- Confidence Score
- Price Range
- AI Generated Insights
- Download PDF Report

---

# 🚀 Technologies Used

## Frontend

- HTML5
- CSS3
- JavaScript
- Font Awesome
- jsPDF

## Backend

- Python
- Flask
- Pandas
- NumPy

## Machine Learning

- XGBoost Regressor
- Scikit-Learn
- Ordinal Encoder
- Pickle

---

# 📂 Project Structure

```
CarValue_AI/
│
├── dataset/
│   └── cardekho_dataset.csv
│
├── model/
│   ├── car_price_model.pkl
│   └── encoder.pkl
│
├── notebook/
│   └── CarValue_AI.ipynb
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── Car_image.png
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

Dataset Used:

**Cardekho Used Car Dataset**

Dataset Size

- 15,000+ Records
- Multiple Car Brands
- Various Fuel Types
- Manual & Automatic Vehicles
- Multiple Seller Types

---

# 🤖 Machine Learning Pipeline

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Vehicle Age Calculation
      │
      ▼
Ordinal Encoding
      │
      ▼
Train-Test Split
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Model Saving
      │
      ▼
Flask Integration
      │
      ▼
Real-Time Prediction
```

---

# 📥 Model Input Features

The prediction model uses the following features:

- Brand
- Model
- Manufacturing Year
- Vehicle Age
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission Type
- Mileage
- Engine Capacity
- Maximum Power
- Seating Capacity

---

# 📤 Model Output

The application predicts

- Estimated Market Value
- Price Range
- Confidence Score
- AI Generated Market Insight

---

# 📈 Model Performance

Multiple Machine Learning algorithms were trained and evaluated before selecting the final production model.

| Model | R² Score | MAE | MSE |
|------|---------:|---------:|-------------:|
| Linear Regression | 0.676 | ₹253,053 | 197,139,466,176 |
| Decision Tree Regressor | 0.815 | ₹128,910 | 112,483,605,209 |
| Random Forest Regressor | 0.837 | ₹102,976 | 99,070,536,629 |
| **XGBoost Regressor** | **0.939** | **₹92,296** | **37,041,291,264** |

---

# 🏆 Final Model

Algorithm

**XGBoost Regressor**

Performance

- ✅ R² Score : **0.9391**
- ✅ Mean Absolute Error : **₹92,296**
- ✅ Mean Squared Error : **37.04 Billion**
- ✅ High Prediction Accuracy
- ✅ Production Ready

The XGBoost model achieved the highest prediction accuracy among all trained models and was selected for deployment in the Flask application.

---

# 📊 Evaluation Metrics

### R² Score

Measures how well the model explains the variance in car prices.

A value closer to **1** indicates a better model.

### Mean Absolute Error (MAE)

Represents the average prediction error in Indian Rupees.

Lower MAE means higher accuracy.

### Mean Squared Error (MSE)

Measures the squared prediction error.

Lower MSE indicates fewer large prediction errors.

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/palshrenik/CarValue-AI.git
```

---

## Navigate into Project

```bash
cd CarValue-AI
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Flask Application

```bash
python app.py
```

---

Visit

```
http://127.0.0.1:5000
```

---

# 🖥️ Workflow

```
User Input
      │
      ▼
Flask Backend
      │
      ▼
Feature Processing
      │
      ▼
Ordinal Encoding
      │
      ▼
XGBoost Model
      │
      ▼
Price Prediction
      │
      ▼
Interactive Dashboard
      │
      ▼
Download PDF Report
```

---

# 🚀 Future Improvements

- VIN Number Recognition
- Image-Based Damage Detection
- Deep Learning Price Prediction
- Live Market Price API
- Dealer Recommendation System
- Vehicle Comparison
- Cloud Deployment
- User Authentication
- Price Trend Visualization
- Market Analytics Dashboard
- Car Recommendation Engine

---

# 📚 Libraries Used

- Flask
- Pandas
- NumPy
- XGBoost
- Scikit-Learn
- Joblib
- Pickle
- jsPDF

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create your feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 👨‍💻 Author

## **Shrenik Pal**

**B.Tech Computer Science Engineering (AI & ML)**

Machine Learning • Artificial Intelligence • Data Science • Python • Flask • XGBoost

---

# ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

It motivates me to build more Machine Learning and AI projects.

---

## 💙 Thank You for Visiting CarValue AI!
