package org.geeksforgeeks.practice.basics;

public class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Point() {
        this(0,0);
    }

    @Override
    public String toString() {
        String output = "x: " + x + ", y: " + y;
        return output;
    }
}
