from pydantic import BaseModel

class ColourState(BaseModel):
    favourite_color: str = "Blue"
    least_favourite_color: str = "Brown"