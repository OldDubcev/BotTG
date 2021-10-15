import psycopg2


class BD:

    def __init__(self, Error=None, version=None):
        Error
        version
        self.connection = psycopg2.connect(
            host='ec2-54-228-139-34.eu-west-1.compute.amazonaws.com',
            user='jijysackpahqwk',
            password='e5b4dd520000c26bf3d2313a1e5522ffbfc2385168af3a7ce5adac1d5e29dd69',
            database='d7hh2s3obincbl')

        self.cursor = self.connection.cursor()

    def update_status(self,machine_status, machine_id):
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
            #txt2 = "UPDATE mechanic SET machine_status = {0} WHERE machine_id = {1}".format(machine_status,machine_id)
            txt2 = "UPDATE mechanic SET machine_status = {0} WHERE machine_id = {1}".format(machine_status,machine_id)
            cur.execute(txt2)
            conn.commit()
            # display the PostgreSQL database server version
            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            Error = error
        finally:
            if conn is not None:
                conn.close()