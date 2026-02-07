# Friendly Hello World - DigitalOcean Deployment

A cheerful Flask web application designed for easy deployment to DigitalOcean App Platform.

## 🌟 Features

- Beautiful, responsive design with animations
- Multiple friendly routes
- Health check endpoint for monitoring
- Optimized for DigitalOcean deployment
- Mobile-friendly interface

## 🚀 Routes Available

- `/` - Main hello world page with animated welcome
- `/about` - Information about the application
- `/greet/<name>` - Personalized greeting (try `/greet/YourName`)
- `/status` - Application status and system info
- `/api/health` - JSON health check endpoint

## 🏃‍♂️ Local Development

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**

   ```bash
   python deploy_hello_world.py
   ```

3. **Open in browser:**
   Visit `http://localhost:5000`

## 🌊 Deploy to DigitalOcean

### Method 1: Using DigitalOcean App Platform (Recommended)

1. **Push your code to GitHub:**

   ```bash
   git init
   git add .
   git commit -m "Initial commit - Friendly Hello World app"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git push -u origin main
   ```

2. **Create app on DigitalOcean:**

   - Go to [DigitalOcean App Platform](https://cloud.digitalocean.com/apps)
   - Click "Create App"
   - Connect your GitHub repository
   - Select the repository containing this code
   - DigitalOcean will auto-detect it's a Python app

3. **Configure the app:**

   - App name: `friendly-hello-world` (or your preferred name)
   - Environment: `requirements.txt` will be automatically detected
   - Build command: Will be auto-configured
   - Run command: `gunicorn deploy_hello_world:app`

4. **Deploy:**
   - Click "Create App"
   - Wait for deployment (usually 2-3 minutes)
   - Your app will be available at `https://your-app-name.ondigitalocean.app`

### Method 2: Using doctl CLI

1. **Install doctl:**

   ```bash
   # macOS
   brew install doctl
   ```

2. **Authenticate:**

   ```bash
   doctl auth init
   ```

3. **Create app spec file** (optional - App Platform can auto-detect):

   ```yaml
   name: friendly-hello-world
   services:
     - name: web
       source_dir: /
       github:
         repo: yourusername/your-repo-name
         branch: main
       run_command: gunicorn deploy_hello_world:app
       environment_slug: python
       instance_count: 1
       instance_size_slug: basic-xxs
       http_port: 8080
   ```

4. **Deploy:**
   ```bash
   doctl apps create --spec app-spec.yaml
   ```

## 🎯 What Makes This App DigitalOcean-Ready

- **Environment Variables:** Uses `PORT` environment variable (DigitalOcean provides this)
- **Health Check:** `/api/health` endpoint for monitoring
- **Production Server:** Configured to use Gunicorn
- **Minimal Dependencies:** Only Flask and Gunicorn for fast builds
- **Error Handling:** Custom 404 pages and error handling

## 📁 Files Structure

```
lab_5/
├── deploy_hello_world.py  # Main Flask application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔧 Environment Variables

The app automatically uses these environment variables:

- `PORT`: Set by DigitalOcean (defaults to 5000 locally)

## 💡 Tips for DigitalOcean Deployment

1. **Keep it simple:** This app uses minimal dependencies for faster builds
2. **Use health checks:** The `/api/health` endpoint helps with monitoring
3. **Environment variables:** DigitalOcean automatically sets `PORT`
4. **Static files:** For production apps, consider using DigitalOcean Spaces for static assets
5. **Scaling:** Start with basic-xxs instance and scale up as needed

## 🆘 Troubleshooting

**Build fails?**

- Check that `requirements.txt` is in the root directory
- Ensure Python version compatibility (app works with Python 3.7+)

**App won't start?**

- Verify the run command: `gunicorn deploy_hello_world:app`
- Check logs in DigitalOcean dashboard

**Can't access the app?**

- Make sure the app is running on `0.0.0.0` (it is by default)
- Check that DigitalOcean assigned the correct PORT

---

Happy deploying! 🚀💙
