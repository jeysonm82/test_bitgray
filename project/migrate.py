import env
import MySQLdb
from subprocess import call
import os

DB_EXISTS = 1007
db = MySQLdb.connect(host=env.MYSQL_HOST, user=env.MYSQL_USERNAME,
                     passwd=env.MYSQL_PASSWORD)
cursor = db.cursor()

try:
    cursor.execute("CREATE DATABASE %s" % (env.MYSQL_DATABASE))
except MySQLdb.ProgrammingError as e:
    errcode = e.args[0]
    if errcode != DB_EXISTS:
        raise

db.close()

# Execute script prueba_python_1_0.sql using command line mysql
os.system('mysql -u%s -p"%s" %s < prueba_python_1_0.sql' %
          (env.MYSQL_USERNAME, env.MYSQL_PASSWORD, env.MYSQL_DATABASE))
