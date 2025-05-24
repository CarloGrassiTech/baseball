from fastapi.openapi.utils import status_code_ranges

from database.DAO import DAO


class Model:
    @staticmethod
    def getAllYears():
        return DAO.getAllYears()