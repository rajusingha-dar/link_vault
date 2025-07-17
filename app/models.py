from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLAlchemyEnum, Index
from sqlalchemy.sql import func
import enum
from .database import Base

# Define an Enum for the different types of links
# UPDATED: Simplified the Enum so the member name and value are the same.
# This makes data transfer between the frontend and backend unambiguous
# and resolves the validation error permanently.
class LinkType(str, enum.Enum):
    youtube = "youtube"
    github = "github"
    web_page = "web_page"
    pdf = "pdf"
    social_media = "social_media"

class Link(Base):
    """
    SQLAlchemy ORM model for a saved link.
    This class maps to the 'links' table in the database.
    """
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    
    url = Column(String(2048), nullable=False)
    
    title = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    
    link_type = Column(SQLAlchemyEnum(LinkType), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        Index('ix_links_url', 'url', mysql_length=255),
    )

    def __repr__(self):
        return f"<Link(id={self.id}, title='{self.title}', type='{self.link_type}')>"
