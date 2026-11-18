# 7Ton Express

[![Python](https://img.shields.io/badge/Python-3-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Framework-Django-092E20)](https://www.djangoproject.com/)

**Live website:** [7tonexpress.com](https://7tonexpress.com/)

7Ton Express is a courier booking website that helps customers submit shipment details, estimate delivery charges, create orders, and proceed to payment. I contributed to the **backend**, working on the Django booking and order workflow.

## Features

- Multi-step shipment booking with sender and recipient details
- Volumetric-weight and delivery-cost calculations using configured rates and surcharges
- Order creation and payment handoff
- Views for pending payments, pending deliveries, and completed deliveries
- Django Admin and authentication integration

## Technology Stack

- Python and Django
- Django REST Framework
- MySQL
- Django templates, HTML, CSS, and JavaScript

## Project Structure

- `courier/` — Django project configuration and root routes
- `delivery/` — Shipment views, models, URLs, serializers, and migrations
- `adminpanel/` — Admin configuration
- `templates/` — Server-rendered pages
- `static/` — Frontend styles, scripts, and assets

## Local Development

The project is configured to use MySQL. Configure the database and install the project’s required Python packages before starting the Django development server:

```bash
python manage.py migrate
python manage.py runserver
```

## Links

- [Live website](https://7tonexpress.com/)
- [Source code](https://github.com/Munia2319/7Ton-Express)
