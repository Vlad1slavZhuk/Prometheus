package com.tasks6.rle_decoder;

public class Application {

    public static void main(String[] args) {
        
        if ((args.length == 0)  || (args[0].equals(""))) {
            System.out.println("");
        } else {
            String income = args[0];
            int length = income.length();

            if (Character.isDigit(income.charAt(0))) {
                System.out.println("");
                return;
            }

            for (int i = 0; i < length - 1; i++) {
                if (income.charAt(i) == income.charAt(i + 1)) {
                    System.out.println("");
                    return;
                }
                if (Character.isDigit(income.charAt(i)) && Character.isDigit(income.charAt(i + 1))) {
                    System.out.println("");
                    return;
                }
            }

            StringBuilder result = new StringBuilder("");
            char basket;
            int n = 0;
            basket = income.charAt(0);

            for (int i = 1; i < length; i++) {

                if (Character.isDigit(income.charAt(i))) {
                    n = income.charAt(i) - '0';

                    for (int j = 0; j < n - 1; j++) {
                        result.append(basket);
                    }
                } else {
                    result.append(basket);
                    basket = income.charAt(i);
                }
            }

            result.append(basket);
            System.out.println(result.toString());
        }
    }
}