# End-to-End MLOps Pipeline on Kubernetes

An enterprise-grade, end-to-end Machine Learning Operations (MLOps) pipeline designed to train, containerize, version, and deploy a machine learning model using **FastAPI**, **MLflow**, **Docker**, **Kubernetes (Minikube)**, and **GitHub Actions**.

---

## 🎯 Project Aim
The primary goal of this project is to automate and standardize the complete machine learning lifecycle—from data preprocessing and model tracking to containerized cloud-native deployment and automated CI/CD integration. This eliminates the "it works on my machine" barrier and ensures reproducible, scalable model serving.

---

## 🛠️ Tech Stack & Architecture

* **Machine Learning & Tracking:** Scikit-Learn, MLflow (Model Registry & Tracking)
* **Backend API:** FastAPI, Uvicorn
* **Containerization:** Docker (Optimized Python 3.12-slim base image)
* **Orchestration:** Kubernetes (Minikube deployments, services, and rolling updates)
* **CI/CD Automation:** GitHub Actions (Automated building and pushing to Docker Hub)

---

## 📁 Project Directory Structure

```text
End-to-End MLOps Pipeline/
├── .github/
│   └── workflows/
│       └── mlops.yml       # Automated GitHub Actions CI pipeline
├── k8s/
│   ├── deployment.yaml     # Kubernetes Deployment manifest
│   └── service.yaml        # Kubernetes Service load balancer manifest
├── src/
│   ├── app.py              # FastAPI inference application
│   └── train.py            # Model training and MLflow logging script
├── .gitignore              # Excluded artifacts, caches, and virtual environments
├── Dockerfile              # Container build instructions
├── requirements.txt        # Pinned Python dependencies
└── mlflow.db               # Local SQLite backend for MLflow tracking
```

---

## 🚀 Getting Started & Local Setup

### 1. Clone the Repository
```powershell
git clone https://github.com/mrsid743/End-to-End-MLOps-Pipeline.git
cd End-to-End-MLOps-Pipeline
```

### 2. Set Up Virtual Environment & Dependencies
```powershell
python -m venv venv
venv\Scripts\Activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Train and Register the Model
Run the training script to log metrics and register the model via MLflow:
```powershell
python src/train.py
```

---

## 🐳 Running Locally with Docker

1. **Build the Docker Image:**
   ```powershell
   docker build -t mrsid743/ml-model:latest .
   ```
2. **Run the Container Locally:**
   ```powershell
   docker run -p 8000:8000 mrsid743/ml-model:latest
   ```

---

## ☸️ Deploying to Kubernetes (Minikube)

1. **Start Minikube:**
   ```powershell
   minikube start
   ```
2. **Load Image into Minikube:**
   ```powershell
   minikube image load mrsid743/ml-model:latest
   ```
3. **Apply Kubernetes Manifests:**
   ```powershell
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```
4. **Access the Service:**
   ```powershell
   minikube service ml-model-service
   ```
   *(Append `/docs` to the generated URL to interact with the interactive Swagger UI).*

---

## 🔄 CI/CD Automation (GitHub Actions)
The project includes an automated GitHub Actions pipeline (`.github/workflows/mlops.yml`) that triggers on every push to the `main` branch. It runs dependency validation, logs into Docker Hub via secure repository secrets, and builds/pushes optimized container images automatically.
