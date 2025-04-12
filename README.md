# 🧠 iGoUltra Backend V2

The `igo_ultra_backend_v2` is the core backend for the iGoUltra universe.  
It connects **real-life challenges** to a gamified XP system that tracks users  
across levels, leagues, seasons, and layers (reality/cyber).  
The goal is a modular, scalable backend with future integrations for  
Discord, wearables, and VR/AR.

---

## 🚀 Features

- 🎮 XP system with level curves, activities, entries & services
- 🔗 Discord OAuth2 login & bot integration (XP via Discord)
- 📆 Season system with seasonal leaderboards
- 🌌 Reality & Cyber layer logic based on XP/level
- 🧱 Clean Architecture using `core/services`, `constants`, `utils`
- 📡 REST API powered by Django Rest Framework
- 🔐 Auth system using **session cookies** (CSRF-safe, frontend-ready)

---

## 🧩 Project Structure

```bash
igo_ultra_backend_v2/
├── ultrabackend/         # Django project (settings, urls)
├── api/
│   └── v1/               # Versioned API endpoints
├── users/                # CustomUser model (with discord_id)
├── xp/                   # Activities, XPEntry, UserProfile
├── seasons/              # SeasonScore, leaderboards
├── layers/               # Reality & Cyber Layer Status
├── core/
│   ├── services/         # XP, season, layer logic
│   ├── constants/        # XP levels, layer definitions
│   └── utils/            # Date & helper functions
└── manage.py
```

---

## 🔐 Auth System

- `CustomUser` with `discord_id`
- Login via `django-allauth` + `dj-rest-auth`
- Secure session-based auth (CSRF support)
- Discord bot sends XP via API

---

## 🧠 XP System Overview

| Model         | Purpose                                 |
|---------------|------------------------------------------|
| `ActivityType`| Defined activities (e.g. Pushups)        |
| `XPEntry`     | A single XP action entry                 |
| `UserProfile` | Stores total XP and level per user       |

Logic via: `core/services/xp_service.py`

---

## 📆 Seasons

- `SeasonScore`: stores XP per month and mode
- Two modes: `reality` and `cyber`
- Leaderboards via DRF API

---

## 🌌 Layer System

- `RealityLayerStatus` and `CyberLayerStatus`
- Layer is calculated from XP or level
- Used for event and dungeon access

---

## 🔗 Key Endpoints

| Endpoint                      | Description                 |
|------------------------------|-----------------------------|
| `/api/auth/discord/`         | Discord OAuth login         |
| `/api/xp/add/`               | Add XP via bot/frontend     |
| `/api/user/profile/`         | Get current XP & level      |
| `/api/seasons/reality/`      | Reality leaderboard         |
| `/api/seasons/cyber/`        | Cyber leaderboard           |

---

## ✅ Setup

```bash
# 1. Clone the repository
git clone https://github.com/ThePyth0nKid/igoultra-backend-v2.git
cd igoultra-backend-v2

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Migrate & create superuser
python manage.py migrate
python manage.py createsuperuser

# 5. Start dev server
python manage.py runserver
```

---

## 🌐 Deployment

- Backend domain: `https://api.igoultra.de`
- Setup CORS + CSRF for frontend domain: `https://app.igoultra.de`
- Use `Heroku PostgreSQL` addon
- Add `.env` variables in Heroku Settings > Config Vars
  - `DJANGO_SECRET_KEY`
  - `DJANGO_DEBUG=False`
  - `DATABASE_URL` (from addon)
- Set `ALLOWED_HOSTS` in `settings.py` to include both domains

---

## 📱 Mobile Compatibility

- Backend works for both web and mobile apps
- Use same API base (`api.igoultra.de`) in native apps
- Future-proof with JWT fallback if needed

---

## 🧱 Conventions

- Clean architecture: logic lives in `core/`
- English comments
- DRY: business logic in services
- Versioned API: all under `/api/v1/`

---

## 💡 Vision

> **iGoUltra** is more than a project – it’s a movement.  
> Real-world actions become the foundation for a digital universe  
> where your progress is visible, tangible, and playable.  
> XP, training, community. You vs. You.

**AHHU.**