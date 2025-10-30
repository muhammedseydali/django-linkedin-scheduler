# Automate & Schedule LinkedIn Posts with Django + Inngest

Building social automation tools often starts simple — posting content via an API call.  
But once you need to schedule posts, handle user authentication, and ensure reliable delivery, things quickly become complex.

This project demonstrates how to build a **LinkedIn Post Scheduler** using **Python**, **Django**, and **Inngest** to manage asynchronous, delayed, and reliable task execution.

---

##  Key Features

✅ **LinkedIn OAuth Integration** — Securely connect user LinkedIn accounts  
✅ **Post Scheduling** — Schedule posts for a specific future date/time  
✅ **Inngest Task Execution** — Offload, queue, and process scheduled jobs  
✅ **Multi-Platform Ready** — Extend easily to Facebook, X (Twitter), or Discord  
✅ **Admin Panel Management** — Manage posts, users, and scheduled tasks from Django admin  

---

##  System Architecture

The system is divided into three main components:

- **Django Backend** — Handles authentication, post creation, and API communication  
- **LinkedIn API** — Publishes posts on behalf of users using OAuth tokens  
- **Inngest Worker** — Manages event scheduling, delayed task execution, and retries  

---

##  System Flow Diagram

Here’s how everything connects:

```mermaid
graph TD
    A[ User] -->|Clicks "Login with LinkedIn"| B[Django + AllAuth]
    B -->|OAuth Redirect| C[🔗 LinkedIn OAuth]
    C -->|Returns Access Token| B
    B -->|Stores Token| D[(Database)]

    A -->|Creates Post + Schedule Time| B
    B -->|Sends Task Event| E[⚙️ Inngest]
    E -->|Waits Until Scheduled Time| F[⏰ Inngest Worker]
    F -->|Triggers POST Request| G[🌐 LinkedIn API]
    G -->|Publishes Post| H[📰 LinkedIn Feed]
OAuth Authentication Flow
Create a LinkedIn Developer App at LinkedIn Developers.

Copy your Client ID, Client Secret, and Redirect URI.

Add them to your .env file (see below).

Django handles the OAuth redirect via Django AllAuth.

After successful authentication, LinkedIn returns an Access Token.

Django securely stores this token for future API requests.

Requirements

Python 3.10+

Django 5.x

Django AllAuth

Inngest (Node CLI)

Requests / HTTPX

PostgreSQL or SQLite

Environment Variables
Create a .env file in your project root:

bash
Copy code
LINKEDIN_CLIENT_ID=your_client_id
LINKEDIN_CLIENT_SECRET=your_client_secret
LINKEDIN_REDIRECT_URI=http://localhost:8000/accounts/linkedin/login/callback/
INNGEST_API_KEY=your_inngest_api_key
DJANGO_SECRET_KEY=your_django_secret_key
▶️ Run the Project
bash
Copy code
# 1️⃣ Activate virtual environment
source venv/bin/activate

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run migrations
python manage.py migrate

# 4️⃣ Start Django server
python manage.py runserver

# 5️⃣ Start Inngest dev worker
npx inngest dev
Running Inngest with Docker
You can run the Inngest development server locally using Docker.
This allows your Django app to send scheduled events and handle asynchronous tasks.

Docker Compose Example
yaml
Copy code
services:
  scheduler_server:
    image: inngest/inngest
    ports:
      - "8288:8288"
    command: inngest dev -u http://host.docker.internal:8000/api/inngest --no-discovery
Explanation

image: inngest/inngest → uses the official Inngest Docker image

ports: "8288:8288" → exposes the Inngest dev UI locally at http://localhost:8288

command → runs the Inngest dev server pointing to your Django API endpoint:
-u http://host.docker.internal:8000/api/inngest tells Inngest where your Django backend is running
--no-discovery disables automatic function discovery (useful in dev)

🏃 Run the Docker Service
Ensure Docker Desktop is running on your machine

Save the service in a docker-compose.yml file

Start the service:

bash
Copy code
docker-compose up scheduler_server
Then open your browser at http://localhost:8288 to see Inngest’s dev interface.
Your Django app can now send events to Inngest for scheduling tasks like LinkedIn post sharing.

💡 Future Improvements
Add support for scheduling media posts (images/videos)

Extend OAuth integration to other social platforms

Add analytics and post engagement tracking

Author
Muhammed Seydali
Founder, The Code Club
Building innovative automation & web solutions

License
This project is licensed under the MIT License — see the LICENSE file for details.

---

Would you like me to also create a **GitHub-ready preview image** (architecture diagram or project banner) for the top of your README?  
It helps a lot with presentation if you plan to publish it publicly.