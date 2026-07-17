# DevOps Containerized Python Application

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestrated-326CE5)
![License](https://img.shields.io/badge/License-MIT-green)

## Project Overview

This project is a lightweight, containerized Python HTTP application deployed on Kubernetes using configuration management, resource limits, rolling updates, and health probes.

Its purpose is to showcase DevOps and Kubernetes fundamentals along with production-oriented practices.

The application is intentionally simple so the focus remains on infrastructure and operational practices.

---

## Architecture

### System Flow

```text
User Request
      |
      v
Kubernetes Service
      |
      v
Service selects Pods using labels
      |
      v
Deployment manages Pod replicas
      |
      v
Pods running containers
      |
      v
Python HTTP Application
```

### Configuration Flow

```text
ConfigMap          Secret
     |                |
     |                |
     v                v
Environment variables injected into containers
```

The application is deployed using a Kubernetes Deployment that maintains three replicas of the Python application. A Kubernetes Service provides network access and routes traffic to healthy Pods using label selectors. Configuration is separated from the application code using ConfigMaps for non-sensitive values and Secrets for sensitive values, both injected into the containers as environment variables.

---

## Features Demonstrated

- Containerized Python application
- Kubernetes Deployment with three replicas
- Service-based networking
- Configuration management using ConfigMaps
- Secret management
- Resource requests and limits
- Startup, readiness, and liveness probes
- Rolling updates
- Kubernetes troubleshooting

---

## Technology Stack

- **Python** – Implements the HTTP application.
- **Docker** – Packages the application into a portable container image.
- **Kubernetes** – Orchestrates deployment, scaling, and recovery of the application.
- **Minikube** – Provides a local Kubernetes cluster for development and testing.
- **kubectl** – Manages and troubleshoots Kubernetes resources.
- **Git** – Tracks version history throughout development.

---

## Repository Structure

```text
.
├── app.py
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── configmap.yaml
├── secret.yaml
├── docker-compose.yml
├── values.yaml
├── .gitignore
└── README.md
```

---

## How to Run the Project

### Prerequisites

- Docker
- Minikube
- kubectl

### Build the Docker image

```bash
docker build -t devops-app:latest .
```

### Load the image into Minikube

```bash
minikube image load devops-app:latest
```

### Apply the Kubernetes manifests

```bash
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Verify the deployment

```bash
kubectl get pods
kubectl get svc
kubectl get endpoints
```

### Access the application

```bash
kubectl port-forward service/devops-app-service 8000:80
```

In another terminal:

```bash
curl http://localhost:8000
```

Expected output:

```text
Hello DevOps
Mode: dev
Log level: info
Password loaded successfully
```

---

## Troubleshooting

Useful commands when investigating deployment or application issues:

- `kubectl get pods` — Check Pod status, readiness, and names.
- `kubectl describe pod <pod-name>` — Inspect Pod configuration, conditions, and recent events.
- `kubectl logs <pod-name>` — View application output and runtime logs.
- `kubectl get endpoints` — Verify that the Service has healthy backend Pods available.
- `kubectl describe deployment devops-app` — Inspect Deployment status, rollout progress, and ReplicaSets.

---

## Engineering Concepts Practiced

- Container lifecycle management
- Kubernetes reconciliation and desired state
- Configuration management with ConfigMaps
- Secret management
- Resource requests and limits
- Startup, readiness, and liveness probes
- Rolling updates and application availability
- Kubernetes networking using Services and label selectors
- Systematic Kubernetes troubleshooting
