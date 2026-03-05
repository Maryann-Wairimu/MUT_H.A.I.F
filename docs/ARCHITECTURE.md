## MUT H.A.I.F – High-level Architecture

- **Backend**: Django 5 + Django REST Framework, with apps:
  - `accounts` – custom user model with roles (student, hostel_admin, finance_officer, super_admin), login/logout/me endpoints.
  - `students` – student profile and program data.
  - `hostels` – hostels, rooms, room types, allocations.
  - `finance` – fee types, hostel fee structures, invoices, payments.
  - `reports` – report snapshots for analytics.
- **Frontend**: React + Vite + Tailwind CSS, with feature modules:
  - Auth (login page, session handling).
  - Portal shell and landing page, ready for student/hostel admin/finance/reporting dashboards.

APIs are exposed under `/api/v1/` in `mut_haif.api_urls`, with DRF routers for the main resources and basic role-based permissions wired via `accounts.permissions`.

