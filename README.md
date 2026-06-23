# 🚀 Sanjeevani : AI-Powered Self-Healing Kubernetes Platform



Modern cloud-native applications run on Kubernetes, where application failures, pod crashes, configuration issues, and unexpected incidents can impact service availability.

This project is an **AI-Powered Self-Healing Kubernetes Platform** that automatically detects application failures, collects logs, performs AI-driven Root Cause Analysis (RCA), generates incident reports, and executes automated remediation actions.

The platform combines **Kubernetes, Observability, Incident Management, Site Reliability Engineering (SRE) principles, and Generative AI** to reduce Mean Time To Detection (MTTD) and Mean Time To Recovery (MTTR).

---

## Problem Statement

In traditional environments, when an application crashes:

1. Engineers manually detect the failure.
2. Logs are collected manually.
3. Root Cause Analysis is performed manually.
4. Incident reports are written manually.
5. Recovery actions are executed manually.

This process increases downtime and operational overhead.

This platform automates the entire workflow.

---

## Project Architecture

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/eb377089-ee71-4135-8a8e-2e9c993c31ab" />


---

## Key Features

### 🔍 Incident Detection

* Continuous Kubernetes pod monitoring
* Restart count tracking
* CrashLoopBackOff detection
* Automated incident identification

### 📊 Observability

* Kubernetes API integration
* Log collection from failed pods
* Health monitoring
* Failure visibility

### 🤖 AI-Powered Root Cause Analysis

* Automatic log analysis using Gemini AI
* Incident severity assessment
* Impact analysis
* Recommended remediation actions
* Confidence scoring

### 📝 Incident Management

* Automatic incident report generation
* Timestamped report storage
* Persistent incident history
* RCA documentation

### 🔄 Self-Healing Automation

* Automatic deployment restart
* Recovery workflow execution
* Reduced Mean Time To Recovery (MTTR)

### 🔐 Secure Kubernetes Access

* Service Accounts
* Role-Based Access Control (RBAC)
* Least Privilege Principle

---

## SRE Concepts Demonstrated

This project showcases practical implementation of:

* Site Reliability Engineering (SRE)
* Incident Management
* Observability
* Root Cause Analysis (RCA)
* Self-Healing Infrastructure
* Kubernetes Operations
* Monitoring & Alerting
* Automated Remediation
* Reliability Engineering
* Failure Recovery Automation

---

## Tech Stack

### Infrastructure

* Kubernetes (Kind)
* Docker
* Linux

### Monitoring & Reliability

* Prometheus
* Alertmanager

### Backend

* Python
* Kubernetes Python Client

### AI Layer

* Google Gemini AI

### Storage

* Kubernetes Persistent Volume
* Persistent Volume Claim (PVC)

### Security

* Kubernetes RBAC
* Service Accounts

---

# ⚙️ How It Works

## Step 1: Application Failure

An application enters a failed state.

### Example

```http
GET /fail
```

The health endpoint starts returning:

```http
500 Internal Server Error
```

As a result, the application becomes unhealthy.

---

## Step 2: Kubernetes Self-Healing

Kubernetes continuously monitors pod health using **Liveness Probes**.

When a liveness probe fails, Kubernetes automatically:

```text
Failed Pod
     ↓
Pod Terminated
     ↓
New Pod Created
```

This is Kubernetes' built-in **self-healing mechanism**.

---

## Step 3: Incident Detection

The AI Analyzer continuously monitors all pods running in the cluster.

Every **30 seconds**, it checks for pod restarts:

```python
restart_count > previous_restart_count
```

If the restart count increases:

```text
🚨 Incident Detected
```

An incident workflow is automatically triggered.

---

## Step 4: Log Collection

Once an incident is detected, the analyzer automatically collects:

* Previous container logs
* Last 50 log entries
* Pod metadata
* Namespace information

Using:

```python
read_namespaced_pod_log(
    previous=True
)
```

