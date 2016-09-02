import MySQLdb
import smtplib
import env
# Not using Django's ORM due to lack of calculated fields logic


def send_report():
    db = MySQLdb.connect(host=env.MYSQL_HOST, user=env.MYSQL_USERNAME,
                         passwd=env.MYSQL_PASSWORD, db=env.MYSQL_DATABASE)

    report = """
    COMPRAS REPORT
    ==============
    Precio productos - Precio compras:
    - Diferencia promedio: %.2f
    - Max: %s
    - Min: %s

    Compras:
    - Num. Compras: %s
    - Total ganacias: %s
    - Compras promedio por minuto: %.2f
    """

    cursor = db.cursor()

    cursor.execute("""SELECT AVG(sub.diff) as prom, MAX(sub.diff) as max,
                      MIN(sub.diff) as min, count(*) as numcompras,
                      SUM(sub.diff) as ganancias FROM
                      (SELECT productos.precio - compras.precio as diff FROM compras
                      INNER JOIN productos ON compras.id_producto=productos.id)
                      as sub""")

    prom, max_d, min_d, numcompras, ganancias = cursor.fetchone()

    cursor.execute("""SELECT AVG(sub.numcompras) as promcompras FROM
                    (SELECT  DATE_FORMAT(fecha, '%Y%m%d%H%i') as fc,
                     Count(*) as numcompras FROM compras GROUP BY fc) as sub""")
    promcompras, = cursor.fetchone()

    report = report % (prom, max_d, min_d, numcompras, ganancias, promcompras)
    # Send report by email
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login("testbgray.jmolina@gmail.com", "testbgray2016")
    header = 'To:' + "testbgray.jmolina@gmail.com" + '\n' + 'From: ' + \
        "testbgray.jmolina@gmail.com" + '\n' + 'Subject:testing \n'
    msg = header + '\n %s \n\n' % (report)
    server.sendmail(
        "testbgray.jmolina@gmail.com", "testbgray.jmolina@gmail.com", msg)
    server.close()
    db.close()
    return report

if __name__ == '__main__':
    send_report()
