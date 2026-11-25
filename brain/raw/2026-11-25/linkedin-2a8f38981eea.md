---
author: Pratiksha Supekar
fetched_at: '2026-11-25T11:53:20.618392Z'
id: 2a8f38981eea
lane: lead
published: ''
source: linkedin
title: '🚀 Day 18 of 30 Days Java Interview Preparation

  📌 Topic: Advanced Multithreading in Java


  1. What is ExecutorService in J'
url: https://www.linkedin.com/posts/pratiksha-supekar-306a5027b_java-corejava-multithreading-activity-7531323194771709953-CKZ4
---

🚀 Day 18 of 30 Days Java Interview Preparation
📌 Topic: Advanced Multithreading in Java

1. What is ExecutorService in Java?
ExecutorService is an interface in Java that manages thread execution. It helps us execute tasks without manually creating and managing every thread.

2. Why do we use ExecutorService?
Reuses existing threads.
Reduces the overhead of creating threads repeatedly.
Manages multiple tasks efficiently.
Provides better control over thread execution.

3. What is a Thread Pool?
A thread pool is a collection of reusable worker threads that execute submitted tasks.

4. How can we create an ExecutorService?
We can use the Executors factory methods.
Example:
ExecutorService service =     Executors.newFixedThreadPool(3);
This creates a thread pool with three worker threads.

5. What is the difference between execute() and submit()?
execute() accepts a Runnable task and does not return a result.
submit() accepts Runnable or Callable and returns a Future object.

6. What is Callable in Java?
Callable is a functional interface that represents a task that can return a result and throw checked exceptions.
Its method is:
V call() throws Exception;

7. What is the difference between Runnable and Callable?
Runnable uses the run() method.
Callable uses the call() method.
Runnable cannot return a result.
Callable can return a result.
Callable can throw checked exceptions.

8. What is Future in Java?
Future represents the result of an asynchronous task. It allows us to check whether the task is complete and retrieve its result.

9. What is the get() method in Future?
The get() method retrieves the task result. If the task is not completed, the calling thread waits until the result becomes available.

10. What is the difference between shutdown() and shutdownNow()?
shutdown() stops accepting new tasks but allows submitted tasks to finish.
shutdownNow() attempts to stop running tasks, interrupts them, and returns tasks that have not started.

11. What is awaitTermination()?
It makes the calling thread wait for the ExecutorService to terminate, up to the specified time.

12. What is Deadlock in Java?
Deadlock occurs when two or more threads wait forever for locks held by one another.

13. What are the necessary conditions for Deadlock?
Four conditions are required:
Mutual Exclusion
Hold and Wait
No Preemption
Circular Wait

14. How can we prevent Deadlock?
Acquire locks in a consistent order.
Avoid unnecessary nested locks.
Keep synchronized blocks small.
Use timeout-based locking where appropriate.

15. What is the difference between shutdown() and Future.cancel()?
shutdown() stops an executor from accepting new tasks.
Future.cancel(true) attempts to cancel a particular task and may interrupt it if it is running.

💻 Practical Coding Question: Execute a Callable Task Using ExecutorService.

#Java #CoreJava #Multithreading #ExecutorService #Callable #Future #Deadlock #JavaInterviewQuestions #JavaDeveloper #BackendDeveloper #30DaysOfJava
