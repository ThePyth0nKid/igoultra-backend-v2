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
- 🔐 Auth system with JWT (`simplejwt`)

---

## 🧩 Project Structure

```bash
igo_ultra_backend_v2/
├── ultrabackend/         # Django core settings
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
- Token-based using `simplejwt`
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
git clone https://github.com/youruser/igo_ultra_backend_v2.git

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

## 🧱 Conventions

- Clean architecture: logic lives in `core/`
- ESLint 501-style: max. 80 characters per line
- English comments, even in DE-based code
- DRY: no business logic in views – always use services
- Modular & scalable for games, VR, AR

---

## 🛠️ Roadmap

- [ ] Test XP API with real data
- [ ] Connect Discord bot to API
- [ ] Integrate frontend
- [ ] Auto-detect season changes
- [ ] Make layer influence game mechanics

---

## 💡 Vision

> **iGoUltra** is more than a project – it’s a movement.  
> Real-world actions become the foundation for a digital universe  
> where your progress is visible, tangible, and playable.  
> XP, training, community. You vs. You.

**AHHU.**


# 🧠 iGoUltra Backend V2

Das `igo_ultra_backend_v2` ist das zentrale Backend des iGoUltra-Universums.  
Es verbindet **Real-Life Challenges** mit einem gamifizierten XP-System,  
das Nutzer:innen über Level, Ränge, Saisons und Schichten (Layer) hinweg  
begleitet. Ziel ist ein modulares, skalierbares Backend, das später mit  
Discord, Wearables und VR/AR-Technologien interagieren kann.

---

## 🚀 Features

- 🎮 XP-System mit Levelkurve, Aktivitäten, Einträgen & Services
- 🔗 Discord OAuth2 Login & Bot-Integration (XP via Discord)
- 📆 Season-System mit saisonalen Leaderboards
- 🌌 Reality & Cyber Layer Logik basierend auf XP/Level
- 🧱 Clean Architecture mit `core/services`, `constants`, `utils`
- 📡 REST API über Django Rest Framework
- 🔐 Auth-System mit JWT (simplejwt)

---

## 🧩 Projektstruktur

```bash
igo_ultra_backend_v2/
├── ultrabackend/         # Django Core Projekt (settings, urls)
├── users/                # CustomUser-Modell (inkl. Discord-ID)
├── xp/                   # Aktivitäten, XPEntry, UserProfile
├── seasons/              # SeasonScore, Leaderboards
├── layers/               # RealityLayerStatus & CyberLayerStatus
├── core/
│   ├── services/         # XP-, Season-, Layer-Logik
│   ├── constants/        # XP-Grenzen, Layer-Mappings
│   └── utils/            # Zeit- und Hilfsfunktionen
└── manage.py
```

---

## 🔐 Auth System

- `CustomUser` mit `discord_id`
- Login über `django-allauth` + `dj-rest-auth`
- Token-basiert über `simplejwt`
- Discord Bot vergibt XP via API

---

## 🧠 XP-System Übersicht

| Modell         | Zweck                              |
|----------------|-------------------------------------|
| `ActivityType` | Definierte Aktivitäten (z.B. Pushups) |
| `XPEntry`      | Einzelne Aktion mit XP              |
| `UserProfile`  | XP + Level pro Nutzer               |

Logik über: `core/services/xp_service.py`

---

## 📆 Seasons

- `SeasonScore`: XP-Speicherung nach Monat & Modus
- Zwei Modi: `Reality` & `Cyber`
- Leaderboards über DRF-API

---

## 🌌 Layer System

- `RealityLayerStatus` & `CyberLayerStatus`
- Layer wird aus XP/Level berechnet
- Zugang zu Events & Dungeons

---

## 🔗 Wichtige Endpoints

| Endpoint                       | Beschreibung               |
|-------------------------------|----------------------------|
| `/api/auth/discord/`          | Discord OAuth Login        |
| `/api/xp/add/`                | XP vergeben (Bot / Frontend)|
| `/api/user/profile/`          | Aktuelles XP-Level anzeigen|
| `/api/seasons/reality/`       | Reality Leaderboard        |
| `/api/seasons/cyber/`         | Cyber Leaderboard          |

---

## ✅ Setup

```bash
# 1. Repo klonen
git clone https://github.com/deinuser/igo_ultra_backend_v2.git

# 2. Virtuelle Umgebung starten
python -m venv venv
source venv/bin/activate  # oder venv\Scripts\activate

# 3. Requirements installieren
pip install -r requirements.txt

# 4. Migrationen & Superuser anlegen
python manage.py migrate
python manage.py createsuperuser

# 5. Dev Server starten
python manage.py runserver
```

---

## 🧱 Konventionen

- Clean Architecture: Logik in `core/`
- ESLint 501-konformer Stil: max. 80 Zeichen pro Zeile
- Englische Kommentare, auch im deutschen Code
- DRY: Keine Business-Logik in Views, nur über Services
- Modular & skalierbar für Games, VR, AR

---

## 🛠️ Roadmap

- [ ] XP-API mit echten Daten testen
- [ ] Discord-Bot anbinden
- [ ] Frontend integrieren
- [ ] Saisonwechsel automatisch erkennen
- [ ] Layer beeinflussen Spielmechanik

---

## 💡 Vision

> **iGoUltra** ist mehr als ein Projekt – es ist ein Movement.  
> Reale Handlungen werden zur Basis für ein digitales Universum,  
> in dem dein Fortschritt sichtbar, spürbar und spielbar wird.  
> XP, Training, Community. You vs. You.

**AHHU.**
