---
author: Nikhil Ganorkar
fetched_at: '2026-09-19T07:39:07.777721Z'
id: 1b151fa4396e
lane: lead
published: ''
source: linkedin
title: '𝗦𝗲𝘁𝘁𝗶𝗻𝗴 𝗨𝗽 𝗞𝘂𝗯𝗲𝗿𝗻𝗲𝘁𝗲𝘀 𝗜𝘀 𝗡𝗼𝘁 𝗝𝘂𝘀𝘁 𝘬𝘶𝘣𝘦𝘢𝘥𝘮 𝘪𝘯𝘪𝘵


  When setting up Kubernetes outside a managed service like EKS, AKS, or G'
url: https://www.linkedin.com/posts/nikhil-ganorkar-48351a191_kubernetes-kubespray-rke2-activity-7506968406424780800-jpBZ
---

𝗦𝗲𝘁𝘁𝗶𝗻𝗴 𝗨𝗽 𝗞𝘂𝗯𝗲𝗿𝗻𝗲𝘁𝗲𝘀 𝗜𝘀 𝗡𝗼𝘁 𝗝𝘂𝘀𝘁 𝘬𝘶𝘣𝘦𝘢𝘥𝘮 𝘪𝘯𝘪𝘵

When setting up Kubernetes outside a managed service like EKS, AKS, or GKE, one of the first questions is:

How do we want to provision and operate the cluster?
There are several approaches.

𝟭. 𝗸𝘂𝗯𝗲𝗮𝗱𝗺
A more hands-on approach where you bootstrap Kubernetes components yourself.

You get a much better understanding of:
 • Control-plane bootstrap
 • Worker node joining
 • Certificates
 • etcd
 • CNI
 • Cluster lifecycle

But you also own more of the operational work.

𝟮. 𝗞𝘂𝗯𝗲𝘀𝗽𝗿𝗮𝘆
Kubespray uses Ansible to automate multi-node Kubernetes provisioning.

Inventory
  ↓
Ansible
  ↓
OS + Container Runtime
  ↓
Control Plane + Workers
  ↓
etcd + CNI + Kubernetes

This becomes useful when you want a repeatable cluster build across multiple machines.

𝟯. 𝗥𝗞𝗘𝟮
RKE2 takes a more opinionated approach to Kubernetes.

Instead of assembling every component manually, the distribution packages and manages many of the required pieces for you.

That changes the operational model and the decisions you need to make around configuration, upgrades, security, and lifecycle management.

The interesting part isn't:
“Which one can create a Kubernetes cluster?”

They all can.

The better questions are:
 1. How do we upgrade it?
 2. How do we handle etcd?
 3. How are certificates managed?
 4. How is networking configured?
 5. What happens when a control-plane node fails?
 6. Can we reproduce the same cluster reliably?
 7. How much of the lifecycle does the platform team own?

That's where Kubernetes setup starts becoming platform engineering.

For me, the goal isn't just:
𝘬𝘶𝘣𝘦𝘤𝘵𝘭 𝘨𝘦𝘵 𝘯𝘰𝘥𝘦𝘴

and seeing:
STATUS
Ready

The real goal is understanding how to build, operate, upgrade, troubleshoot, and recover the cluster.

I'm currently exploring this path:

Bare VMs → Kubespray / RKE2 → Multi-node Kubernetes → Networking → HA → Upgrades → Failure testing

The cluster being created is only the beginning.
The real engineering starts after Ready.

#Kubernetes #Kubespray #RKE2 #DevOps #SRE #PlatformEngineering #CloudNative #Infrastructure
