package org.geeksforgeeks.practice.basics;

import junit.framework.TestCase;

public class ComplexTest extends TestCase {
    Complex c1 = new Complex(11, -5);
    Complex c2 = new Complex();

    public void testTestToString() {
        assertEquals("11 - i5", c1.toString());
        assertEquals("0 + i0", c2.toString());
    }

    public void testAdd() {
        c2.add(c1).add(new Complex(5, 5));
        assertEquals(0, c2.comp);
    }
}