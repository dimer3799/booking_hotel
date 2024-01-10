from fastapi import APIRouter

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.get("/")
def get_bookings():
    pass


@router.get("/")
def get_bookings():
    pass
