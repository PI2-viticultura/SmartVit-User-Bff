from fastapi import APIRouter, Response
from controllers import bff_controller
from utils.formatters import create_response

router = APIRouter()


@router.post('/support/')
async def support(response: Response):
    result, status = await bff_controller.get_git()
    return create_response(result, status, response)
