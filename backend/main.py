from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import select, text
from sqlalchemy.orm import Session, selectinload, joinedload

from database import get_db
from models import Series, Episode

from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title = "Paperflix API",
    description = "Research discovery through storytelling",
    version="0.1.0"
)

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials = False
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = False,
    allow_methods = ["*"],
    allow_headers = ["*"],

)

def episode_card(episode):

    presentation = episode.presentation or {}

    return {
        "id": episode.id,
        "episode_number": episode.episode_number,
        "title":presentation.get("title"),
        "tagline": presentation.get("tagline"),
        "genre": presentation.get("genre"),
        "difficulty": presentation.get("difficulty"),
        "estimated_minutes":presentation.get("estimated_minutes"),
        "thumbnail":presentation.get("thumbnail"),
        "publication_status": episode.publication_status
    }
def episode_details(episode):

    paper = episode.paper
    series = episode.series

    return {
        "id": episode.id,
        "episode_number": episode.episode_number,

        "series": {
            "id":series.id,
            "title":series.title
        },

        "paper": {
            "id": paper.id,
            "title": paper.title,
            "authors": paper.authors,
            "year": paper.year,
            "venue":paper.venue,
            "source": paper.source,
            "research": paper.research
        },

        "presentation": episode.presentation,
        "story": episode.story,
        "science_card": episode.science_card,

        "navigation": {
            "next_episode_id":episode.next_episode_id
        },

        "publication_status": episode.publication_status
    }


#HEALTH CHECK

@app.get("/", include_in_schema=False)
def home():
    return FileResponse(FRONTEND_DIR / "index.html")

@app.get("/api/health")
def health_check(db: Session = Depends(get_db)):

    db.execute(text("SELECT 1"))

    return{
        "status": "healthy",
        "database":"connected"
    }

#SERIES
@app.get("/api/series")
def get_series(db: Session = Depends(get_db)):

    statement = (
        select(Series)
        .options(selectinload(Series.episodes))
        .order_by(Series.title)
    )

    series_list = db.scalars(statement).all()

    return  {
        "total": len(series_list),
        "series": [
            {
                "id": item.id,
                "title":item.title,
                "description": item.description,
                "genre": item.genre,
                "topic": item.topic,
                "cover":item.cover,
                "status": item.status,
                "episode_count": len(item.episodes)
            }

            for item in series_list
        ]
    }

@app.get("/api/series/{series_id}")
def get_series_details(
    series_id:str,
    db: Session = Depends(get_db)
):

    statement= (
        select(Series)
        .options(selectinload(Series.episodes))
        .where(Series.id == series_id)
    )

    series = db.scalar(statement)

    if not series:
        raise HTTPException(
            status_code= 404,
            detail = "Series not found"
        )

    return {
        "id": series.id,
        "title": series.title,
        "description": series.description,
        "genre": series.genre,
        "topic": series.topic,
        "cover": series.cover,
        "episodes": [
            episode_card(ep)
            for ep in series.episodes
        ]
    }

#EPISODE
@app.get("/api/episodes/{episode_id}")
def get_episode(
    episode_id: str,
    db: Session = Depends(get_db)
):

    statement = (
        select(Episode)
        .options(
            joinedload(Episode.paper),
            joinedload(Episode.series)
        )
        .where(Episode.id == episode_id)
    )

    episode = db.scalar(statement)

    if not episode:
        raise HTTPException(
                    status_code= 404,
                    detail = "Episode not found"
                )
    return episode_details(episode)

#NEXT EPISODE

@app.get("/api/episodes/{episode_id}/next")
def get_next_episode(
    episode_id: str,
    db: Session = Depends(get_db)
):
    current_episode = db.get(Episode, episode_id)

    if not current_episode:
        raise HTTPException(
                    status_code= 404,
                    detail = "Episode not found"
                )

    next_id = current_episode.next_episode_id

    if not next_id:
        return{
            "has_next": False,
            "message": "You have reached the end of the series!"
        }

    statement = (
        select(Episode)
        .options(
            joinedload(Episode.paper),
            joinedload(Episode.series)
        )
        .where(Episode.id == next_id)
    )

    next_episode = db.scalar(statement)

    if not next_episode:
        raise HTTPException(
                    status_code= 404,
                    detail = "Next episode could not be found"
                )
    return {
        "has_next": True,
        "episode" : episode_details(next_episode)
    }