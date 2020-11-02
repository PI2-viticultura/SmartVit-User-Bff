from fastapi import APIRouter, Response
from controllers import notification_controller
from utils.formatters import create_response

router = APIRouter()


@router.get('/notification/{user_id}')
async def notification(response: Response, user_id: str):
    result, status = await notification_controller.get_notification(user_id)
    return create_response(result, status, response)
