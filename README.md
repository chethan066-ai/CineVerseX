# CineVerseX

CineVerseX is a Flask movie discovery and cinema management web application. It combines a local movie database, IMDb-style detail pages, upcoming releases, theater listings, admin tools, reports, Google login, wishlist, and external booking links.

## Features

- Google login and direct email/password login
- Admin and user roles
- Movie discovery with posters, ratings, genres, runtime, and descriptions
- IMDb dataset movie detail pages
- Trailer discovery links
- JustWatch links for movie availability
- BookMyShow redirect links for upcoming/releasing movies
- Wishlist and recently viewed movies
- Upcoming releases page
- Theater directory with filters and pagination
- Admin dashboard with platform metrics
- Reports module for CSV exports
- Revenue and analytics views
- Activity logging
- REST API endpoints for movies, theaters, shows, upcoming, and trending data
- White and dark themes

## Tech Stack

- Python
- Flask
- SQLite
- SQLAlchemy
- HTML
- CSS
- Bootstrap
- JavaScript

## Project Structure

```text
CineVerseX/
+-- backend/
|   +-- app.py
|   +-- routes/
|   +-- services/
|   +-- models/
|   +-- templates/
|   +-- static/
|   +-- data/
+-- scripts/
+-- requirements.txt
+-- README.md
```

## How to Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python backend\app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Environment Variables

For local development, create a `.env` file in the project root.

```env
SECRET_KEY=change-this-secret
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=http://127.0.0.1:5000/auth/google/callback
```

Optional catalog sync settings:

```env
ENABLE_STARTUP_CATALOG_SYNC=false
ENABLE_DAILY_CATALOG_SYNC=false
```

Keep these disabled on free Render deployments unless you specifically want startup or daily external sync work.

## Database Notes

Large local database files are ignored by Git. The repository includes only the smaller seed data needed for deployment.

Ignored generated/runtime paths include:

- `*.db`
- `backend/instance/`
- `instance/`
- `backend/static/tickets/`
- `backend/static/qrcodes/`
- `backend/static/posters/`

## Render Notes

Set these in Render Environment settings:

```env
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=https://your-render-app.onrender.com/auth/google/callback
```

Also add the same Render callback URL in Google Cloud Console under Authorized redirect URIs.
