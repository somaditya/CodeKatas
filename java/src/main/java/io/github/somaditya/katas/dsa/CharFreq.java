package io.github.somaditya.katas.dsa;

import java.util.HashMap;

public class CharFreq {
    public HashMap<Character, Integer> count(String input) {
        HashMap<Character, Integer> hm = new HashMap<>();
    
        for (Character c : input.toCharArray()) {
            if (hm.containsKey(c)) {
                hm.put(c, hm.get(c) + 1);
            } else {
                hm.put((c), 1);
            }
        }
        return hm;
    }
}
