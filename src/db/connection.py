import psycopg2

class PostgreSQLConnection:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
            print("Conexão estabelecida com sucesso!")
        except psycopg2.Error as e:
            print("Erro ao conectar ao PostgreSQL:", e)

    def execute_query(self, query):
        if not self.conn:
            print("Erro: Conexão com o banco de dados não estabelecida.")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except psycopg2.Error as e:
            print("Erro ao executar a consulta:", e)
            return None
        
    def insert_user(self, id, name, area, job_description, role, salary, is_active, last_evaluation=None):
        if not self.conn:
            print("Erro: Conexão com o banco de dados não estabelecida.")
            return
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO users (id, name, area, job_description, role, salary, is_active, last_evaluation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (id, name, area, job_description, role, salary, is_active, last_evaluation)
            )
            self.conn.commit()
            cursor.close()
            print("Registro inserido com sucesso!")
        except psycopg2.Error as e:
            print("Erro ao inserir registro:", e)

    def delete_user(self, id):
        if not self.conn:
            print("Erro: Conexão com o banco de dados não estabelecida.")
            return
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "DELETE FROM users WHERE id = %s",
                (id,)
            )
            self.conn.commit()
            cursor.close()
            print("Registro deletado com sucesso!")
        except psycopg2.Error as e:
            print("Erro ao deletar registro:", e)

    def update_user(self, id, name=None, area=None, job_description=None, role=None, salary=None, is_active=None, last_evaluation=None):
        if not self.conn:
            print("Erro: Conexão com o banco de dados não estabelecida.")
            return
        try:
            cursor = self.conn.cursor()
            update_query = "UPDATE users SET"
            update_values = []
            if name is not None:
                update_query += " name = %s,"
                update_values.append(name)
            if area is not None:
                update_query += " area = %s,"
                update_values.append(area)
            if job_description is not None:
                update_query += " job_description = %s,"
                update_values.append(job_description)
            if role is not None:
                update_query += " role = %s,"
                update_values.append(role)
            if salary is not None:
                update_query += " salary = %s,"
                update_values.append(salary)
            if is_active is not None:
                update_query += " is_active = %s,"
                update_values.append(is_active)
            if last_evaluation is not None:
                update_query += " last_evaluation = %s,"
                update_values.append(last_evaluation)
            
            # Remove a última vírgula e adiciona a condição WHERE
            update_query = update_query.rstrip(',') + " WHERE id = %s"
            update_values.append(id)
            
            cursor.execute(update_query, tuple(update_values))
            self.conn.commit()
            cursor.close()
            print("Registro atualizado com sucesso!")
        except psycopg2.Error as e:
            print("Erro ao atualizar registro:", e)

    def close(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")