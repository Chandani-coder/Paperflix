from database import Base, engine, SessionLocal

from models import Series, Paper, Episode

from data import PAPERS, EPISODES, SERIES

def initialize_database():

    Base.metadata.create_all(bind = engine)
    print("Database table initialized.")


def seed_papers(db):
    for paper_id, paper_data in PAPERS.items():

        paper = db.get(Paper, paper_id)

        if paper is None:
            paper = Paper(id=paper_id)
            db.add(paper)

        paper.title = paper_data["title"]
        paper.authors = paper_data["authors"]
        paper.year = paper_data["year"]
        paper.venue = paper_data["venue"]
        paper.source = paper_data["source"]
        paper.research = paper_data["research"]

    db.flush()
    print(f"Processed {len(PAPERS)} research papers.")

def seed_series(db):
    for series_id, series_data in SERIES.items():

        series = db.get(Series, series_id)

        if series is None:
            series = Series(id=series_id)
            db.add(series)

        series.title = series_data["title"]
        series.description = series_data["description"]
        series.genre = series_data["genre"]
        series.topic = series_data["topic"]
        series.cover = series_data["cover"]
        series.status = series_data["status"]

    db.flush()
    print(f"Processes {len(SERIES)} series.")



def seed_episodes(db):

    for episode_id, episode_data in EPISODES.items():

        episode = db.get(Episode, episode_id)

        if episode:
            # Update existing episode
            episode.paper_id = episode_data["paper_id"]
            episode.series_id = episode_data["series_id"]
            episode.episode_number = episode_data["episode_number"]
            episode.presentation = episode_data["presentation"]
            episode.story = episode_data["story"]
            episode.science_card = episode_data["science_card"]
            episode.next_episode_id = (
                episode_data["navigation"]["next_episode_id"]
            )
            episode.publication_status = (
                episode_data["publication_status"]
            )

        else:
            # Insert new episode
            episode = Episode(
                id=episode_id,
                paper_id=episode_data["paper_id"],
                series_id=episode_data["series_id"],
                episode_number=episode_data["episode_number"],
                presentation=episode_data["presentation"],
                story=episode_data["story"],
                science_card=episode_data["science_card"],
                next_episode_id=(
                    episode_data["navigation"]["next_episode_id"]
                ),
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
            print("\nPaperflix database seeded successfully!")

        except Exception:
            db.rollback()
            raise

if __name__ == "__main__":
    seed_database()