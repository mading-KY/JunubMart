# JunubMart Development Journal

This journal documents the progress, lessons learned, challenges encountered, and milestones achieved throughout the development of JunubMart.

---

# Week 1
**Duration:** 25 June 2026 – 1 July 2026

## Theme
Project Foundation

---

## Learning Objectives

- Understand Django project structure.
- Learn the purpose of `manage.py`.
- Understand the MVT (Model-View-Template) architecture.
- Learn the difference between a Django Project and a Django App.
- Set up the development environment.
- Learn basic Git workflow.

---

## Completed

### Project Setup

- Installed Python and Django.
- Created the JunubMart project.
- Created a virtual environment.
- Configured SQLite database.
- Created a superuser.
- Successfully accessed the Django Admin panel.

### Project Architecture

Created the following applications:

- Core
- Marketplace
- Accounts
- Rentals
- Orders

Organized each application with:

- templates/
- static/
- urls.py

Created a modular project structure following Django best practices.

---

## Challenges

- Renamed the `store` app to `marketplace`.
- Fixed import and configuration issues after renaming.
- Learned how Django discovers installed applications.
- Understood the importance of app names and configuration.

---

## Lessons Learned

- A Django project can contain multiple applications.
- Each application should have a single responsibility.
- URLs are organized into project-level and app-level routing.
- Templates and static files are namespaced to avoid conflicts.
- Building the project incrementally makes debugging easier.

---

## Reflection

This week focused on laying a strong foundation rather than building visible features. Although little functionality was added, understanding the project structure, Django applications, and project organization established the groundwork for the weeks ahead.

---

# Week 2

**Status:** In Progress

### Theme

Connecting URLs, Views, and Templates

Objectives:

- Understand Django URL routing.
- Learn how views handle requests.
- Render templates from views.
- Build the first working pages of JunubMart.