# DevOps Containerized Python App

## What this project does:

This is a simple Python web application containerized using Docker.

It is executed inside a Docker container and managed using Docker Compose.

The application behavior can be modified using environment variables without changing the code or rebuilding the app.

___


## Architecture Overview:

- **Docker Image**
  A Docker image is a blueprint used to create containers.
  It contains the application code and its runtime environment.
  It should only change when the application structure or dependencies change.

- **Docker Container**
  A container is a running instance of a Docker image.
  It executes the application in an isolated environment.

- **Docker Compose**
  Docker Compose is a tool used to define and manage multi-container or structured applications.
  It allows services to be configured using a YAML file and started with a single command.

- **Environment Variables**
  Environment variables are external configuration values passed to the application at runtime.
  They allow changing application behavior without modifying code or rebuilding image.

___


## How to run the project

docker compose up -d --build

Then access:

curl http:// localhost:8080

___

## What I learned

- Difference between image and container
- Container lifecycle and execution
- How Docker networking works (port mapping)
- How configuration is separated from code using environment variables
- How Docker Compose manages application structure
- How to debug containers using logs and execution context

___

## Notes

This project is intentionally simple and used for learning DevOps fundamentals such as containerization, orchestration, and configuration management.
