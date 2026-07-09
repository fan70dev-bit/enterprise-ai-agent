from datetime import datetime


def serialize(data):

    if isinstance(data, list):
        return [serialize(item) for item in data]

    if hasattr(data, "__table__"):

        result = {}

        for column in data.__table__.columns:

            value = getattr(data, column.name)

            if isinstance(value, datetime):
                value = value.isoformat()

            result[column.name] = value

        return result

    return data