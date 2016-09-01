import logging
import MySQLdb
import env
import time


class SQLSelectHandler(logging.Handler):

    """Logging for SELECT statements at the db backend.
    Since we're logging Django's backend classes, We don't use those to avoid infinite recursion.
    """

    def emit(self, record):
        if 'SELECT' in record.sql:
            db = MySQLdb.connect(host=env.MYSQL_HOST, user=env.MYSQL_USERNAME,
                                 passwd=env.MYSQL_PASSWORD, db=env.MYSQL_DATABASE)
            cursor = db.cursor()
            dt = time.strftime('%Y-%m-%d %H:%M:%S')
            try:
                cursor.execute(
                        'INSERT INTO log (`fecha`, `descripcion`) VALUES ("%s","ACTION:SELECT \n %s")' % (dt, record.sql))
            except:
                pass
            db.commit()
            db.close()
