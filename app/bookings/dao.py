"""DAO/Сервис/Репозиторий  для работы с бронированием"""

from app.bookings.models import Bookings
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    """Класс реализующий основные методы для работы с бронированием"""

    model = Bookings
