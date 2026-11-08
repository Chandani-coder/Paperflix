from database import Base, engine, SessionLocal

from models import Series, Paper, Episode

from data import PAPERS, EPISODES, SERIES

def initialize_database():

    Base.metadata.create_all(bind = engine)
    print("Database table initialized.")


def seed_papers(db):
    for paper_id, paper_data in PAPERS.items():

        if db.get(Paper, paper_id):
            continue

        paper = Paper(
            id=paper_id,
            title=paper_data["title"],
            authors=paper_data["authors"],
            year=paper_data["year"],
            venue=paper_data["venue"],
            source=paper_data["source"],
            research=paper_data["research"]
        )

        db.add(paper)

    db.flush()
    print(f"Processed {len(PAPERS)} research papers.")

def seed_series(db):
    for series_id, series_data in SERIES.items():

        if db.get(Series, series_id):
            continue

        series= Series(
            id=series_id,
            title=series_data["title"],
            description=series_data["description"],
            genre=series_data["genre"],
            topic=series_data["topic"],
            cover=series_data["cover"],
            status=series_data["status"]
        )

        db.add(series)

    db.flush()
    print(f"Processes {len(SERIES)} series.")


def seed_episodes(db):
    for episode_id, episode_data in EPISODES.items():

        if db.get(Episode, episode_id):
            continue

        episode= Episode(
            id=episode_id,
            paper_id=episode_data["paper_id"],
            series_id=episode_data["series_id"],
            episode_number=episode_data["episode_number"],
            presentation=episode_data["presentation"],
            story=episode_data["story"],
            science_card=episode_data["science_card"],
            next_episode_id=episode_data["navigation"]["next_episode_id"],
            publication_status=episode_data["publication_status"]
        )

        db.add(episode)

    db.flush()
    print(f"Processed {len(EPISODES)} episodes.")

def seed_database():
    initialize_database()

    with SessionLocal() as db:
        try:
            seed_papers(db)
            seed_series(db)
            seed_episodes(db)

            db.commit()
            print("\nPaperrflix database seeded successfully!")

        except Exception:
            db.rollback()
            raise

if __name__ == "__main__":
    seed_database()