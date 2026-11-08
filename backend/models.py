from datetime import datetime, timezone 

from sqlalchemy import(
    String,
    Integer,
    Float,
    Boolean,
    Text,
    JSON,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    CheckConstraint
)

from sqlalchemy.orm import Mapped, mapped_column, relationship


from database import Base

class Series(Base):
    __tablename__ = "series"

    id: Mapped[str] = mapped_column(
        String(100), primary_key=True
    )

    title: Mapped[str] = mapped_column(
        String(200), nullable = False
    )

    description: Mapped[str] = mapped_column(Text)

    genre: Mapped[str] = mapped_column(String(100))

    topic: Mapped[str] = mapped_column(String(100))

    cover: Mapped[dict] = mapped_column(JSON)

    status: Mapped[str] = mapped_column(
        String(30), default= "in_development"
    )

    episodes: Mapped[list["Episode"]]= relationship(
        back_populates = "series",
        cascade = "all, delete-orphan",
        order_by = "Episode.episode_number"
    )

#PAPERS TABLE

class Paper(Base):
    __tablename__ = "papers"

    id: Mapped[str] = mapped_column(
        String(100), primary_key = True
    )

    title: Mapped[str] = mapped_column(
        String(500), nullable = False
    )

    authors: Mapped[list]= mapped_column(
        JSON, nullable=False
    )

    year: Mapped[int]= mapped_column(
        Integer, nullable=False)

    venue: Mapped[str]= mapped_column(
        String(200))

    source: Mapped[dict]= mapped_column(
        JSON, nullable=False)

    research: Mapped[dict]= mapped_column(
        JSON, nullable=False)

    episodes: Mapped[list["Episode"]]= relationship(
        back_populates="paper"
    )

# EPISODES TABLE

class Episode(Base):
    __tablename__ = "episodes"

    __table_args__=(
        UniqueConstraint(
            "series_id",
            "episode_number",
            name= "uq_series_episode_number"
        ),
        CheckConstraint(
            "episode_number>=1",
            name = "ck_episode_number"
        ),
    )

    id:Mapped[str] = mapped_column(
        String(100), primary_key = True
    )

    paper_id: Mapped[str] = mapped_column(
        ForeignKey("papers.id", ondelete = "RESTRICT"),
        nullable = False
    )

    series_id: Mapped[str] = mapped_column(
        ForeignKey("series.id", ondelete="CASCADE"),
        nullable=False
    )

    episode_number: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    
    next_episode_id: Mapped[str | None] = mapped_column(
        ForeignKey("episodes.id"),
        nullable=True
    )


    presentation: Mapped[dict] = mapped_column(
        JSON, nullable=False
    )

    publication_status: Mapped[str] = mapped_column(
    String(30),
    default="draft"
    )

    story: Mapped[dict] = mapped_column(
        JSON, nullable=False
    )

    science_card: Mapped[str] = mapped_column(
        JSON, nullable=False
    )

    series: Mapped["Series"] = relationship(
        back_populates="episodes"
    )

    paper : Mapped["Paper"] = relationship(
        back_populates="episodes"
    )


# Reading progress table

class ReadingProgress(Base):
    __tablename__ = "reading_progress"

    __table_args__= (
        UniqueConstraint(
            "session_id",
            "episode_id",
            name = "uq_session_episode"
        ),
            CheckConstraint(
                "progress_percent >= 0 AND progress_percent <=100",
                name = "ck_progress_percent"
            ),

    )

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )

    session_id: Mapped[str] = mapped_column(
        String(100), index=True, nullable=False
    )

    episode_id: Mapped[str] = mapped_column(
        ForeignKey("episodes.id", ondelete = "CASCADE"), nullable=False
    )

    progress_percent: Mapped[float] = mapped_column(
        Float, default=0.0
    )

    completed: Mapped[bool] = mapped_column(
        Boolean, default=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )