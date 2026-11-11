# SRI-WEB-003 — Appointment Booking Desk

- **Purpose:** collect a structured appointment request for a small service business.
- **Audience:** clinics (administrative enquiries only), salons, tutors, consultants and independent service providers.
- **Workflow:** configure business name, service, duration, WhatsApp contact and offered time labels; customer enters name, phone, date, preferred time and optional note; app generates a clearly unconfirmed request summary for WhatsApp, copy or print/PDF.
- **Runtime:** browser-local only. No server, persistent storage, live calendar, slot locking, reminders, cancellation, staff scheduling, payment, customer account or automatic confirmation.
- **Privacy:** do not enter sensitive health or financial information. No form submission to a remote server occurs.
- **Commercial delivery:** sell as a configurable enquiry-form prototype or customisation service only. A production booking system requires backend/database, authenticated business access, concurrency-safe slot reservation, privacy controls, notification and recovery workflows.
- **Release gate:** test date minimum, invalid dates, time parsing, missing fields, phone validation, WhatsApp encoding, mobile/desktop layout, print output and explicit unconfirmed status.
- **Truth boundary:** generated request text is not a booked slot, appointment confirmation, payment, or proof of service delivery.
- **Version:** 1.0 prototype.
