from pydantic import BaseModel, ConfigDict, HttpUrl
from datetime import datetime
from .models import LinkType # Import the Enum from our models

# --- Base Schema ---
# Contains common attributes for a link
class LinkBase(BaseModel):
    url: HttpUrl # Pydantic will validate that this is a valid URL
    title: str
    description: str | None = None # Optional description
    link_type: LinkType

# --- Schema for Creation ---
# This is the data we expect from the user when they create a new link.
class LinkCreate(LinkBase):
    pass

# --- Schema for Reading/Returning ---
# This is the data we will send back to the user from the API.
# It includes the database-generated fields like id and timestamps.
class Link(LinkBase):
    id: int
    created_at: datetime
    updated_at: datetime

    # Configure Pydantic to work with ORM models
    model_config = ConfigDict(from_attributes=True)
