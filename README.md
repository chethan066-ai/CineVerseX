# 🎬 CineVerseX

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap)
![TMDB](https://img.shields.io/badge/TMDB-API-green?style=for-the-badge)
![Google OAuth](https://img.shields.io/badge/Google-OAuth-red?style=for-the-badge&logo=google)

### 🚀 Modern Movie Ticket Booking & Entertainment Platform

**Live Demo:** https://cineversex.onrender.com

</div>

---

## 📖 Overview

CineVerseX is a full-stack Flask web application that combines movie discovery, ticket booking, personalized recommendations, wishlist management, theater browsing, and an admin management system into one platform.

Designed as a professional portfolio project, it demonstrates authentication, database management, REST architecture, API integration, responsive UI, and deployment.

---

# ✨ Features

## 👤 User Features

- Secure User Registration
- Login & Logout
- Google OAuth Login
- Browse Trending Movies
- Search Movies
- View Movie Details
- Movie Posters & Backdrops
- Upcoming Movies
- Movie Ratings
- Theater Listings
- Add to Wishlist
- Remove Wishlist
- Responsive UI
- Light/Dark Theme
- Mobile Friendly

---

## 🎟 Ticket Booking

- Browse Available Shows
- Select Theater
- Seat Selection
- Booking Confirmation
- Booking History

---

## 🎬 Movie Information

- TMDB Integration
- Popular Movies
- Upcoming Releases
- Movie Posters
- Genres
- Runtime
- Release Date
- Cast Information
- Movie Description
- Ratings

---

## 🛠 Admin Dashboard

- Dashboard Analytics
- Add Movies
- Edit Movies
- Delete Movies
- Manage Theaters
- Manage Shows
- Manage Users
- Export CSV Reports
- Database Management

---

# 🏗 Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Flask |
| Language | Python |
| ORM | SQLAlchemy |
| Database | SQLite |
| Authentication | Google OAuth |
| Frontend | HTML5 |
| Styling | CSS3 |
| UI Framework | Bootstrap 5 |
| JavaScript | Vanilla JavaScript |
| Movie API | TMDB API |
| Deployment | Render |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
CineVerseX
│
├── backend
│   ├── app.py
│   ├── config.py
│   ├── models
│   ├── routes
│   ├── services
│   ├── templates
│   ├── static
│   ├── database
│   └── utils
│
├── artifacts
├── scripts
├── requirements.txt
├── README.md
└── vercel.json
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/chevior/CineVerseX.git

cd CineVerseX
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```
SECRET_KEY=your_secret_key

GOOGLE_CLIENT_ID=your_google_client_id

GOOGLE_CLIENT_SECRET=your_google_client_secret

GOOGLE_REDIRECT_URI=http://127.0.0.1:5000/auth/google/callback

TMDB_API_KEY=your_tmdb_api_key
```

---

## Run Application

```bash
python backend/app.py
```

Visit

```
http://127.0.0.1:5000
```

---

# 🌍 Deployment

The project is deployed on Render.

```
https://cineversex.onrender.com
```

For deployment:

- Add Environment Variables
- Configure Google OAuth Redirect URI
- Deploy from GitHub
- Start Command

```
python backend/app.py
```

---

# 📸 Screenshots

> Add screenshots here

- Home Page
- Login
- Google Login
- Movie Details
- Search
- Wishlist
- Admin Dashboard
- Booking Page
- Reports

---

# 🔐 Authentication

- Email Authentication
- Password Hashing
- Google OAuth
- Secure Sessions

---

# 📊 Reports

- CSV Export
- User Reports
- Movie Reports
- Theater Reports

---

# 🎯 Future Improvements

- Payment Gateway
- QR Code Tickets
- Email Notifications
- SMS Notifications
- AI Movie Recommendations
- Seat Heatmaps
- Reviews & Ratings
- Multi-language Support
- Progressive Web App
- Mobile App

---

# 👨‍💻 Developer

**Chethan N**

GitHub

https://github.com/chevior

---

# ⭐ Support

If you like this project,

⭐ Star the repository.

🍴 Fork the repository.

💡 Open Issues for suggestions.

---

# 📜 License

This project is developed for educational and portfolio purposes.
