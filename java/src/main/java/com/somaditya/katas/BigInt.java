package com.somaditya.katas;
        
        import java.io.*;
        import java.util.*;
        import java.text.*;
        import java.math.*;
        import java.util.regex.*;

public class BigInt {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        BigInteger n1 = new BigInteger(sc.next());
        BigInteger n2 = new BigInteger(sc.next());
        
        System.out.println(n1.add(n2));
        System.out.println(n1.multiply(n2));
        
    }
}
