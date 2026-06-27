# Docker Learning Repository

## Overview

This repository contains a collection of Docker examples designed to help students understand the fundamentals of containerization using Python, FastAPI, Streamlit, and Docker Compose. The examples are structured progressively, starting from a simple Python application and moving towards a multi-container architecture.

The objective of this repository is to provide hands-on experience with Docker concepts such as image creation, container execution, port mapping, service communication, and orchestration using Docker Compose.

---

## Prerequisites

Before running the examples, ensure the following software is installed:

* Docker Desktop
* Python 3.12+ (optional for local execution)
* Git

Verify Docker installation:

```bash
docker --version
docker compose version
```

---

# Application 1: Simple Python Application

## Description

This application demonstrates how to containerize a basic Python script.

### Concepts Covered

* Docker Images
* Docker Containers
* Dockerfile Basics
* Running Python inside a Container

### Components

* Python Script
* Dockerfile

### Build

```bash
docker build -t app_1 ./app_1
```

### Run

```bash
docker run app_1
```

---

# Application 2: FastAPI Backend Application

## Description

This application introduces web applications inside Docker by containerizing a FastAPI backend service.

### Concepts Covered

* REST APIs
* FastAPI
* Exposing Container Ports
* Accessing Applications through a Browser

### Components

* FastAPI Backend
* Dockerfile

### Build

```bash
docker build -t app_2 ./app_2
```

### Run

```bash
docker run -p 8000:8000 app_2
```

### Access

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

# Application 3: FastAPI Backend + Streamlit Frontend (Single Container)

## Description

This application demonstrates how multiple services can run within a single Docker container.

### Concepts Covered

* Frontend and Backend Integration
* Streamlit
* FastAPI
* Multiple Processes in a Container
* Port Mapping

### Components

* FastAPI Backend
* Streamlit Frontend
* Single Dockerfile

### Build

```bash
docker build -t app_3 ./app_3
```

### Run

```bash
docker run -p 8000:8000 -p 8501:8501 app_3
```

### Access

FastAPI Swagger:

```text
http://localhost:8000/docs
```

Streamlit Application:

```text
http://localhost:8501
```

---

# Application 4: FastAPI Backend + Streamlit Frontend using Docker Compose

## Description

This application demonstrates a production-oriented architecture where the frontend and backend are deployed as separate containers and managed using Docker Compose.

### Concepts Covered

* Multi-Container Applications
* Docker Compose
* Service Discovery
* Container Networking
* Microservice Architecture

### Components

* FastAPI Backend Container
* Streamlit Frontend Container
* Docker Compose Configuration

### Run

Navigate to the application directory and execute:

```bash
docker compose up --build
```

### Access

FastAPI Swagger:

```text
http://localhost:8000/docs
```

Streamlit Application:

```text
http://localhost:8501
```

### Stop Services

```bash
docker compose down
```

---

# Learning Path

The applications are designed to be explored in the following order:

1. Application 1 – Basic Python Containerization
2. Application 2 – Containerized Web API using FastAPI
3. Application 3 – Full-Stack Application in a Single Container
4. Application 4 – Multi-Container Architecture using Docker Compose

Following this progression will help learners understand how containerized applications evolve from simple scripts to production-ready distributed systems.

---

# Key Docker Commands

### Build an Image

```bash
docker build -t <image_name> .
```

### Run a Container

```bash
docker run <image_name>
```

### Run with Port Mapping

```bash
docker run -p host_port:container_port <image_name>
```

### List Running Containers

```bash
docker ps
```

### List Docker Images

```bash
docker images
```

### Stop a Container

```bash
docker stop <container_id>
```

### Docker Compose

Start Services:

```bash
docker compose up --build
```

Stop Services:

```bash
docker compose down
```

---

# Conclusion

This repository provides a structured introduction to Docker and containerized application development. By progressing through these examples, learners gain practical experience with Docker fundamentals, web application deployment, frontend-backend communication, and multi-container orchestration using Docker Compose.
