package application;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class Main05 extends Application {
	
	private Label lbl1;
	private Label lbl2;
	private Label lbl3;
	private Label lbl4;
	private Label lbl5;
	private Label lbl6;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main05.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			lbl1 = (Label) scene.lookup("#lbl1");
			lbl2 = (Label) scene.lookup("#lbl2");
			lbl3 = (Label) scene.lookup("#lbl3");
			lbl4 = (Label) scene.lookup("#lbl4");
			lbl5 = (Label) scene.lookup("#lbl5");
			lbl6 = (Label) scene.lookup("#lbl6");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					
					getLotto2();
				}
				
			});
			
			btn.setOnKeyPressed(new EventHandler<KeyEvent>() {
				@Override
				public void handle(KeyEvent event) {
					if (event.getCode().equals(KeyCode.SPACE)) {
						getLotto2();
					}
					
				}
			});
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void getLotto() {
		
		// 입력
		List<Integer> lottoNum = new ArrayList<>();
		
		// 처리
		for (int i = 0; i < 45; i++) {
			lottoNum.add(i+1);
		}
		Collections.shuffle(lottoNum);
		
		// 출력
		lbl1.setText(lottoNum.get(0) + "");
		lbl2.setText(lottoNum.get(1) + "");
		lbl3.setText(lottoNum.get(2) + "");
		lbl4.setText(lottoNum.get(3) + "");
		lbl5.setText(lottoNum.get(4) + "");
		lbl6.setText(lottoNum.get(5) + "");
		
	}
	
	public void getLotto2() {
		
		// 입력
		int[] arr = {
					 1,2,3,4,5,			6,7,8,9,10,
					 11,12,13,14,15,	16,17,18,19,20,
					 21,22,23,24,25,	26,27,28,29,30,
					 31,32,33,34,35,	36,37,38,39,40,
					 41,42,43,44,45
					};
		
		List<Integer> arr6 = new ArrayList<Integer>();
		
		
		// 처리
		while(arr6.size() < 6) {
			int rnd = (int)(Math.random()*45);
			
			if (arr[rnd] > 0) {
				arr6.add(arr[rnd]);
				arr[rnd] = -1;
			}
		}
		
		
		// 출력
		lbl1.setText(arr6.get(0) + "");
		lbl2.setText(arr6.get(1) + "");
		lbl3.setText(arr6.get(2) + "");
		lbl4.setText(arr6.get(3) + "");
		lbl5.setText(arr6.get(4) + "");
		lbl6.setText(arr6.get(5) + "");
		
	}
	
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
