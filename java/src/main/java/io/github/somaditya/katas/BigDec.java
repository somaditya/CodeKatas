package io.github.somaditya.katas;

import java.math.BigDecimal;
import java.util.*;

class BigDec {
    public static void main(String[] args) {
        //Input
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] s = new String[n + 2];
        for (int i = 0; i < n; i++) {
            s[i] = sc.next();
        }
        sc.close();
        
        ArrayList<BigDecimal> list = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            list.add(new BigDecimal(s[i]));
        }
        
        list.sort(null);
        
        int iList = list.size() - 1;
        int iArray = 0;
        
        while (iList >= 0) {
            s[iArray] = list.get(iList).stripTrailingZeros().toString();
            iList--;
            iArray++;
        }
        
        //Output
        for (int i = 0; i < n; i++) {
            System.out.println(s[i]);
        }
    }
}