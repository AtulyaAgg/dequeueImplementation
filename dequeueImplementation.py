dequeue = [0]*10 #circular array of length 10
r = -1 #rear pointer
f = -1 #front pointer

def enqueueAtFront(num):
    global f, r, dequeue
    if (f==0 and r==len(dequeue)-1) or f==r+1:
        print("dequeue is full while inserting at front")
    elif f==0:
        f = len(dequeue)-1
        dequeue[f] = num
    elif f==-1 and r==-1:
        r=0
        f=0
        dequeue[f] = num
    else:
        f-=1
        dequeue[f] = num

def enqueueAtRear(num):
    global f, r, dequeue
    if (f==0 and r==len(dequeue)-1) or f==r+1:
        print("dequeue is full while inserting at read")
    elif r==len(dequeue)-1:
        r=0
        dequeue[r] = num
    elif f==-1 and r==-1:
        r=0
        f=0
        dequeue[r] = num
    else:
        r+=1
        dequeue[r] = num

def deletionAtFront():
    global f, r, dequeue
    if f==-1 and r==-1:
        print("dequeue is empty while deleting at front")
    elif f==r:
        print(f"Deleted element is: {dequeue[f]}" )
        f=-1
        r=-1
    elif f==len(dequeue)-1:
        print(f"Deleted element is: {dequeue[f]}")
        f=0
    else:
        print(f"Deleted element is: {dequeue[f]}")
        f+=1

def deletedAtRear():
    global f, r, dequeue
    if f==-1 and r==-1:
        print("dequeue is empty while deleting at read")
    elif f==r:
        print(f"Deleted element is: {dequeue[r]}")
        f=-1
        r=-1
    elif r==0:
        print(f"Deleted element is: {dequeue[r]}")
        r=len(dequeue)-1
    else:
        print(f"Deleted element is: {dequeue[r]}")
        r-=1

def getAllElements():
    global f, r, dequeue
    if f==-1 and r==-1:
        print("dequeue is empty")
    i=f
    while i!=r:
        print(dequeue[i])
        i=(i+1)%len(dequeue)
    print(dequeue[r])

def getFront():
    global f, dequeue
    if f==-1 and r==-1:
        print("dequeue is empty, nothing to show while getting front")
    print(dequeue[f])

def getRear():
    global r, dequeue
    if f==-1 and r==-1:
        print("dequeue is empty, nothing to show while getting rear")
    print(dequeue[r])

def executeOperations(operation, value=None):
    if operation == "enqueueAtFront":
        enqueueAtFront(value)
    elif operation == "enqueueAtRear":
        enqueueAtRear(value)
    elif operation == "deletionAtFront":
        deletionAtFront()
    elif operation == "deletionAtRear":
        deletionAtRear()
    elif operation == "getAllElements":
        getAllElements()
    elif operation == "getFront":
        getFront()
    elif operation == "getRear":
        getRear()
    else:
        print("Invalid operation")

executeOperations("enqueueAtRear", 10)
executeOperations("enqueueAtRear", 20)
executeOperations("enqueueAtFront", 5)
executeOperations("getAllElements")
executeOperations("deletionAtFront")
executeOperations("getAllElements")
print(dequeue)
