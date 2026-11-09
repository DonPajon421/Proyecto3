# Proyecto3: API REST de mascotas

API REST en Django + Django REST Framework con el CRUD de `Responsable` y `Mascota`
(un responsable tiene muchas mascotas), conectada a MariaDB, más el front React
(Vite) en la carpeta `frontend/`.

## Estructura

```
Proyecto3/
├── Proyecto3/          settings.py, urls.py (las 8 URLs, sin include)
├── Mascotas/           models.py, serializers.py, views.py, tests.py, admin.py
├── bruno/              colección de Bruno con todas las pruebas
├── frontend/           front Vite + React (interfaz "Mascotas CRUD")
└── requirements.txt
```

## 1. Backend (terminal 1)

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

La base de datos se configura en `Proyecto3/settings.py` (`DATABASES`) y debe existir
en MariaDB antes de migrar:

```sql
CREATE DATABASE Proyecto_3_DB CHARACTER SET utf8mb4;
```

## 2. Front (terminal 2)

```bash
cd frontend
npm install
npm run dev
```

Abrir http://localhost:5173. El front llama a `/api/...` y Vite lo redirige a
`http://127.0.0.1:8000`, por eso Django debe estar corriendo en el puerto 8000.

## Endpoints

| URL                           | Vista                   | Método     | Éxito | Error    |
|-------------------------------|-------------------------|------------|-------|----------|
| `/mascota/crear`              | `crear_mascota`         | POST o PUT | 201   | 400      |
| `/mascotas`                   | `listar_mascotas`       | GET        | 200   |          |
| `/mascota/modificar/<id>`     | `modificar_mascota`     | PATCH      | 200   | 400, 404 |
| `/mascota/eliminar/<id>`      | `eliminar_mascota`      | DELETE     | 204   | 404      |
| `/responsable/crear`          | `crear_responsable`     | POST o PUT | 201   | 400      |
| `/responsables`               | `listar_responsable`    | GET        | 200   |          |
| `/responsable/modificar/<id>` | `modificar_responsable` | PATCH      | 200   | 400, 404 |
| `/responsable/eliminar/<id>`  | `eliminar_responsable`  | DELETE     | 204   | 404      |

Cualquier otro método responde 405 (lo hace `@api_view`).

## Pruebas automáticas

**Tests de Django** (24 casos, usan una BD temporal `test_...`, no tocan tus datos):

```bash
python manage.py test Mascotas
```

**Colección de Bruno** (15 peticiones con sus códigos esperados, incluye los 6 casos
de error del enunciado). Con Django corriendo:

- En la app de Bruno: *Open Collection* → carpeta `bruno/` → entorno `local` → *Run*.
- O por terminal: `npm i -g @usebruno/cli` y luego `cd bruno && bru run --env local`.
