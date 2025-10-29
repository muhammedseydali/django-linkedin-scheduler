Automate & Schedule LinkedIn Posts with Django + Inngest

Building social automation tools often starts simple — posting content via an API call.
But once you need to schedule posts, handle user authentication, and ensure reliable delivery, things quickly become complex.

This project demonstrates how to build a LinkedIn post scheduler using Python, Django, and Inngest to manage asynchronous, delayed, and reliable task execution.

🧩 Key Features

✅ LinkedIn OAuth Integration — Securely connect user LinkedIn accounts
✅ Post Scheduling — Schedule posts for a future date/time
✅ Inngest Task Execution — Offload and process scheduled jobs
✅ Multi-Platform Ready — Extend to other social platforms (X, Facebook, Discord, etc.)
✅ Django Admin Dashboard — Manage posts and user connections easily

⚙️ Architecture Overview
🔐 OAuth Flow

Create a LinkedIn App in the LinkedIn Developer Portal
.

Store your app credentials (CLIENT_ID, CLIENT_SECRET, REDIRECT_URI) in environment variables.

Configure Django with Django AllAuth or a similar OAuth library.

When users click “Connect with LinkedIn”, Django redirects them to LinkedIn’s OAuth page.

After successful authorization, LinkedIn returns an Access Token.

Django stores this token for authenticated API use.

🧠 How It Works

User connects LinkedIn via OAuth

User creates a post in Django (with content + scheduled time)

Django saves the post and sends a delayed task to Inngest

At the scheduled time, Inngest triggers the task

Django uses the stored LinkedIn token to send a POST request to LinkedIn’s API

LinkedIn publishes the post on behalf of the user 🎯

🛠️ Tech Stack

Python 3.10+

Django (backend framework)

Django AllAuth (OAuth support)

Inngest (event-driven and scheduled task handler)

Requests / HTTPX (API communication)

SQLite / PostgreSQL (data storage)
