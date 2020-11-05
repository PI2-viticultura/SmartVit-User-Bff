from fastapi import APIRouter, Response
from controllers import pest_controller
from utils.formatters import create_response
from pydantic import BaseModel

router = APIRouter()


class Pest(BaseModel):
    idVineyard: str
    type: str
    startTime: str
    endTime: str
    action: str
    observation: str
    # description: Optional[str] = None


@router.post('/pest/')
async def pest(response: Response, pest: Pest):
    result, status = await pest_controller.post_pest(pest.dict())
    return create_response(result, status, response)
