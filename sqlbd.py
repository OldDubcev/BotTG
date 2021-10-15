import psycopg2


class BD:
    def __init__(self):
        self.connection = psycopg2.connect(
        host ='ec2-54-228-139-34.eu-west-1.compute.amazonaws.com',
        user = 'jijysackpahqwk',
        password = 'e5b4dd520000c26bf3d2313a1e5522ffbfc2385168af3a7ce5adac1d5e29dd69',
        database = 'd7hh2s3obincbl')
        
        self.cursor = self.connection.cursor()
    
    def update_status(self, machine_status, machine_id):
        with self.connection:
            return self.cursor.execute("UPDATE `mechanic` SET `machine_status` = ? WHERE `machine_id` = 2", (machine_status, machine_id))

        
    def close(self):
        self.connection.close()    