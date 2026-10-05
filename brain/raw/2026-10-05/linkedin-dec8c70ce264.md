---
author: Shraddha Wankhade
fetched_at: '2026-10-05T09:48:27.497221Z'
id: dec8c70ce264
lane: lead
published: ''
source: linkedin
title: '🚀 Day 86 of #90DaysOfDevOps — End-to-End GitOps CI/CD


  Today I completed one of the most important stages of my DevOps j'
url: https://www.linkedin.com/posts/shraddha-wankhade-ba45293b4_90daysofdevops-90daysofdevops-devops-activity-7512801561660764160-8qs-
---

🚀 Day 86 of #90DaysOfDevOps — End-to-End GitOps CI/CD

Today I completed one of the most important stages of my DevOps journey: building and validating a complete CI/CD + GitOps deployment workflow on AWS EKS.

🔄 What I implemented:

Developer → GitHub → GitHub Actions → DockerHub → GitOps Repository → Argo CD → AWS EKS

🛠️ Key technologies used
☁️ AWS EKS
🔧 GitHub Actions
🐳 Docker amp; DockerHub
🚀 Argo CD
☸️ Kubernetes
🌱 GitOps
🔐 cert-manager amp; TLS
🌐 Gateway API
🏗️ Terraform

✅ What I completed

• Automated Docker image build and push using GitHub Actions
• Updated Kubernetes manifests with the new image version
• Implemented GitOps-based deployment using Argo CD
• Configured Argo CD automated sync, pruning and self-healing
• Deployed the application successfully on EKS
• Verified Kubernetes rollout and application health
• Tested Argo CD self-healing by manually changing the replica count
• Troubleshot TLS/certificate issues with cert-manager
• Resolved GitOps synchronization and deployment issues

🔥 One important lesson

GitOps isnt simply about installing Argo CD.

The real learning came from troubleshooting the complete chain:

Code → CI → Container Image → Git Change → Argo CD → Kubernetes → Application

When something breaks, understanding where the failure occurs in this chain makes troubleshooting much easier.💡 Interview takeaway

A strong DevOps engineer should not only know how to deploy an application, but also understand:

How do we automate it?
How do we make deployments reproducible?
How do we detect drift?
How do we recover automatically?
How do we troubleshoot failures?

Day 86 gave me practical experience with all of these.

One more step closer to becoming a DevOps Engineer.

 🚀#90DaysOfDevOps #DevOps #GitOps #ArgoCD #Kubernetes #AWS #EKS #GitHubActions #Docker #Terraform #CICD #CloudDevOps #DevOpsLearning
