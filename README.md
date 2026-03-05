# Slack AI Data Bot

Natural language to SQL query bot for Slack using LangChain and FastAPI.

## Architecture

```
Slack User
   │
   │  /ask-data "show revenue by region"
   ▼
Slack App (Slash Command)
   │
   ▼
FastAPI Backend
   │
   ├── LangChain NL → SQL
   │
   ├── Execute SQL (Postgres)
   │
   └── Format result
   │
   ▼
Slack Response
```

## Tech Stack

- **Backend**: FastAPI
- **AI Layer**: LangChain
- **LLM**: OpenAI GPT-4o-mini
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Database Setup

```bash
# Create database
psql -U postgres -c "CREATE DATABASE analytics;"

# Run seed script
psql -U postgres -d analytics -f scripts/seed.sql
```

### 3. Environment Variables

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

### 4. Run Server

```bash
uvicorn app.main:app --reload --port 8000
```

### 5. Expose with ngrok

```bash
ngrok http 8000
```

### 6. Configure Slack App

1. Go to [Slack API](https://api.slack.com/apps)
2. Create new app → From scratch
3. Add Slash Command:
   - Command: `/ask-data`
   - Request URL: `https://your-ngrok-url/ask-data`
4. Install app to workspace

## Example Queries

```
/ask-data show revenue by region
/ask-data total orders on 2025-09-01
/ask-data revenue by category
/ask-data top 3 regions by revenue
/ask-data average revenue per order
```

## Project Structure

```
slack-ai-data-bot/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI server
│   ├── config.py            # Environment config
│   ├── database.py          # PostgreSQL connection
│   ├── slack_handler.py     # Slack endpoint
│   ├── langchain_sql.py     # NL → SQL conversion
│
├── scripts/
│   └── seed.sql             # Database setup
│
├── requirements.txt
├── .env.example
└── README.md
```

## Features

✅ Natural language to SQL conversion  
✅ PostgreSQL query execution  
✅ Formatted table results in Slack  
✅ Error handling  
✅ Production-ready structure  

## Stretch Goals (Optional)

- [ ] CSV export button
- [ ] Chart visualization for time-series
- [ ] Redis caching for repeated queries
- [ ] Query history logging
