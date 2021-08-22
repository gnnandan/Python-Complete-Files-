"""
The retry function tries to execute an 
operation that might fail, it retries the operation 
for a number of attempts.  Currently the code 
will keep executing the function even if it succeeds. 
Fill in the blank so the code stops trying after the operation succeeded.
"""
def retry(attempts):
    operation=['create_user','stop_services']
    for n in range(attempts):
        if operation:
            print("Attempt " + str(n) + " succeeded")
            # break
        else:
            print("Attempt " + str(n) + " failed")

retry(3)
retry(5)
