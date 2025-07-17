from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import HttpUrl
from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from . import crud, models, schemas
from .database import engine, get_db
from .models import LinkType

# Create all database tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Link Saver App")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# --- HTML Endpoints ---

@app.get("/", response_class=HTMLResponse)
def root(request: Request, filter_by: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Renders the main page. If a 'filter_by' query parameter is provided,
    it shows links of that type. Otherwise, it shows all links.
    """
    try:
        links = []
        active_filter = "All" # Default active filter

        # UPDATED: Explicitly check if the filter_by string is a valid LinkType
        if filter_by and filter_by in LinkType._value2member_map_:
            link_type_enum = LinkType(filter_by) # Convert string to Enum member
            links = crud.get_links_by_type(db, link_type=link_type_enum)
            active_filter = filter_by # Set the active filter for the UI
        else:
            # If no filter or an invalid filter is provided, get all links
            links = crud.get_links(db)
        
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "links": links, 
            "link_types": LinkType,
            "active_filter": active_filter
        })
    except SQLAlchemyError as e:
        return templates.TemplateResponse("index.html", {"request": request, "links": [], "error": f"Database error: {e}"})

@app.post("/add", response_class=RedirectResponse)
def add_link(
    request: Request,
    title: str = Form(...),
    url: HttpUrl = Form(...),
    description: str = Form(None),
    link_type: LinkType = Form(...),
    db: Session = Depends(get_db)
):
    """Handles the form submission to create a new link."""
    try:
        link_schema = schemas.LinkCreate(title=title, url=url, description=description, link_type=link_type)
        crud.create_link(db=db, link=link_schema)
        return RedirectResponse(url="/", status_code=303)
    except SQLAlchemyError:
        return RedirectResponse(url="/?error=true", status_code=303)

@app.get("/delete/{link_id}", response_class=RedirectResponse)
def delete_link(link_id: int, db: Session = Depends(get_db)):
    """Deletes a link and redirects back to the main page."""
    try:
        crud.delete_link(db, link_id)
        return RedirectResponse(url="/", status_code=303)
    except SQLAlchemyError:
        return RedirectResponse(url="/?error=true", status_code=303)
