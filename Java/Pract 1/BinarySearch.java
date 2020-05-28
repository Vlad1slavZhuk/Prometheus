public class BinarySearch {

	public static void main(String[] args) {

		int data[] = { 3, 6, 7, 10, 34, 56, 60 };
		int numberToFind = 10;

		// PUT YOUR CODE HERE
        int last = data.length - 1;
		int first = 0;
		int mid = (last + 1) / 2;
		
		while(data[mid] != numberToFind && last != mid && first != mid) {
			if (data[mid] < numberToFind) {
				first = mid;
				mid = (last + first) / 2;
			} else {
				last = mid;
				mid = (last + first) / 2;
			}
		}
		if (data[last] == numberToFind)
			mid = last;
		if (data[first] == numberToFind)
			mid = first;
		
		System.out.println(data[mid] == numberToFind ? mid : -1);
		// PUT YOUR CODE HERE
	}
}