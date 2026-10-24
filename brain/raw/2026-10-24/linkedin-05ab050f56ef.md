---
author: Riyaz Basha
fetched_at: '2026-10-24T07:44:30.186140Z'
id: 05ab050f56ef
lane: lead
published: ''
source: linkedin
title: 'Kubernetes Tip: Your Deployment has 3 replicas. But are you really protected
  during maintenance? 🤔


  We use Deployments a'
url: https://www.linkedin.com/posts/riyaz-basha-cloudops_kubernetes-tip-your-deployment-has-3-replicas-activity-7519648229681053696-bKoi
---

Kubernetes Tip: Your Deployment has 3 replicas. But are you really protected during maintenance? 🤔

We use Deployments and ReplicaSets to maintain the desired number of Pods and improve application availability.
But there’s one important question:
What happens when we need to drain a node or upgrade an AKS cluster?
This is where a PodDisruptionBudget (PDB) comes into the picture.
Let’s take a simple example. 👇
Imagine an application running with 3 replicas.
✅ A Deployment manages the desired state.
✅ A ReplicaSet ensures the desired number of Pods is maintained.
🛡️ A PDB helps protect application availability during supported voluntary disruptions.
What exactly is a voluntary disruption?
It’s a planned action that may interrupt running Pods, such as:
• Draining a node for maintenance
• Upgrading an AKS node pool
• Removing a node from the cluster
• Manually evicting a Pod
How does a PDB help?
Suppose we configure:
minAvailable: 2
This tells Kubernetes that at least 2 selected Pods must remain healthy during voluntary disruptions covered by the budget.
If all 3 Pods are healthy, Kubernetes can allow one Pod to be evicted. A further eviction that violates the budget will be blocked until the budget allows it again.
Without a PDB, there is no PDB-based limit on these evictions. Depending on Pod placement and the operation, maintenance could disrupt more replicas than expected.
One important point to remember ⚠️
A PDB does not prevent every outage. It does not protect against involuntary disruptions such as a sudden node failure.
Also, PDBs do not distribute Pods across nodes or availability zones. For that, we need to understand Pod Topology Spread Constraints and Pod Anti-Affinity.
Here’s how I remember the difference:
🔹 Deployment — Manages application releases and desired replicas
🔹 ReplicaSet — Maintains the desired number of Pods
🔹 HPA — Scales replicas based on metrics
🔹 PDB — Limits supported voluntary disruptions
🔹 Topology Spread Constraints — Help distribute Pods across nodes or zones
These Kubernetes features solve different problems, and understanding how they work together is essential when operating production workloads.

#Kubernetes #K8s #Azure #AKS #DevOps #CloudOps #CloudEngineering #Docker #Terraform #PlatformEngineering #Containerization #DevOpsEngineer #AzureDevOps #KubernetesArchitecture
