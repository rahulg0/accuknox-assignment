# ASSIGNMENT


**Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.**

**Answer:** 

By default, django signals are exectuted synchronously. This means when a signal is sent, the signal handler is executed immediately in the same request, which in turn blocks the main thread until it is finished.
Code Snippet: you can find it in -> **./assignment/questions/question1.py**


**Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.**

**Answer:**

Yes, django signals runs in the same thread as the caller by default because of their synchronous nature.

Code Snippet: you can find it in -> **./assignment/questions/question2.py**


**Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.**

**Answer:**

By default, they run in the same database transaction as the caller meaning if the the signal is called during a database transaction, the signal handler will run within the same transaction.

Code Snippet: you can find it in -> **./assignment/questions/question3.py**
