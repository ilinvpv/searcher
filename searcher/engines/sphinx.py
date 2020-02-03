from pymysqlpool import ConnectionPool


class SphinxEngine:
    def __init__(self, host='localhost', port=9306, user='', password='',
                 database='', pool_name=None):
        self.__pool = ConnectionPool(host=host, port=port, user=user,
                                     password=password, database=database,
                                     pool_name=pool_name)
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._database = database
        self._pool_name = pool_name

    def __execute(self, raw_query):
        with self.__pool.cursor() as cursor:
            return cursor.execute(raw_query)

    @property
    def is_ready(self):
        return self.__execute('SELECT 1')

    @property
    def all_indices(self):
        res = self.__execute('SHOW TABLES')
        return [row['Index'] for row in res]

    @property
    def meta(self):
        res = self.__execute('SHOW META')
        return {row['Variable_name']: row['Value'] for row in res}

    def get_index_meta(self, index_name):
        res = self.__execute('SHOW INDEX {} STATUS'.format(index_name))
        return {row['Variable_name']: row['Value'] for row in res}
