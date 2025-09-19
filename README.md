# Ping a server on Render
## Project Info:

This repo is designed to help counter the cold start on render issue. Render's free tier server usually shuts down after 15 minutes of inactivity. How this repo works is it sends a request to the servers backend every 10 minutes and uses GitHub Action as an automated workflow with a cron job to send requests every 10 minutes.

The only requirement is having Python & pip installed.

Follow these steps:

```sh
# Step 1: Clone the repository using the project's Git URL.
git clone https://github.com/whoIsImai/send-request.git

# Step 2: Navigate to the project directory.
cd send-request

# Step 3: Install the necessary dependencies.
pip install requests

```