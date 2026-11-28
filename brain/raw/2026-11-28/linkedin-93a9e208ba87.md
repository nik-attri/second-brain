---
author: Jaya Suriya
fetched_at: '2026-11-28T11:07:15.084005Z'
id: 93a9e208ba87
lane: lead
published: ''
source: linkedin
title: "Have you ever run \n\n Kubectl delete namespace demo\n\nand watched it sit\
  \ in #Terminating Forever?\n\nMy first thought used t"
url: https://www.linkedin.com/posts/activity-7532384126667030528-Hhfe
---

Have you ever run 

 Kubectl delete namespace demo

and watched it sit in #Terminating Forever?

My first thought used to be: 

 "K8 is broken"

But in Reality is much more Interesting.

#Finalizers 

A Finalizers is K8 way of saying

 "Hold on.Before I delete the resource , I need to clean up everything associated with it."

Delete Request -> Finalizer Found -> Cleanup happens -> Finalizer Removed -> Resources Deleted.

Why Does K8 Do this?

Imagine Deleting 

 LB service, PVC, Namespace , An ArgoCD or Crossplane Resource

Before removing the K8 object K8 ensures dependent Resources are cleaned up properly. 

Without Finalizers, You could end up with: 

Orphaned LB (Load Balancers), Unused PVC'S, Stale DNS Records, Unexpected Cloud Costs, External infrastructure still Running..

#BenefitsofFinalizers

Prevent Orphaned Resources

Protect Production Workloads

Maintain data integrity

Enable Automated Cleanup

Reduce Cloud Costs

Improve the Operational Reliability 

#Example

 metadata:
    finalizers:
         - https://lnkd.in/g7-GqFM6

As long as Finalizers exists K8 won't remove the objects.

#TheCatch

If the controller responsible for Cleanup crashes is removed or can't complete it's task: 

Resource Status = Terminating

and it may stay there indefinitely.

That's why one of the first things We need to check While delete

Kubectl get <Resource> <name> -o yml

  Can we remove Finalizers Manually?

  #Yes
 
  Kubectl patch <Resource> <name> \
  -p '{"metadata" :{"Finalizers":[]}' \
-- type = merge. 

But this should be #lastResort

#KeyTakeaway

A delete request in K8 doesn't always mean "delete now"

Cleanup first. Delete Later

Finalizers are k8 'Safety net, ensuring that delete doesn't mean leave a mess behind.

#Mylearning

I used to think Kubectl delete instantly removed Resources 

Learning about Finalizers changed my perspective.

Now whenever I see something stuck in #Terminating, I don't start with Force Deletion.

Need to think 

What Cleanup is K8 waiting to finish?

#Question 

What the Most interesting or frustrating Finalizers issues you've encountered in K8's

Have you ever had a Namespaces, PVC, or custom Resources Stuck in Terminating because of Finalizers?

Share your Experience!

#Kubernetes #K8 #Devops #Cloud #CICD #Gitops #Devops #MLOPS #Terraform #Docker #LearninginPublic
