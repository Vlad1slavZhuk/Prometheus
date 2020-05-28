public class SquareRoot {

	public static void main(String[] args) {
		double a = 3;
		double b = 2.5;
		double c = -0.5;

		//PUT YOUR CODE HERE
		double D;
		D = b * b - 4 * a * c;
		
		if (D > 0) {
			double x1, x2;
			x1 = (-b + Math.sqrt(D)) / (2 * a);
			if (Double.isNaN(x1) || Double.isInfinite(x1))
				x1 = 0;
		    x2 = (-b - Math.sqrt(D)) / (2 * a);
		    if (Double.isNaN(x2) || Double.isInfinite(x2))
				x2 = 0;
		    System.out.println("x1=" + x1);
		    System.out.println("x2=" + x2);
		} else if (D == 0) {
			double x;
			x = -b / (2 * a);
			if (Double.isNaN(x) || Double.isInfinite(x)) {
				System.out.println("x1=");
				System.out.println("x2=");
				return;
			}		
			System.out.println("x1=" + x);
			System.out.println("x2=" + x);
		} else {
			System.out.println("x1=");
			System.out.println("x2=");
		}
		//PUT YOUR CODE HERE
	}
}
      
      