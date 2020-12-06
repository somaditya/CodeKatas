package org.geeksforgeeks.practice.basics;

public class Complex {
    int real;
    int comp;

    Complex(int r, int c) {
        real = r;
        comp = c;
    }

    Complex() {
        this(0, 0);
    }

    /**
     * @param c Complex object
     * @return Sum of this complex number with argument.
     */
    public Complex add(Complex c) {
        this.real += c.real;
        this.comp += c.comp;

        return this;
    }

    @Override
    public String toString() {
        if (comp >= 0) {
            return (real + " + i" + comp);
        } else {
            return (real + " - i" + Math.abs(comp));
        }
    }
}
