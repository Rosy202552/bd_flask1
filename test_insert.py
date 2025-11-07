import psycopg2

try:
    conn = psycopg2.connect(
        host='localhost',
        database='alumnos_db',
        user='postgres',
        password='abc123'
    )
    cur = conn.cursor()
    # Insertar un registro con carácter acentuado
    cur.execute("INSERT INTO alumnos (matricula, nombre, edad) VALUES (%s, %s, %s) RETURNING id;", ('TST001', 'José', 30))
    new_id = cur.fetchone()[0]
    conn.commit()
    print(f'Registro insertado con id = {new_id}')

    # Leer el registro recién insertado
    cur.execute("SELECT matricula, nombre, edad FROM alumnos WHERE id = %s;", (new_id,))
    row = cur.fetchone()
    print('Registro leído:', row)

    cur.close()
    conn.close()
except Exception as e:
    print('Error:', e)
