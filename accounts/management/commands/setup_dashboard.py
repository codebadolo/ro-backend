import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Set up the dashboard template structure and base files'

    def handle(self, *args, **kwargs):
        # Define paths
        app_dir = os.path.join(os.getcwd(), 'accounts')
        templates_dir = os.path.join(app_dir, 'templates', 'accounts')
        static_dir = os.path.join(app_dir, 'static', 'accounts')

        # Create directories if they don't exist
        os.makedirs(templates_dir, exist_ok=True)
        os.makedirs(static_dir, exist_ok=True)

        # Create base.html
        base_html_path = os.path.join(templates_dir, 'base.html')
        with open(base_html_path, 'w') as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Dashboard{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Dashboard</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="#">Profile</a></li>
                    <li class="nav-item"><a class="nav-link text-danger" href="/logout/">Logout</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% block content %}
        {% endblock %}
    </div>

    <!-- Optional JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>""")

        # Create dashboard.html
        dashboard_html_path = os.path.join(templates_dir, 'dashboard.html')
        with open(dashboard_html_path, 'w') as f:
            f.write("""{% extends "accounts/base.html" %}

{% block title %}User Dashboard{% endblock %}

{% block content %}
<div class="row">
    <!-- Sidebar -->
    <nav class="col-md-2 d-none d-md-block bg-light sidebar">
        <ul class="list-group list-group-flush">
            <li class="list-group-item"><a href="#">Overview</a></li>
            <li class="list-group-item"><a href="#">Reports</a></li>
            <li class="list-group-item"><a href="#">Settings</a></li>
        </ul>
    </nav>

    <!-- Main Content -->
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
        <h1>Welcome to Your Dashboard!</h1>
        <!-- Add charts or other content here -->
        <p>This is the main content area.</p>
    </main>
</div>
{% endblock %}""")

        self.stdout.write(self.style.SUCCESS('Dashboard template structure and base files created successfully!'))
