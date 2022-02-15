package day15;

public class RefTest {
	
	public static void rentArr(int[] a) {
		a[0] = 3;
	}
	public static void rentA(int a) {
		a = 4;
	}
	public static void rentB(String b) {
		b = "12";
	}
	public static void main(String[] args) {
		int[] arr = {1};
		int a = 2;
		String b = "11";
		
		System.out.println("arr[0]: " + arr[0]);
		System.out.println("a: " + a);
		System.out.println("b: " + b);
		
		rentArr(arr);
		rentA(a);
		rentB(b);
		
		System.out.println("arr[0]: " + arr[0]);
		System.out.println("a: " + a);
		System.out.println("b: " + b);
	}
}