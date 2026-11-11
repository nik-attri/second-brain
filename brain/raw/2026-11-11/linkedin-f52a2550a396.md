---
author: Bindu Sri Gudelli
fetched_at: '2026-11-11T10:00:42.067351Z'
id: f52a2550a396
lane: lead
published: ''
source: linkedin
title: '☕ Garbage Collection in Java – How Does JVM Identify and Reclaim Unreachable
  Objects?

  Have you ever wondered what happen'
url: https://www.linkedin.com/posts/activity-7526216967964483584-Xytg
---

☕ Garbage Collection in Java – How Does JVM Identify and Reclaim Unreachable Objects?
Have you ever wondered what happens to objects after we stop using them in Java?
Do we need to manually delete objects to free memory?
No! Java provides automatic memory management through Garbage Collection (GC).
But how does the JVM actually identify which objects can be removed?
Let's understand the internal working. 👇
1️⃣ What is Garbage Collection?
Garbage Collection is an automatic memory management mechanism in Java that reclaims heap memory occupied by objects that are no longer reachable.
Instead of manually freeing object memory, the JVM manages this process.
2️⃣ How Does Garbage Collection Work Internally?
A simplified explanation of the Mark-and-Sweep approach:
Step 1: Identify GC Roots
The JVM starts from GC Roots, such as:
References in active thread stacks.
Static references.
Other JVM-defined root references.
Step 2: Mark Reachable Objects
The garbage collector follows references from GC Roots and identifies reachable objects.
Step 3: Identify Unreachable Objects
Objects that cannot be reached from GC Roots are considered garbage.
Step 4: Reclaim Memory
The collector reclaims memory occupied by eligible objects.
Some collectors also compact memory to reduce fragmentation.
3️⃣ Practical Java Example
class Employee {     
     int id = 101; 
   }  
public class GCDemo {    
     public static void main(String[] args) {         
            Employee emp = new Employee();
            System.out.println(emp.id);          
            emp = null;          // Employee object is now         // eligible for Garbage Collection.     } }
What happens here?
An Employee object is created in the heap.
emp references that object.
We assign null to emp.
If no other reachable reference points to the object, it becomes eligible for GC.
Important: Eligible for GC does not mean immediately deleted.
4️⃣ JVM Heap Generations
Many commonly used JVM garbage collectors organize the heap using generations.
Young Generation
Eden Space
Survivor Space (S0 and S1)
Newly allocated objects typically start in Eden.
Objects that survive collection may move between Survivor spaces and eventually be promoted to the Old Generation.
Old Generation
Typically contains longer-lived objects.
This generational approach is based on the observation that many objects have short lifetimes.
5️⃣ Types of Garbage Collection
Some commonly discussed GC terms:
Minor GC: Traditionally refers to collection of the Young Generation.
Major GC: Often used to describe Old Generation collection, although its exact meaning varies by JVM and collector.
Full GC: A broader collection involving the entire heap and sometimes additional memory areas.
Modern collectors such as G1 and ZGC have different collection strategies, so these terms should not be treated as universal implementation rules.
6️⃣ Two Real-World Examples
Example 1: E-commerce Application
A user searches for products.
The application creates temporary objects to process search results.
When these objects are no longer reachable, the JVM can reclaim their memory.
Example 2: Banking Application
A transaction-processing service creates temporary calculation objects.
After processing completes, objects that are no longer referenced become eligible for Garbage Collection.
7️⃣ Important Interview Questions
Can we force Garbage Collection in Java?
What is the difference between Minor GC and Full GC?
What are GC Roots?
Can an unreachable object become reachable again?
What happens if an application creates too many objects?
What is the difference between Memory Leak and OutOfMemoryError?
8️⃣ Important Points to Remember
Java automatically manages heap memory.
GC identifies unreachable objects.
System.gc() only requests garbage collection; it does not guarantee execution.
Garbage Collection does not guarantee immediate object destruction.
Finalization is deprecated and should not be used for resource management.
Use try-with-resources for resources such as files and database connections.
💡 Final takeaway:
Garbage Collection helps Java developers focus on application logic instead of manually managing object memory.
But understanding how GC works is essential for writing memory-efficient and high-performance applications.
💬 Interview question:
What is the difference between an object being eligible for Garbage Collection and actually being garbage collected?
Share your answer in the comments! 👇
#Java #CoreJava #JVM #GarbageCollection #MemoryManagement #JavaDeveloper #Programming #TechnicalInterview #SoftwareEngineering
