package com.tasks7.rpn;

import java.util.Deque;
import java.util.LinkedList;

public class Application {

	public static double parse(String rpnString) {
        if (rpnString == null || rpnString.isEmpty())
            throw new RPNParserException();

        String[] array = rpnString.split(" ");
        Deque<Double> stack = new LinkedList<>();

        for (String s : array) {
            if (isNumber(s))
                stack.push(Double.parseDouble(s));

            else if (isOperator(s)) {
                if (stack.size() < 2) {
                    throw new RPNParserException();
                }
                switch (s) {
                    case "+":
                        stack.push(stack.pop() + stack.pop());
                        break;
                    case "-":
                        stack.push(-stack.pop() + stack.pop());
                        break;
                    case "/":
                        if (stack.peek() == 0) {
                            throw new ArithmeticException();
                        }
                        stack.push(1 / stack.pop() * stack.pop());
                        break;
                    case "*":
                        stack.push(stack.pop() * stack.pop());
                        break;
                }
            } else
                throw new RPNParserException();
        }
        if (stack.size() != 1)
            throw new RPNParserException();

        return stack.pop();
    }

    private static boolean isNumber(String string) {
        if (string == null)
            return false;
        return string.matches("^-?\\d+(\\.\\d+)?$");
    }

    private static boolean isOperator(String string) {
        if (string == null)
            return false;
        return string.matches("[+-/*]");
    }

	public static void main(String[] args) {
        if (args == null || args.length == 0)
            throw new RPNParserException();
            
        System.out.println(parse(args[0]));
	}

}