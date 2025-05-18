from sqlalchemy import inspect, text
from sqlalchemy.orm import Session
from schema import ToDoResponse
from database import engine, SessionLocal
from pydantic import ValidationError

inspector = inspect(engine)

def run_connection_test():
    print("🔌 Verificando conexión...")
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1")).scalar()
            if result == 1:
                print("✅ Conexión exitosa con PostgreSQL")
            else:
                print("❌ Fallo en la conexión")
    except Exception as e:
        print(f"❌ Error al conectar: {e}")
        return

    print("\n📋 Verificando tablas...")
    tables = inspector.get_table_names()
    print(f"Tablas encontradas: {tables}")
    if "todos" not in tables:
        print("❌ La tabla 'todos' no existe")
        return

    print("\n🔍 Verificando columnas de 'todos'...")
    columns = inspector.get_columns("todos")
    col_names = {col["name"] for col in columns}
    print(f"Columnas encontradas: {col_names}")
    expected = {"id", "name", "completed"}
    missing = expected - col_names
    if missing:
        print(f"❌ Faltan columnas: {missing}")
        return
    else:
        print("✅ La estructura de 'todos' es correcta")

    print("\n📄 Probando consulta real sobre 'todos' y validación con ToDoResponse...")
    try:
        with SessionLocal() as session:
            rows = session.execute(text("SELECT * FROM todos LIMIT 5")).fetchall()
            if not rows:
                print("⚠️ No hay registros en la tabla 'todos' (aún).")
            else:
                print(f"✅ Se encontraron {len(rows)} registros:")
                for row in rows:
                    try:
                        todo = ToDoResponse.from_orm(row)
                        print(f"✅ Validado: {todo}")
                    except ValidationError as ve:
                        print(f"❌ Error de validación: {ve}")
    except Exception as e:
        print(f"❌ Error en consulta: {e}")

if __name__ == "__main__":
    run_connection_test()

