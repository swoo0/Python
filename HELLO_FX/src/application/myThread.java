package application;

public class myThread {

	public static void showNum() {
		new Thread(new Runnable() {
			
			@Override
			public void run() {
				for (int i = 0; i < 100000; i++) {
					System.out.print(i);
						if (i % 100 == 0) {
							System.out.println();
					}
				}
			}
		}).start();

	}
	
	public static void showAscii() {
		new Thread(new Runnable() {
			
			@Override
			public void run() {
				for (int i = 0; i < 100000; i++) {
					System.out.print((char)i);
					if (i % 100 == 0) {
						System.out.println();
					}
				}
			}
		}).start();
		
	}

	
	public static void main(String[] args) {
		showNum();
		showAscii();
	}
}
