from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        result = []
        query = """select DISTINCT  t.year
                    from teams t
                    where t.year>1979
                    order by `year` desc """
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllTeam(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        result = []
        query = """select *
                from teams t
                where t.`year` = %s """
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Team(**row))
        cursor.close()
        conn.close()
        return result