package com.hackerrank.linkedlist;

public class Node {
    Node next;
    int data;
    
    Node(int data) {
        this.data = data;
        next = null;
    }
    
    Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }
    
    //get-set
    public int getData() {
        return data;
    }
    
    public void setData(int newData) {
        data = newData;
    }
    
    public Node getNext() {
        return next;
    }
    
    public void setNext(Node newNext) {
        next = newNext;
    }
}
