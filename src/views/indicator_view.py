from fastapi import APIRouter, Response
from controllers import indicator_controller
from utils.formatters import create_response
from pydantic import BaseModel

router = APIRouter()


class Indicator(BaseModel):
    title: str
    message_body: str


@router.post('/indicator/')
async def indicator(response: Response, indicator: Indicator):
    result, status = await indicator_controller.post_indicator(indicator.dict())
    return create_response(result, status, response)
