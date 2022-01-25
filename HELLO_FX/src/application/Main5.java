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
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class Main5 extends Application {
	
	private Scene scene;
	private Label lbl1;
	private Label lbl2;
	private Label lbl3;
	private Label lbl4;
	private Label lbl5;
	private Label lbl6;
	private Button btn;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main5.fxml"));
			scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			getId();
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					
					getLotto();
					
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
	
	public void getId() {
		lbl1 = (Label) scene.lookup("#lbl1");
		lbl2 = (Label) scene.lookup("#lbl2");
		lbl3 = (Label) scene.lookup("#lbl3");
		lbl4 = (Label) scene.lookup("#lbl4");
		lbl5 = (Label) scene.lookup("#lbl5");
		lbl6 = (Label) scene.lookup("#lbl6");
		btn = (Button) scene.lookup("#btn");
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
