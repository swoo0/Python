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
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main7 extends Application {
	
	TextField tfm;
	TextField tfc;
	TextField tfr;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main7.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			tfm = (TextField) scene.lookup("#tf_Mine");
			tfc = (TextField) scene.lookup("#tf_Com");
			tfr = (TextField) scene.lookup("#tf_Result");
			
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					playGame();
				}
			});
			
			tfm.setOnKeyPressed(new EventHandler<KeyEvent>() {
				@Override
				public void handle(KeyEvent event) {
					if (event.getCode().equals(KeyCode.ENTER)) {
						playGame();
					}
				}
			});
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void playGame() {
		
		// 입력
		String mine = tfm.getText();
		String com = "";
		String result = "";
		
		List<String> list = new ArrayList<>();
		list.add("가위");
		list.add("바위");
		list.add("보");
		
		Collections.shuffle(list);
		com = list.get(0);
		
		// 처리
		if (mine.equals(list)) {
			result = "무승부 !";
		} else if (mine.equals("가위") && com.equals("보")
				|| mine.equals("바위") && com.equals("가위")
				|| mine.equals("보") && com.equals("바위")) {
			result = "승리 !";
		} else {
			result = "패배 !";
		}
		
		// 출력
		tfc.setText(com);
		tfr.setText(result);
		
	}
	
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
