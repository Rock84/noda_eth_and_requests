from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

wallet = "0xdc3EC8947438F7A834C3F38ce98B2243089CF7e6"

class Balance(BaseModel):
    "jsonrcp": float
    "id": int
    "method": str
    "params": List[str]



if __name__ == '__main__':

