# Serverless Architecture with Open-Source Tools

## Project Overview
This project demonstrates the creation of a **serverless architecture** using open-source tools. The architecture includes an API Gateway, serverless functions, and object storage, utilizing the following technologies:

- 🚀 **Apache APISIX**: API Gateway to manage and expose serverless functions.

- ⚙️ **Knative**: Function-as-a-Service (FaaS) platform for deploying and managing serverless functions.

- 🗄️ **MinIO**: Serverless object storage for storing processed images.

- 🐳 **Docker**: Containerization of services.

- 📦 **Docker Compose**: Orchestration of multiple services.


This project was initially designed to use OpenFaaS but transitioned to Knative due to issues with the OpenFaaS repository.

---

## Lab Objectives


1. 🎯 **Setup a serverless environment** using open-source tools.

2. 🖼️ **Process images** with serverless functions.

3. 🔀 **Route API requests** through an API Gateway.

4. 💾 **Store processed images** in a serverless object storage solution.

5. ✅ **Test the workflow** end-to-end.

---

## Tools Used


- 🚀 **Apache APISIX** (API Gateway)

- ⚙️ **Knative** (FaaS)

- 🗄️ **MinIO** (Object Storage)

- 🐳 **Docker & Docker Compose**

---


## Setup Instructions


### 1. Environment Setup


1. 🛠️ **Project Initialization**:
   ```bash
   mkdir serverless-architecture-lab
   cd serverless-architecture-lab
   ```


2. 📝 **Create `docker-compose.yml`**:
   Configure services for:
   - Apache APISIX
   - Knative
   - MinIO


3. ▶️ **Start Services**:
   ```bash
   docker-compose up -d
   ```

4. 🔍 **Verify Services**:
   - Check dashboards/logs for APISIX, MinIO, and Knative.

### 2. Deploy Knative

1. 📥 **Install Knative CLI**:
   ```bash
   curl -L -O https://github.com/knative/client/releases/download/vX.Y.Z/kn
   chmod +x kn
   sudo mv kn /usr/local/bin
   ```

2. 🛠️ **Verify Installation**:
   ```bash
   kn version
   ```

3. ⚡ **Configure Minikube for Knative**:
   ```bash
   minikube start --cpus=2 --memory=2048
   ```

4. 🔄 **Install Knative Serving & Eventing components**:
   ```bash
   kubectl apply -f https://github.com/knative/serving/releases/download/vX.Y.Z/serving-crds.yaml
   kubectl apply -f https://github.com/knative/serving/releases/download/vX.Y.Z/serving-core.yaml
   ```

5. 🖼️ **Deploy a serverless function for image processing**.


### 3. Configure Apache APISIX

1. 🖥️ **Access the APISIX dashboard**.

2. ➕ **Create a new route**:

   - **Route Path**: `/process-image`

   - **Backend Service**: Knative function endpoint.

3. 🛠️ **Test the route** using `curl` or Postman.


### 4. Configure MinIO


1. 🖥️ **Access the MinIO dashboard**.

2. 🪣 **Create a bucket** for storing processed images.

3. 🔗 **Update the serverless function** to save processed images to MinIO using the **MinIO Python SDK**.

---

## Workflow

1. 📤 **Send an image** to the `/process-image` endpoint via the API Gateway.

2. ⚙️ **Knative processes** the image (e.g., resizing or format conversion).

3. 🗄️ **Processed image** is stored in MinIO.

4. ✅ **Verify** the image storage in the designated MinIO bucket.

---

## Challenges Faced

1. ❌ **OpenFaaS Repository Issues**:
   - OpenFaaS repository was temporarily down, leading to a switch to Knative.
   
2. ⚠️ **Port Conflicts**:
   - APISIX and MinIO default ports conflicted. Resolved by reconfiguring the MinIO port.

3. 🖥️ **Virtual Machine Configuration**:
   - Minikube required a minimum of 2 CPUs. Adjusted VM configurations accordingly.

4. 🌐 **Inconsistent Internet Connectivity**:
   - Affected pulling of Docker images and applying Kubernetes manifests. Mitigated by working offline where possible.

---

## Results


- ✅ **Functional serverless architecture** deployed.

- 🖼️ **Processed images** successfully routed through APISIX, processed by Knative, and stored in MinIO.

---

## How to Test

1. 📤 **Send an Image**:
   ```bash
   curl -X POST -F "file=@<image_path>" http://<APISIX_URL>/process-image
   ```

2. 🗄️ **Verify in MinIO**:
   - Check the specified bucket for the processed image.

---

## Cleanup

1. ⛔ **Stop Services**:
   ```bash
   docker-compose down
   ```

2. 🗑️ **Remove unused Docker resources**:
   ```bash
   docker system prune -a
   ```

---

## Future Improvements

1. ⚙️ **Improve Port Configuration**:
   - Avoid port conflicts by dynamically assigning ports.

2. ➕ **Expand Functionality**:
   - Add more serverless functions for other image processing tasks.

3. 🧪 **Enhance Testing**:
   - Implement automated tests for end-to-end workflow validation.

---

## Author

**Donfack Tsopfack Yves Dylane**

---

## Resources

- 📚 [Apache APISIX Documentation](https://apisix.apache.org/)
- 📚 [Knative Documentation](https://knative.dev/)
- 📚 [MinIO Documentation](https://min.io/)
- 📚 [Docker Documentation](https://www.docker.com/)

