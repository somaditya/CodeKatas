package org.geeksforgeeks.practice.basics;

import org.junit.jupiter.api.Test;

class PointTest {
    @Test
    void testPoint() {
        Point origin = new Point();
        Point p1 = new Point(10, 20);

        assert p1.toString().equals("x: 10, y: 20");
        assert origin.toString().equals("x: 0, y: 0");

        assert p1.x == 10;
        assert origin.y == 0;
    }
}