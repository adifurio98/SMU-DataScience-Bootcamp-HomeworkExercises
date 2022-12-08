from sqlalchemy import create_engine
import pandas as pd

class SQLHelper():
    
    def __init__(self):
        self.database_path = "Resources/hawaii.sqlite"
        self.connection_str = f"sqlite:///{self.database_path}"
        self.engine = create_engine(self.connection_str)

    def executeQuery(self, query):
        df = pd.read_sql(query, self.engine)
        return(df)
    
    def getprcp(self):
        query = """SELECT
                        date,
                        prcp
                    FROM
                        measurement
                    WHERE
                        date >= '2016-08-23'
                    ORDER BY 
                        date asc
                """
        return(self.executeQuery(query))

    def getstation(self):
        query = """SELECT
                        *
                    FROM
                        station
                    ORDER BY 
                        station desc
                """
        return(self.executeQuery(query))
    
    def gettobs(self):
        query = """
                    SELECT
                        date,
                        tobs
                    FROM
                        measurement
                    WHERE
                        date >= '2016-08-23' AND
                        station = 'USC00519281' 
                    ORDER BY 
                        date asc
                """
        return(self.executeQuery(query))
    
    def getstart(self, start):
        query = """
                    SELECT 
                        max(tobs) as maxTobs,
                        min(tobs) as minTobs,
                        avg(tobs) as avgTobs
                    FROM 
                        measurement
                    WHERE
                        date >= '{start}'
                """
        return(self.executeQuery(query))
    
    def getend(self, start, end):
        query = f"""SELECT
                        max(tobs) as maxTobs,
                        min(tobs) as minTobs,
                        avg(tobs) as avgTobs
                    FROM
                        measurement
                    WHERE
                        date >= '{start}' AND
                        date <= '{end}'
                """
        return(self.executeQuery(query))
    