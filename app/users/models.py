from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    bookings = relationship("Bookings", back_populates="user")

    def __str__(self):
        return f"Пользователь {self.email}"
