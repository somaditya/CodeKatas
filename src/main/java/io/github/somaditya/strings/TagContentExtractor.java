package io.github.somaditya.strings;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class TagContentExtractor {
    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        while (testCases > 0) {
            String line = in.nextLine();
            
            String content = line.substring(line.indexOf(">") + 1, line.indexOf("<", line.indexOf(">")));
            System.out.println(content);
            
            testCases--;
        }
    }
}
