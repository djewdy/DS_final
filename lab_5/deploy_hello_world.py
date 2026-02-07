#!/usr/bin/env python3
"""
Lab 5 - Friendly Hello World Web Application
A simple Flask web application for DigitalOcean deployment.
"""

from flask import Flask, render_template_string
from datetime import datetime
import os

# Create Flask application instance
app = Flask(__name__)

# HTML template for a beautiful, friendly interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            text-align: center;
            max-width: 600px;
            width: 100%;
            animation: fadeIn 0.8s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        h1 {
            color: #333;
            font-size: 2.5em;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .emoji {
            font-size: 4em;
            margin: 20px 0;
            display: block;
            animation: bounce 2s infinite;
        }
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }
        p {
            color: #666;
            font-size: 1.2em;
            line-height: 1.6;
            margin: 15px 0;
        }
        .highlight {
            background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
            padding: 8px 15px;
            border-radius: 25px;
            font-weight: bold;
            display: inline-block;
            margin: 10px 0;
        }
        .nav {
            margin-top: 30px;
        }
        .nav a {
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            transition: all 0.3s ease;
            font-weight: 600;
        }
        .nav a:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        }
        .footer {
            margin-top: 30px;
            font-size: 0.9em;
            color: #888;
            border-top: 1px solid #eee;
            padding-top: 20px;
        }
        .platform-badge {
            background: #0080ff;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            margin: 10px 0;
            display: inline-block;
        }
    </style>
</head>
<body>
    <div class="container">
        <span class="emoji">{{ emoji }}</span>
        <h1>{{ heading }}</h1>
        <p>{{ message }}</p>
        <div class="highlight">{{ highlight_text }}</div>
        <div class="platform-badge">🚀 Powered by DigitalOcean</div>
        <p><strong>Current Time:</strong> {{ current_time }}</p>
        
        <div class="nav">
            <a href="/">🏠 Home</a>
            <a href="/about">ℹ️ About</a>
            <a href="/greet/Friend">👋 Say Hello</a>
            <a href="/status">📊 Status</a>
        </div>
        
        <div class="footer">
            <p>Lab 5 - DigitalOcean Deployment Demo</p>
            <p>Built with ❤️ using Flask & Python</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def hello_world():
    """Main route displaying a friendly hello world message."""
    return render_template_string(HTML_TEMPLATE,
        title="Welcome to Our Friendly App!",
        emoji="🌍",
        heading="Hello, Beautiful World!",
        message="🎉 Welcome to our amazing web application! We're so excited to have you here. This friendly app is running on DigitalOcean and ready to brighten your day!",
        highlight_text="✨ Spreading joy across the internet, one visit at a time! ✨",
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    )

@app.route('/about')
def about():
    """About page with information about the application."""
    return render_template_string(HTML_TEMPLATE,
        title="About Our App",
        emoji="📱",
        heading="About This Friendly App",
        message="This is a delightful Flask web application created for Lab 5! It demonstrates how to deploy a Python web app to DigitalOcean's App Platform. Simple, beautiful, and ready to scale!",
        highlight_text="🚀 Built for the cloud, designed for happiness!",
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    )

@app.route('/greet/<name>')
def greet_user(name):
    """Personalized greeting route."""
    return render_template_string(HTML_TEMPLATE,
        title=f"Hello, {name}!",
        emoji="👋",
        heading=f"Hello there, {name}!",
        message=f"What a wonderful name, {name}! 🌟 We're absolutely delighted to meet you. Thanks for visiting our friendly application running on DigitalOcean. We hope you're having an fantastic day!",
        highlight_text=f"🎉 {name}, you're absolutely awesome! 🎉",
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    )

@app.route('/status')
def status():
    """Application status and environment information."""
    python_version = f"{os.sys.version_info.major}.{os.sys.version_info.minor}.{os.sys.version_info.micro}"
    
    return render_template_string(HTML_TEMPLATE,
        title="App Status",
        emoji="✅",
        heading="Application Status",
        message=f"🟢 Everything is running smoothly! Our application is healthy and ready to serve. Python version: {python_version}. All systems are go on DigitalOcean!",
        highlight_text="💫 Ready to handle all your requests! 💫",
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    )

@app.route('/api/health')
def health_check():
    """Health check endpoint for DigitalOcean monitoring."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "message": "Hello World app is running great!"
    }

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 error page."""
    return render_template_string(HTML_TEMPLATE,
        title="Oops! Page Not Found",
        emoji="🤔",
        heading="Hmm, we can't find that page!",
        message="Don't worry though - even the best explorers sometimes take a wrong turn! Let's get you back on track to something amazing.",
        highlight_text="🧭 Let's navigate back to familiar territory!",
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    ), 404

if __name__ == '__main__':
    # Get port from environment variable or default to 5000 for local development
    # DigitalOcean will set the PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    
    # Print startup messages
    print("🚀 Starting the Friendly Hello World application...")
    print(f"🌐 Application will be available at http://localhost:{port}")
    print("💙 Ready for DigitalOcean deployment!")
    
    # Run the application
    # debug=False for production, host='0.0.0.0' to accept external connections
    app.run(host='0.0.0.0', port=port, debug=False)