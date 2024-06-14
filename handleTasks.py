# -*- coding: utf-8 -*-
"""
Created on Sun May 26 19:58:46 2024

@author: rahul
"""
class Queue:
    def __init__(self, size):
        self.queue = [None for _ in range(size)]
        self.front = -1
        self.rear = -1
        self.size = size
    
    def enqueue(self, x):
        if self.rear >= self.size:
            raise IndexError("enqueue in full queue.")
        self.rear = self.rear + 1
        self.queue[self.rear] = x
        
    def dequeue(self):
        if self.front == -1:
            raise IndexError('dequeue in empty queue.')
        x = self.queue[self.front]
        if self.front == self.rear:
            self.front, self.rear = -1
        else:
            self.front = self.front + 1
        if self.front == self.size:
            self.front = 0
        return x
    
    def sneekPeak(self):
        print(self.queue)