import requests

BASE_URL = "http://localhost:8000"

def test_create_todo():
    print("\n📝 POST /todos")
    payload = {"name": "Test CRUD completo", "completed": False}
    res = requests.post(f"{BASE_URL}/todos", json=payload)
    assert res.status_code == 200
    data = res.json()
    print("✅ Creado:", data)
    return data["id"]

def test_get_all():
    print("\n📄 GET /todos")
    res = requests.get(f"{BASE_URL}/todos")
    assert res.status_code == 200
    print("✅ Todos encontrados:", res.json())

def test_get_one(todo_id):
    print(f"\n🔍 GET /todos/{todo_id}")
    res = requests.get(f"{BASE_URL}/todos/{todo_id}")
    assert res.status_code == 200
    print("✅ Detalles:", res.json())

def test_update(todo_id):
    print(f"\n✏️ PUT /todos/{todo_id}")
    payload = {"name": "Actualizado desde test", "completed": True}
    res = requests.put(f"{BASE_URL}/todos/{todo_id}", json=payload)
    assert res.status_code == 200
    print("✅ Actualizado:", res.json())

def test_delete(todo_id):
    print(f"\n🗑 DELETE /todos/{todo_id}")
    res = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    assert res.status_code == 200
    print("✅ Eliminado")

if __name__ == "__main__":
    test_get_all()
    new_id = test_create_todo()
    test_get_one(new_id)
    test_update(new_id)
    test_get_one(new_id)
    test_delete(new_id)
    test_get_all()
