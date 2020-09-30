from fastapi import APIRouter, Response, Request
from controllers import support_controller
from utils.formatters import create_response
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


class Support(BaseModel):
    title: str
    message_body: str
    description: str
    # description: Optional[str] = None


@router.post('/support/')
async def support(response: Response, support: Support):
    result, status = await support_controller.post_support(support.dict())
    return create_response(result, status, response)
