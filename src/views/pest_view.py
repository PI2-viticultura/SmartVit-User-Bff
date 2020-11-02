from fastapi import APIRouter, Response
from controllers import pest_controller
from utils.formatters import create_response
from pydantic import BaseModel

router = APIRouter()


class Pest(BaseModel):
    priority: str
    problem: str
    description: str
    # description: Optional[str] = None


@router.post('/pest/')
async def pest(response: Response, pest: Pest):
    result, status = await pest_controller.post_pest(pest.dict())
    return create_response(result, status, response)
