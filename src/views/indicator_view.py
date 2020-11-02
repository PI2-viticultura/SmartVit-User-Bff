from fastapi import APIRouter, Response
from controllers import indicator_controller
from utils.formatters import create_response

router = APIRouter()


@router.get('/indicators/{winery_id}')
async def indicator(response: Response, winery_id: str):
    result, status = await indicator_controller.retrieve_indicator(winery_id)
    return create_response(result, status, response)
