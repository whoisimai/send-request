# Ping a server on Render
## Project Info:

This repo is designed to help counter the cold start on render issue. Render's free tier server usually shuts down after 15 minutes of inactivity. How this repo works is it sends a request to the server backend every 10 minutes and uses GitHub Actions as an automated workflow with a cron job to send requests every 10 minutes.

The only requirement is having Python & pip installed.

## Features:

- Automatic ping every 10 minutes (via GitHub Actions cron).
- Secure secret storage for your backend URL.
- Simple Python script using requests.
- Logs success/failure of each request.
- Manual trigger support via Run workflow button in GitHub.
- Run locally or on GitHub Actions.

### For setup follow these steps:

```sh
# Step 1: Clone the repository using the project's Git URL.
git clone https://github.com/whoIsImai/send-request.git

# Step 2: Navigate to the project directory.
cd send-request

# Step 3: Install the necessary dependencies.
pip install requests

# Step 4: Add your backend URL as a GitHub secret.

SERVER_URL=https://your-app.com/

# Step 5: Head to your actions tab on GitHub and run the workflow
```

## GitHub Actions (automated pings)

### If you prefer automation, set up the GitHub Actions workflow:

- Add your backend URL as a repository secret (SERVER_URL).
- The workflow (.github/workflows/keep_alive.yml) will run every 10 minutes automatically.
- Make sure the URL is a valid working endpoint that returns HTTP 200.