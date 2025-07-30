
print("Hello, Git!")
from flask import Flask, request, jsonify
import requests

# Optional: keep your existing hello world print
print("✅ hello.py running...")

app = Flask(__name__)


BAMBOO_URL = "http://192.168.1.20:8085"  # Your Bamboo server IP
PLAN_KEY = "MYB"                  # Replace with your real Bamboo Plan key
BAMBOO_USER = "sneha"                   # Replace with your Bamboo username
BAMBOO_PASS = "Maha@13012020"                   # Replace with your Bamboo password

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.get_json()

        # Handle GitHub ping event
        if request.headers.get('X-GitHub-Event') == 'ping':
            print("✅ GitHub webhook ping received!")
            return jsonify({'message': 'Pong!'}), 200

        # Handle push event (real commits)
        if request.headers.get('X-GitHub-Event') == 'push':
            repo = data.get('repository', {}).get('full_name', 'unknown')
            pusher = data.get('pusher', {}).get('name', 'unknown')
            commit_msg = data.get('head_commit', {}).get('message', 'No commit message')

            print(f"📦 Repo: {repo}")
            print(f"👤 Pusher: {pusher}")
            print(f"💬 Commit message: {commit_msg}")

            # Trigger Bamboo or any other logic here...

            return jsonify({'message': 'Push received'}), 200

        return jsonify({'message': 'Unhandled event type'}), 200
    else:
        return jsonify({'error': 'Unsupported content type'}), 400
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
