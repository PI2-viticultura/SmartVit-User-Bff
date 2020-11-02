from fastapi import APIRouter, Response
from controllers import notification_controller
from utils.formatters import create_response
from pydantic import BaseModel

router = APIRouter()


class Notification(BaseModel):
    title: str
    message_body: str


@router.get('/notification/')
async def notification(response: Response, notification: Notification):
    result, status = await notification_controller.post_notification(notification.dict())
    return create_response(result, status, response)
