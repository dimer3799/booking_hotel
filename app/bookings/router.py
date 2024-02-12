from fastapi import APIRouter, Depends

from app.users.models import Users

router = APIRouter(prefix="/bookings", tags=["Бронирование"])

from app.bookings.dao import BookingDAO
from app.bookings.scemas import SBooking
from app.users.dependencies import get_current_user

# @router.get("/{booking_id}")
# async def get_booking():
#     async with async_session_maker() as session:
#         query = select(Bookings)
#         result = await session.execute(query)
#         print(result)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)
