from fastapi import APIRouter

router = APIRouter(prefix="/bookings", tags=["Bookings"])
from sqlalchemy import select

from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings
from app.database import async_session_maker


@router.get("/{booking_id}")
async def get_booking():
    async with async_session_maker() as session:
        query = select(Bookings)
        result = await session.execute(query)
        print(result)


@router.get("")
async def get_bookings():
    result = await BookingDAO.find_all()
    return result
