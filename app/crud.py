from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from . import models, schemas

def get_link(db: Session, link_id: int):
    """Fetches a single link by its ID."""
    return db.query(models.Link).filter(models.Link.id == link_id).first()

def get_links(db: Session, skip: int = 0, limit: int = 100):
    """Fetches a list of all links, ordered by creation date."""
    return db.query(models.Link).order_by(models.Link.created_at.desc()).offset(skip).limit(limit).all()

def get_links_by_type(db: Session, link_type: models.LinkType, skip: int = 0, limit: int = 100):
    """Fetches a list of links filtered by a specific type."""
    return db.query(models.Link).filter(models.Link.link_type == link_type).order_by(models.Link.created_at.desc()).offset(skip).limit(limit).all()

def create_link(db: Session, link: schemas.LinkCreate):
    """Creates a new link in the database."""
    try:
        db_link = models.Link(
            url=str(link.url),
            title=link.title,
            description=link.description,
            link_type=link.link_type
        )
        db.add(db_link)
        db.commit()
        db.refresh(db_link)
        return db_link
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def update_link(db: Session, link_id: int, link_data: schemas.LinkCreate):
    """Updates an existing link."""
    db_link = get_link(db, link_id)
    if db_link:
        try:
            update_data = link_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                if key == 'url':
                    setattr(db_link, key, str(value))
                else:
                    setattr(db_link, key, value)
            db.commit()
            db.refresh(db_link)
            return db_link
        except SQLAlchemyError as e:
            db.rollback()
            raise e
    return None

def delete_link(db: Session, link_id: int):
    """Deletes a link from the database."""
    db_link = get_link(db, link_id)
    if db_link:
        try:
            db.delete(db_link)
            db.commit()
            return db_link
        except SQLAlchemyError as e:
            db.rollback()
            raise e
    return None
