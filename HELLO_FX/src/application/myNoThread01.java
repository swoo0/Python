package application;

public class myNoThread01 {
	
	public static void showNum() {
		
		for (int i = 0; i < 100000; i++) {
			System.out.print(i);
				if (i % 100 == 0) {
					System.out.println();
			}
		}
	}
	
	public static void showAscii() {
		int ga = -1;
		int hih = -1;
		
		for (int i = 0; i < 100000; i++) {
			if ((char)i == '가') {
				ga = i;
				System.out.println(i);
			}
			if ((char)i == '힣') {
				hih = i;
				System.out.println(i);
			}
		}
		int count = hih - ga + 1;
		System.out.println(count);
	}

	
	public static void main(String[] args) {
		showNum();
		showAscii();
	}
}
