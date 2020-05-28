package com.tasks6.rle;

public class Application
{
	public static void main( String[] args )
	{
    if (args == null || args.length == 0) {
            System.out.println();
        } else {
            StringBuilder newWord = new StringBuilder();
            String word = args[0];
            int length = word.length();

            for (int i = 0; i < length; i++) {
                int count = 1;
                while (i < length - 1 && word.charAt(i) == word.charAt(i + 1)){
                    if (count == 9)
                        break;
                    count++;
                    i++;
                }
                newWord.append(word.charAt(i));
                if (count > 1)
                    newWord.append(count);
            }
            System.out.println(newWord.toString());
        }
	}
}      