These logs provide context about the failure before the pod restart occurred.

---

## Step 5: AI Root Cause Analysis

The collected logs are sent to **Google Gemini AI** for analysis.

Gemini generates:

* Root Cause Analysis (RCA)
* Severity Assessment
* Impact Analysis
* Recommended Fixes
* Confidence Score

### Example Output

```text
Root Cause:
NullPointerException in payment-service

Severity:
High

Impact:
Service unavailable

Recommended Fix:
Add null validation before processing request

Confidence:
92%
```

---

## Step 6: Incident Report Generation

A complete incident report is automatically generated and stored.

### Example

```text
/reports/incident-20260621-173915.txt
```

Each report contains:

* Incident Timestamp
* Namespace Information
* Pod Details
* Failure Logs
* AI Analysis
* Recovery Actions
* Remediation Status

This creates a searchable history of production incidents.

---

## Step 7: Automated Remediation

After analysis, the platform automatically performs remediation actions.

Current remediation strategy:

```python
patch_namespaced_deployment()
```

Which triggers:

```text
Deployment Rollout Restart
```


---

## 🔄 Incident Lifecycle
```text 
Application Failure
        ↓
Kubernetes Detects Failure
        ↓
Pod Restart
        ↓
AI Analyzer Detects Incident
        ↓
Collect Logs
        ↓
Gemini RCA
        ↓
Generate Report
        ↓
Store Report
        ↓
Restart Deployment
        ↓
Application Recovery
```

---

## Screenshots

### Kubernetes Workloads

<img width="2312" height="238" alt="image" src="https://github.com/user-attachments/assets/527c4105-f704-4e27-9f18-8a83aef3fe81" />

### Node Endpoint Failure
<img width="1090" height="132" alt="image" src="https://github.com/user-attachments/assets/65db72a0-edbf-4e4f-aeac-39b497e1ffcd" />

### AI Incident Report

<img width="2864" height="1682" alt="image" src="https://github.com/user-attachments/assets/81158b7e-b4d1-4f5f-bcca-a111eaa1023a" />

<img width="2868" height="916" alt="image" src="https://github.com/user-attachments/assets/bb45bfcb-ae27-49af-b506-279acc222719" />



### Self-Healing Execution

<img width="1836" height="966" alt="image" src="https://github.com/user-attachments/assets/8f62ea64-6031-4478-9a41-dc34778f3fc6" />


### Incident Storage

<img width="2824" height="210" alt="image" src="https://github.com/user-attachments/assets/c890dc09-a9be-4aee-bb0e-b08a31b2aaec" />

<img width="2872" height="1428" alt="image" src="https://github.com/user-attachments/assets/8281eb9a-3a90-476e-bc19-8c0f04a846a6" />



---

# 🔍 Kubernetes vs AI-Powered Self-Healing Platform

| Capability                | Kubernetes | AI-Powered Self-Healing Platform |
| ------------------------- | ---------- | -------------------------------- |
| Detect Pod Failure        | ✅          | ✅                                |
| Restart Failed Pod        | ✅          | ✅                                |
| Collect Failure Logs      | ❌          | ✅                                |
| Root Cause Analysis (RCA) | ❌          | ✅                                |
| AI-Powered Investigation  | ❌          | ✅                                |
| Severity Assessment       | ❌          | ✅                                |
| Impact Analysis           | ❌          | ✅                                |
| Generate Incident Reports | ❌          | ✅                                |
| Store Incident History    | ❌          | ✅                                |
| Recommend Fixes           | ❌          | ✅                                |
| Automated Remediation     | ❌          | ✅                                |
| Recovery Action Execution | ❌          | ✅                                |

## 🔍 Kubernetes vs AI-Powered Self-Healing Platform

### Kubernetes

✅ Detects failed containers

✅ Restarts unhealthy pods

✅ Maintains the desired state


❌ Identifies the root cause of failures

❌ Analyzes application logs automatically

