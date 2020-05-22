package com.hackerearth.tatacliq.maxreward;

import java.io.*;
import java.util.*;
import java.util.Collections;

class Main{
    
    /*
    Input:
    t=2
    n=6
    1 2 3 4 5 6
    n=3
    1 2 3

    Output:
    8
    2
    
    prob desc:
    n divisible by 3
    pick 3 nums, each only once, middle num is reward
    solve for max reward
     */
    public long solution(int n, int[] a) {
        Arrays.sort(a);
        
        for (int i : a) {
            System.out.println(i);
        }
        return a[0];
    }
    public void run() throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-->0) {
            int n = sc.nextInt();
            int[] a = new int[n];
            for(int i = 0; i< n; i++) {
                a[i] = sc.nextInt();
            }
            long ans = solution(n, a);
            System.out.println(ans);
        }
    }
    public static void main(String[] args) throws IOException{
        new Main().run();
    }
}