# routes.py

from fastapi import APIRouter, HTTPException

from app.models.transform import TransformRequest

router = APIRouter()


@router.post("/transform")
async def transform_code(req: TransformRequest):
    """
    Transform the code using the selected transformer.
    """
    try:
        return await {"code": req.code, "transformer": req.transformer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))