import psycopg2

def test_connection():
    try:
        # Intentar conexión
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",  # Base de datos por defecto
            user="postgres",      # Usuario por defecto
            password="abc123"     # Tu contraseña
        )
        
        # Obtener versión
        cur = conn.cursor()
        cur.execute('SELECT version();')
        version = cur.fetchone()
        print("Conexión exitosa!")
        print("Versión de PostgreSQL:", version[0])
        
        # Listar bases de datos
        cur.execute("SELECT datname FROM pg_database;")
        print("\nBases de datos disponibles:")
        for db in cur.fetchall():
            print(f"- {db[0]}")
            
        # Cerrar
        cur.close()
        conn.close()
        
    except Exception as e:
        print("Error de conexión:", str(e))

if __name__ == "__main__":
    test_connection()