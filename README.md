# Dequeue Data Structure using Circular Queue

## Overview

This repository provides an implementation of a **Dequeue** (Double-ended Queue) using a **circular queue**. A Dequeue allows insertion and deletion of elements from both the front and rear ends, making it a versatile data structure. By leveraging circular queue theory, we ensure optimal use of space and efficient element management.

## Features

- **Insert at Front**: Add elements to the front of the dequeue.
- **Insert at Rear**: Add elements to the rear of the dequeue.
- **Delete from Front**: Remove elements from the front of the dequeue.
- **Delete from Rear**: Remove elements from the rear of the dequeue.
- **Circular Array Implementation**: Uses a fixed-size array where the rear wraps around to the front, maximizing space utilization.
- **Peek Operations**: Retrieve the element at the front or rear of the dequeue without removing it.
- **Display All Elements**: Print all elements currently in the dequeue in order of insertion.

## Data Structure Details

- **dequeue**: The circular array that holds the elements (fixed size of 10 in this implementation).
- **f**: Front pointer, indicating where the first element is in the dequeue.
- **r**: Rear pointer, indicating where the last element is in the dequeue.

## Operations

The following operations are supported:

1. **Enqueue at Front**: Insert an element at the front of the dequeue.
2. **Enqueue at Rear**: Insert an element at the rear of the dequeue.
3. **Delete from Front**: Remove an element from the front.
4. **Delete from Rear**: Remove an element from the rear.
5. **Get All Elements**: Display all the current elements in the dequeue.
6. **Get Front**: Retrieve the front element without removing it.
7. **Get Rear**: Retrieve the rear element without removing it.

## How to Use

### Prerequisites
-Python 3.x installed on your machine.

### Running the Code
1. Clone the repository:
```
    git clone https://github.com/your-username/dequeue-circular-queue.git
    cd dequeue-circular-queue
```
2. Open the code in a Python IDE or execute it via terminal/command prompt:
```
    python3 dequeue.py
```
3. The program provides an example where enqueue, dequeue, and element retrieval operations are executed in sequence. You can modify the executeOperations function to test other operations.

### Example Usage
```
    # Example of performing operations
    executeOperations("enqueueAtRear", 10)
    executeOperations("enqueueAtRear", 20)
    executeOperations("enqueueAtFront", 5)
    executeOperations("getAllElements")
    executeOperations("deletionAtFront")
    executeOperations("getAllElements")
```

### Output Example
```
    5 10 20
    Deleted element is: 5
    10 20
```

## Functions

## File Structure

## Contributing
