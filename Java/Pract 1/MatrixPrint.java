public class MatrixPrint {
	public static void main(String args[]){
		//PUT YOUR CODE HERE
        int size = 5;
		int num = size - 1;
		int sum = 1;
		
		String arr[][] = new String[size][size];
		
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				arr[i][j] = sum + "";
				sum++;
			}
		}
		
		
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				
				if (i == j) {
					arr[i][j] = "*";
					arr[i][num] = "*";
				} else {
					arr[i][num] = "*";
				}
				
				System.out.printf("%2s ", arr[i][j]);
			}
			System.out.println();
			num--;
		}
        //PUT YOUR CODE HERE
	}
}