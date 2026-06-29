# DevOps Containerized Python App

## Project Overview

This project is a simple Python web application used to learn containerization and Kubernetes fundamentals.

The application runs inside containers and is deployed to a Kubernetes cluster. During the project, concepts such as Deployments, Pods, ConfigMaps, Secrets, scaling, updates, rollbacks, and debugging were explored.

---

## Technologies Used

* Python
* Docker
* Kubernetes
* Minikube
* kubectl

---

## Architecture

### Application Flow

User Request
→ Kubernetes Cluster
→ Pod
→ Python Application
→ Response Returned

The Python application listens on port 8000 and serves HTTP responses.

### Kubernetes Components

**Deployment**

* Maintains the desired application state.
* Configured to run 3 pod replicas.

**Pods**

* Execute the application containers.
* Automatically recreated if they fail.

**ConfigMap**

* Stores non-sensitive configuration values.
* Allows configuration changes without modifying application code.

**Secret**

* Stores sensitive values separately from application configuration.

---

## Running the Project

Start the Kubernetes cluster:

```bash
minikube start
```

Apply the Kubernetes resources:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
```

Verify the deployment:

```bash
kubectl get pods
kubectl get deployments
kubectl get endpoints
```

---

## Troubleshooting Commands

```bash
kubectl get all
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl get endpoints
```

These commands were used throughout the project to investigate deployment, networking, and application issues.

---

## What I Learned

* Container lifecycle management
* Docker image creation
* Container networking concepts
* Kubernetes Deployments and Pods
* Scaling workloads
* Rolling updates and rollbacks
* Configuration management using ConfigMaps
* Secret management
* Kubernetes troubleshooting and debugging techniques

