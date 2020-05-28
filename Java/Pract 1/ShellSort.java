public class ShellSort {

	public static void main(String[] args) {
		int[] array = {30, 2, 10, 4, 6};
		int length = array.length;

		//PUT YOUR CODE HERE
        int step = length / 2;
		while (step > 0) {
			int i,j;
			for (i = step; i < length; i++) {
				int value = array[i];
				for (j = i - step; (j >= 0) && (array[j] > value); j -= step)
					array[j + step] = array[j];
				
				array[j + step] = value;
			}
			step /= 2;
		}
		//PUT YOUR CODE HERE
	    
		for (int i = 0; i < length; i++) {
			System.out.print(array[i] + " ");
		}
	}
}