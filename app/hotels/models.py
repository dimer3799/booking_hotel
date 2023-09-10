from app.database import Base


class Hotels(Base):
    __tablename__ = "hotels"

    id = ""
    name = ""
    location = ""
    services = ""
    rooms_quantity = ""
    image_id = ""
