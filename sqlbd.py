import psycopg2

db = BD
db.host


class BD:

    def init(self, Error=None, version=None):
        Error
        version
        self.connection = psycopg2.connect(
            host='ec2-54-228-139-34.eu-west-1.compute.amazonaws.com',
            user='jijysackpahqwk',
            password='e5b4dd520000c26bf3d2313a1e5522ffbfc2385168af3a7ce5adac1d5e29dd69',
            database='d7hh2s3obincbl')

        self.cursor = self.connection.cursor()

    def update_status(machine_status, machine_id):
        """ Connect to the PostgreSQL database server """

    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host='ec2-54-228-139-34.eu-west-1.compute.amazonaws.com',
                                user='jijysackpahqwk',
                                password='e5b4dd520000c26bf3d2313a1e5522ffbfc2385168af3a7ce5adac1d5e29dd69',
                                database='d7hh2s3obincbl')

        # create a cursor
        cur = conn.cursor()
        version = cur.fetchone()
        # execute a statement
        cur.execute("UPDATE mechanic SET machine_status = ? WHERE machine_id = 2", (machine_status, machine_id))
        # display the PostgreSQL database server version
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        Error = error
    finally:
        if conn is not None:
            conn.close()

    def close(self):
        self.connection.close()