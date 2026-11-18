# 7Ton Express

[![Python](https://img.shields.io/badge/Python-Django-blue)](https://www.djangoproject.com/)

A Django-based courier booking website intended to let signed-in users enter shipment details, estimate delivery charges, create an order, and proceed to an external payment service.

> **Repository status:** This repository currently contains unresolved merge-conflict markers in application files, hard-coded credentials, and no dependency manifest. The documented setup is therefore a guide to the intended Django workflow, not a verified clean installation. Review the security and setup notes before running or deploying the project.

## Project Overview

7Ton Express is a server-rendered courier application. Its code collects shipment, sender, and recipient details; calculates volumetric weight and an estimated price using configured rates and surcharges; stores order information; and includes views for pending delivery, completed delivery, and pending payment.

The repository also includes Django Admin configuration, Django REST Framework usage, and django-allauth/Keycloak authentication configuration. The operational status of the configured external identity and payment services is not known.

## Project Screenshot

No application screenshot is currently included. Add a screenshot after confirming the app can be run safely, for example at `docs/screenshots/booking-flow.png`, then replace this note with:

```markdown
![7Ton Express shipment booking workflow](docs/screenshots/booking-flow.png)
```

## Live Demo

No verified live demo URL is available in the repository. The source contains references to `courier.etaka.online` and `7tonexpress.com`; their current status and authorization for use as a demo require confirmation.

## Key Features

Features visible in the source code include:

- Authenticated, multi-step shipment booking pages
- Sender and recipient contact and address fields
- Shipment type, destination, weight, and dimension inputs
- Volumetric-weight calculation
- Delivery-rate lookup by destination, shipment type, and weight
- Flat, percentage, and per-kilogram surcharge calculations
- Currency conversion using a stored currency rate
- Shipment order creation and partial-payment fields
- External payment URL request and redirect flow
- Views for pending deliveries, completed deliveries, and pending payments
- Django Admin integration
- Authentication routes through django-allauth, including Keycloak provider configuration
- A limited Django REST Framework view for payment-status updates

These behaviors have not been independently run or tested. In particular, merge-conflict markers currently prevent treating the code as a clean, executable application.

## Technology Stack

| Technology | Purpose in this repository |
|---|---|
| Python | Application language |
| Django | Web framework, templates, ORM, authentication, and administration |
| Django REST Framework | Serializer and API-view support |
| django-allauth | Account and social-auth routes |
| Keycloak provider for django-allauth | Configured external identity provider |
| django-cors-headers | CORS middleware |
| MySQL | Database engine configured in Django settings |
| HTML, CSS, JavaScript | Template-based interface and browser behavior |
| Bootstrap, jQuery | Frontend assets present in `static/` |
| Requests | Outbound HTTP call used by the payment flow |

## Dependencies and Their Purpose

There is no `requirements.txt`, `pyproject.toml`, or lock file. The table below lists packages referenced by settings or imports; exact versions and a complete installable dependency set must be confirmed by the maintainer.

| Package / component | Purpose |
|---|---|
| `Django` | Core web framework; settings comments indicate the project was generated with Django 4.0, but the installed version is not recorded |
| `djangorestframework` | API views, responses, and model serialization |
| `django-allauth` | Account and social authentication routes |
| Keycloak allauth provider | External identity-provider integration configured in settings |
| `django-cors-headers` | CORS middleware configured in settings |
| `requests` | Calls the external payment URL-generation service |
| MySQL database adapter | Required for the configured MySQL backend; the correct adapter and version are not documented |
| `django-sslserver` | Listed as an installed Django app; local or production requirement is unconfirmed |
| Bootstrap and jQuery assets | Frontend resources committed under `static/` |

`urllib3` is imported directly, but may be installed transitively; confirm whether it is an intentional direct dependency. Python's `enum` module is part of the standard library.

## Project Architecture

```text
.
├── courier/                 # Django settings, root URL configuration, ASGI/WSGI
├── delivery/                # Shipment views, models, URLs, serializers, migrations
├── adminpanel/              # Additional Django Admin configuration
├── templates/               # Server-rendered HTML templates
├── static/                  # CSS, JavaScript, images, fonts, and vendor assets
├── manage.py                # Django management entry point
├── db.sqlite3               # Committed SQLite database file
├── ecommercedb              # Additional committed database file
└── Customer rate 2019.xlsx  # Rate spreadsheet
```

The intended request flow is Django URL routing → delivery views → Django models/database. The booking views calculate a quote, create an order, and then call an external payment service. Payment callback and status-update behavior is present in the code but needs validation before use.

## Installation and Setup

### Prerequisites

- Python and pip (supported versions need confirmation)
- MySQL, if retaining the database backend currently configured in `courier/settings.py`
- Git

The repository does not pin Python, Django, or other package versions and does not provide a complete database initialization guide.

### Clone and create a virtual environment

```bash
git clone https://github.com/Munia2319/7Ton-Express.git
cd 7Ton-Express
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Install dependencies and configure a database

A reliable installation command cannot be provided yet: the repository has no dependency manifest, and source files contain unresolved merge-conflict markers. First resolve those conflicts, establish supported package versions, and add a dependency file. The settings currently configure MySQL at `localhost:3306` with a database named `courier`; configure a local database and credentials without committing secrets.

## Environment Variables

The project does not currently load settings from environment variables, and no `.env.example` is present. Settings and service credentials are hard-coded in source. Before running or publishing a working deployment, move secrets and environment-specific values into configuration, at minimum:

| Suggested variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Django signing key |
| `DJANGO_DEBUG` | Debug mode |
| `DJANGO_ALLOWED_HOSTS` | Allowed host names |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` | Database connection |
| `KEYCLOAK_URL`, `KEYCLOAK_REALM`, `KEYCLOAK_CLIENT_ID`, `KEYCLOAK_CLIENT_SECRET` | Identity-provider configuration |
| Payment-service URL and credentials | External payment integration, if still in use |

These are recommendations for future configuration, not variables currently supported by the code. **Do not copy the repository's existing credential values into documentation or new configuration files. Rotate any credentials that were real and have been committed.**

## Run Locally

A verified local run command is not available until the merge conflicts are resolved, dependencies are documented, and the database is configured. Once those prerequisites are addressed, the usual Django development commands are:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/`. These commands describe the standard Django workflow; they have **not** been verified against the current repository state.

## Routes and API

The root URL configuration includes the delivery URL configuration, Django Admin, and django-allauth routes. The delivery URL file declares these paths; confirm behavior and HTTP methods after resolving conflicts and testing the app.

| Path | Intended purpose indicated by the code |
|---|---|
| `/` and `/home/` | Home / shipment booking page |
| `/second/` | Shipment cost calculation step |
| `/third/` | Shipment details / confirmation step |
| `/test/` | Order creation and payment initiation flow |
| `/pending_delivery/` | Pending delivery list |
| `/completed_delivery/` | Completed delivery list |
| `/pending_payment/` | Pending payment list |
| `/test_payment/` | Payment-status callback handler |
| `/payment_success/` | Payment completion page |
| `/api_view/` | Authenticated DRF `PUT` view for payment-status data |
| `/admin/` | Django Admin |
| `/accounts/` | django-allauth routes |

The repository does not contain a complete API specification, request/response examples, or documented callback verification. Do not treat these routes as a stable public API without further review.

## Technical Challenges and Solutions

The implementation addresses several domain-specific concerns in code:

- **Price estimation:** Uses stored delivery rates and surcharge records to calculate an estimate based on destination, service type, and shipment weight/dimensions.
- **Volumetric weight:** Calculates a volumetric value from parcel dimensions and uses it in pricing logic.
- **Order/payment handoff:** Persists order information and requests an external payment URL before redirecting the user.
- **Multiple order states:** Provides separate views for unpaid, pending-delivery, and completed-delivery records.

These are observations from the source, not claims that the flows have been verified in a running deployment. The merge conflicts and lack of tests are unresolved issues rather than completed technical solutions.

## Technology Selection

The repository does not include a rationale written by its author. Based on the implementation, Django provides server-rendered pages, authentication, database models, migrations, and the Admin interface in one framework. Django REST Framework supports the limited API view. django-allauth and its Keycloak provider are configured for account and external identity flows. MySQL is selected in the current settings for persistent application data. Bootstrap and jQuery are included as frontend assets.

## Future Improvements

- Resolve merge-conflict markers and run Django system checks
- Add a complete, version-pinned dependency manifest
- Document supported Python, Django, and database versions
- Move secrets and deployment settings out of source; rotate exposed credentials
- Remove committed local databases, generated bytecode, backups, and private deployment notes
- Add `.gitignore` and a safe `.env.example`
- Add tests for quote calculations, order creation, authentication, and payment callbacks
- Verify payment callback authenticity and document the integration contract
- Replace raw SQL where practical with Django ORM queries
- Add form validation and explicit error handling for invalid input and failed external requests
- Document database setup and provide non-sensitive seed data if appropriate
- Add screenshots, a verified demo link, and an accurate license
- Add CI checks for formatting, tests, and Django system checks

## Relevant Links

- [GitHub repository](https://github.com/Munia2319/7Ton-Express)
- [Django documentation](https://docs.djangoproject.com/)
- [Django REST Framework documentation](https://www.django-rest-framework.org/)
- [django-allauth documentation](https://docs.allauth.org/)
- [MySQL documentation](https://dev.mysql.com/doc/)
- [Bootstrap documentation](https://getbootstrap.com/docs/)
- [jQuery documentation](https://api.jquery.com/)
