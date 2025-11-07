import psycopg2

def setup_database():
    try:
        # Conectar a la base de datos
        conn = psycopg2.connect(
            host="localhost",
            database="alumnos_db",
            user="postgres",
            password="abc123"
        )
        conn.autocommit = True
        cur = conn.cursor()
        
        # Crear tabla si no existe
        cur.execute("""
            CREATE TABLE IF NOT EXISTS alumnos (
                id SERIAL PRIMARY KEY,
                matricula VARCHAR(20) UNIQUE NOT NULL,
                nombre VARCHAR(100) NOT NULL,
                edad INTEGER NOT NULL
            );
        """)
        
        print("¡Tabla 'alumnos' creada o verificada correctamente!")
        
        # Cerrar
        cur.close()
        conn.close()
        
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    setup_database()