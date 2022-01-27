package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

		
public class Main09 extends Application {
	
	TextField tf;
	Button btn1;
	Button btn2;
	Button btn3;
	Button btn4;
	Button btn5;
	Button btn6;
	Button btn7;
	Button btn8;
	Button btn9;
	Button btn0;
	Button btnCall;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main09.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			tf = (TextField) scene.lookup("#tf");
			btn1 = (Button) scene.lookup("#btn1");
			btn2 = (Button) scene.lookup("#btn2");
			btn3 = (Button) scene.lookup("#btn3");
			btn4 = (Button) scene.lookup("#btn4");
			btn5 = (Button) scene.lookup("#btn5");
			btn6 = (Button) scene.lookup("#btn6");
			btn7 = (Button) scene.lookup("#btn7");
			btn8 = (Button) scene.lookup("#btn8");
			btn9 = (Button) scene.lookup("#btn9");
			btn0 = (Button) scene.lookup("#btn0");
			btnCall = (Button) scene.lookup("#btnCall");
			
			
			btn1.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					selectNum(btn1);
				}
			});
			btn2.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					selectNum(btn2);
				}
			});
			btn3.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					selectNum(btn3);
				}
			});
			btn4.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					selectNum(btn4);
				}
			});
			btn5.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					selectNum(btn5);
				}
			});
			btn6.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					selectNum(btn6);
				}
			});
			btn7.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					selectNum(btn7);
				}
			});
			btn8.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					selectNum(btn8);
				}
			});
			btn9.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					selectNum(btn9);
				}
			});
			btn0.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					selectNum(btn0);
				}
			});
			
			btnCall.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					call();
				}
			});
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void selectNum(Button btn) {
		String old_Num = tf.getText();
		String new_num = btn.getText();
		
		tf.setText(old_Num += new_num);
	}
	
	public void call() {
		String callNum = tf.getText();
		
		Alert a = new Alert(Alert.AlertType.INFORMATION, callNum + " 연결중..");
		a.showAndWait();
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
