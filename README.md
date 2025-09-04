# 🛒 Django + Stripe E-commerce

> Un sistema de **comercio electrónico moderno** construido con Django, integrado con **Stripe** para procesamiento de pagos seguro y totalmente **containerizado con Docker**.
> Optimizado para **desarrollo en VS Code Dev Containers** y pensado para un despliegue en producción sin complicaciones.

---

## ✨ Características

* ⚡ **Backend Django 5.2.4** – Framework web robusto y seguro
* 💳 **Stripe Checkout** – Procesamiento de pagos rápido y confiable
* 📦 **Gestión de Productos** – CRUD completo con imágenes y precios
* 🖼️ **Soporte de Imágenes** – Carga y visualización de productos
* 🔧 **Admin Personalizado** – Import/Export de datos desde el panel de Django
* 📡 **API REST** – Endpoints con Django REST Framework
* 🐳 **Containerización** – Docker + Compose para dev/prod
* 🌐 **Proxy Reverso** – Nginx para estáticos y proxy
* 🖥️ **Dev Containers** – Entorno listo en VS Code
* 🎨 **UI Moderna** – Bootstrap 5 + HTMX para interacciones dinámicas

---

## 🛠️ Tecnologías Utilizadas

### 🔙 Backend

* Django · Django REST Framework
* dj-stripe (Stripe)
* Pillow (imágenes)
* WhiteNoise · django-import-export

### 🎨 Frontend

* Bootstrap 5 + django-bootstrap5
* HTMX

### ⚙️ Infraestructura

* Docker & Docker Compose
* Nginx · Gunicorn · Uvicorn

### 👨‍💻 Desarrollo

* VS Code Dev Containers
* Git & GitHub
* SQLite (desarrollo) → PostgreSQL/MySQL (producción)

---

## 📦 Instalación y Configuración

### 1️⃣ Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd django-stripe-ecommerce
```

### 2️⃣ Configurar Variables de Entorno

En `productos/settings.py` cambia tus claves de Stripe:

```python
STRIPE_LIVE_MODE = False  # Cambiar a True en producción
STRIPE_SECRET_KEY = "tu_clave_secreta"
STRIPE_PUBLIC_KEY = "tu_clave_publica"
```

### 3️⃣ Ejecutar con Docker

#### 🚀 Opción A – VS Code Dev Containers (Recomendado)

1. Abrir en VS Code
2. Instalar extensión **Dev Containers**
3. `Ctrl+Shift+P` → "Reopen in Container"

#### 🐳 Opción B – Docker Compose

```bash
docker-compose up --build
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py createsuperuser
docker-compose exec app python manage.py collectstatic --noinput
```

### 4️⃣ Acceso a la Aplicación

* 🌍 App Principal → [http://localhost/productos/](http://localhost/productos/)
* 🔑 Admin → [http://localhost/admin/](http://localhost/admin/)
* 🔌 API Stripe → [http://localhost/stripe/](http://localhost/stripe/)

---

## 📂 Estructura del Proyecto

```
django-stripe-ecommerce/
├── .devcontainer/        # Configuración Dev Containers
├── bases/                # Modelos base y auditoría
├── catalogo/              # Gestión de productos
├── pagos/                 # Integración Stripe
├── productos/             # Configuración principal Django
├── nginx/                 # Configuración Nginx
├── docker-compose.yml     # Orquestación Docker
├── Dockerfile             # Imagen principal
└── dependencias.txt       # Requerimientos
```

---

## 🧑‍💻 Funcionalidades Clave

### 🛍️ Gestión de Productos

* Listado con imágenes y precios
* Creación y edición desde panel de admin
* Importación/Exportación de productos

### 💳 Procesamiento de Pagos

* Stripe Checkout con soporte de tarjetas
* Webhooks preparados para producción
* Páginas de éxito y error personalizadas

### 🏗️ Arquitectura

* Modelo de auditoría integrado
* API REST lista para integraciones
* Interfaz responsive (Bootstrap + HTMX)

---

## 🚀 Despliegue en Producción

1. Configurar variables de entorno:

```python
DEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com']
STRIPE_LIVE_MODE = True
```

2. Migrar a **PostgreSQL/MySQL**
3. Configurar **archivos estáticos** en S3 u otro servicio
4. Activar **HTTPS/SSL** con Nginx + Certbot
5. Monitoreo y logging en servidor

```bash
docker-compose -f docker-compose.prod.yml up --build -d
```

---

## 🧪 Testing y Desarrollo

Ejecutar tests:

```bash
docker-compose exec app python manage.py test
```

Pruebas de carga:

```bash
python estres.py
```

Migraciones:

```bash
docker-compose exec app python manage.py makemigrations
docker-compose exec app python manage.py migrate
```

---

## 🔒 Stripe – Modos de Uso

### 🧪 Testing

* Claves de prueba ya configuradas
* Tarjeta de prueba: `4242 4242 4242 4242`

### 🚀 Producción

1. Generar claves reales en [Stripe Dashboard](https://dashboard.stripe.com/)
2. Configurar **Webhooks**
3. Activar `STRIPE_LIVE_MODE = True`

---

## 🗺️ Roadmap

* [ ] PostgreSQL por defecto
* [ ] Carrito de compras
* [ ] Sistema de inventario
* [ ] Cupones y descuentos
* [ ] Notificaciones por email
* [ ] Dashboard de analytics
* [ ] API GraphQL
* [ ] Integración con servicios de envío

---

## 🤝 Contribución

1. Haz un **fork**
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Commit: `git commit -m 'Nueva funcionalidad'`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Abre un **Pull Request** 🚀

---

## 📞 Soporte

* 📌 Issues en GitHub
* 📧 Contacto con el equipo de desarrollo
* 📚 Revisar documentación oficial de [Django](https://docs.djangoproject.com/) y [Stripe](https://stripe.com/docs)
