package com.tasks3.fibonacci;

public class Fibonacci
{
	public long getNumber(int position){
        if (position <= 0)
			return -1;
		if (position == 1)
			return 1;
		if (position == 2)
			return 1;
		else
			return getNumber(position - 1) + getNumber(position - 2);
	}
}