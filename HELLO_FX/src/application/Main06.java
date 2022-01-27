package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main06 extends Application {
	
	TextField tf;
	TextArea ta;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main6.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			tf = (TextField) scene.lookup("#tf");
			ta = (TextArea) scene.lookup("#ta");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					gugudan();
				}
			});
			
			tf.setOnKeyPressed(new EventHandler<KeyEvent>() {
				@Override
				public void handle(KeyEvent event) {
					if (event.getCode().equals(KeyCode.ENTER)) {
						gugudan();
					}
				}
			});
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	
	public void gugudan() {
		
		// 입력
		String dan = tf.getText();
		int idan = Integer.parseInt(dan);
		String text = "";
		
		// 처리
		text += dan + "단" + "\n";
		for (int i = 1; i < 10; i++) {
			text += dan + " * " + i + " = " + (idan * i) + "\n";
		}
		
//		text += idan + "단" + "\n";
//		text += dan + " * " + 1 + " = " + (idan*1) + "\n";
//		text += dan + " * " + 2 + " = " + (idan*2) + "\n";
//		text += dan + " * " + 3 + " = " + (idan*3) + "\n";
//		text += dan + " * " + 4 + " = " + (idan*4) + "\n";
//		text += dan + " * " + 5 + " = " + (idan*5) + "\n";
//		text += dan + " * " + 6 + " = " + (idan*6) + "\n";
//		text += dan + " * " + 7 + " = " + (idan*7) + "\n";
//		text += dan + " * " + 8 + " = " + (idan*8) + "\n";
//		text += dan + " * " + 9 + " = " + (idan*9) + "\n";
		
		// 출력
		ta.setText(text);
		
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
