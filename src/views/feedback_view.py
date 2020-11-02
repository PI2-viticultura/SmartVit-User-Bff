from fastapi import APIRouter, Response
from controllers import feedback_controller
from utils.formatters import create_response
from pydantic import BaseModel

router = APIRouter()


class Feedback(BaseModel):
    title: str
    message_body: str


@router.post('/feedback/')
async def feedback(response: Response, feedback: Feedback):
    result, status = await feedback_controller.post_feedback(feedback.dict())
    return create_response(result, status, response)
