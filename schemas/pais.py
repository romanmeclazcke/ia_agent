from pydantic import BaseModel

class PaisInformation(BaseModel):
    spanish_name:str
    english_name:str
    economy:str
    number_of_inhabitants: int