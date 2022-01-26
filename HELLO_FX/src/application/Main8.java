package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;


public class Main8 extends Application {
	
	TextField tfs;
	TextField tfl;
	TextArea ta;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main8.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			tfs = (TextField) scene.lookup("#tfStart");
			tfl = (TextField) scene.lookup("#tfLast");
			ta = (TextArea) scene.lookup("#ta");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					print();
				}
			});
			
			tfl.setOnKeyPressed(new EventHandler<KeyEvent>() {
				@Override
				public void handle(KeyEvent event) {
					if (event.getCode().equals(KeyCode.ENTER)) {
						print();
					}
				}
			});
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void print() {
		
		String a = tfs.getText();
		String b = tfl.getText();
		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);
		String txt = "";
		
//		for (int i = inum; i <= iline; i++) {
//			star += "z";
//			for (int j = 1; i <= inum; j++) {
//					star += "*";
//			}
//			star += "\n";
//		}
		
		for (int i = aa; i <= bb; i++) {
			txt += drawStar(i);
		}
		
		ta.setText(txt);
	}
	
	public String drawStar(int cnt) {
		String ret = "";
		for (int i = 0; i < cnt; i++) {
			ret += "*";
		}
		ret += "\n";
		return ret;
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