❌ Generates incident reports

❌ Maintains incident history

❌ Recommends remediation actions

❌ Performs intelligent recovery decisions


---

### AI-Powered Self-Healing Platform

✅ Detects incidents automatically

✅ Collects logs and failure evidence

✅ Performs AI-powered root cause analysis

✅ Assesses severity and business impact

✅ Generates detailed incident reports

✅ Maintains incident history

✅ Recommends remediation actions

✅ Executes automated recovery workflows

---

### Key Difference

**Kubernetes says:**

✅ *"The application failed and has been restarted."*

**The AI Platform answers:**

✅ Why did it fail?

✅ What services were affected?

✅ How severe is the incident?

✅ What is the root cause?

✅ What should be fixed?

✅ What recovery action should be executed?

---

## 📊 SRE Concepts Demonstrated

This project implements real SRE workflows:

✅ Incident Detection

✅ Root Cause Analysis (RCA)

✅ Automated Remediation

✅ Self-Healing Infrastructure

✅ Reliability Engineering

✅ Kubernetes Operations

✅ Incident Documentation

✅ Observability

✅ Failure Recovery

✅ Infrastructure Automation

---


# 🚀 Project Status

## Current Engineering Progress

### Kubernetes Automation Platform

| Feature                                  | Status |
| ---------------------------------------- | ------ |
| Kubernetes Deployment Management         | ✅      |
| Liveness Probes                          | ✅      |
| Readiness Probes                         | ✅      |
| Restart Detection                        | ✅      |
| Log Collection                           | ✅      |
| Gemini-Powered Root Cause Analysis (RCA) | ✅      |
| Incident Report Generation               | ✅      |
| Persistent Storage                       | ✅      |
| Automated Remediation                    | ✅      |
| RBAC Security                            | ✅      |

## Engineering MVP Completion

**95% Complete** 🚀

---

# 🔍 Future Roadmap

## Phase 2: Observability Layer

### Monitoring & Metrics

* Prometheus Integration
* Alertmanager Integration
* Kubernetes Events Correlation
* Metrics Collection & Analysis
* Advanced Decision Engine

### Intelligent Remediation

#### Current Capability

* Restart Deployment

#### Planned Enhancements

| Incident Type    | Automated Action             |
| ---------------- | ---------------------------- |
| OOMKilled        | Increase Memory Allocation   |
| CPU Spike        | Scale Replicas               |
| CrashLoopBackOff | Restart Deployment           |
| Node Failure     | Reschedule Workloads         |
| Memory Leak      | Trigger Remediation Workflow |

---

# 🎯 Product Features

### Platform Features

* React Dashboard
* REST API
* Incident Analytics
* Incident Search
* Multi-Cluster Support

### Integrations

* Slack Notifications
* Email Alerts
* Grafana Integration

### AI Capabilities

* Gemini-Powered Root Cause Analysis (RCA)
* AI-Generated Incident Reports
* AI Runbook Generation


---
## 🌟 Product Vision

This project currently operates as a Kubernetes-native MVP.

The long-term goal is to evolve it into a production-ready platform that can be installed on any Kubernetes cluster using:

```helm install sanjeevani```

Organizations would be able to:

Connect Kubernetes clusters
Detect incidents automatically
Generate AI-powered RCA reports
Track incident history
Execute automated recovery workflows
Reduce downtime
Improve service reliability

---

## Learning Outcomes

Through this project I gained hands-on experience in:

* Kubernetes Administration
* Reliability Engineering
* Incident Response Workflows
* Monitoring and Observability
* AI-Assisted Operations (AIOps)
* Root Cause Analysis
* Infrastructure Automation
* Kubernetes Security (RBAC)
* Persistent Storage Management
* Self-Healing System Design

---

## 👨‍💻 Author

Shashank Sanmukh Kanade

Computer Engineering Student

Cloud Computing • DevOps • SRE • Kubernetes • Automation • AIOps
