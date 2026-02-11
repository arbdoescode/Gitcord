# GitCord

GitCord is an open-source Discord bot built with **Python** and **FastAPI** that connects GitHub events to Discord using webhooks.

---

## 🚀 Features

- GitHub → Discord webhook integration  
- FastAPI-based lightweight backend  
- Easy deployment on any web service  
- Environment-based configuration  

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/gitcord.git
cd gitcord
```

### 2️⃣ Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### ⚙️ Environment Configuration
## Copy the example environment file:
```
cp .env.example .env
```
Open `.env` and configure the required variables.

Follow the instructions inside `.env.example` to:

- Add your **Discord Bot Token**
- Add your **Discord Webhook URL**
- Configure your **GitHub Webhook Secret**
- Define separated users or role mappings (if applicable)

⚠️ Make sure all required variables are properly filled before running the application.

---

## ▶️ Running Locally

Start the FastAPI server:

```bash
uvicorn main:app --reload
```
By default, the app runs at:

`http://127.0.0.1:8000`

---

## 🌍 Deploying to a Web Service

You can deploy GitCord to any platform that supports Python and FastAPI, such as:

- Render
- Railway
- Fly.io
- Heroku
- DigitalOcean
- AWS / GCP / Azure

### Deployment Steps

1. Push your code to GitHub  
2. Create a new Web Service on your hosting platform  
3. Set the **Start Command** to:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
