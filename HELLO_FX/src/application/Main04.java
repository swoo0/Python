package application;
	
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


public class Main04 extends Application {
	
	private Scene scene;
	private TextField tfMine;
	private TextField tfCom;
	private TextField tfResult;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main04.fxml"));
			scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			tfMine = (TextField) scene.lookup("#tfMine");    
			tfCom = (TextField) scene.lookup("#tfCom");      
			tfResult = (TextField) scene.lookup("#tfResult");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>(){
				@Override
				public void handle(Event event) {
					playGame();
				}

			});
			
			tfMine.setOnKeyPressed(new EventHandler<KeyEvent>() {
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
		String mine = "";
		String com = ""; 
		String result = "";
		mine = tfMine.getText();
		
		
		// 처리
		double rnd = Math.random();
		if (rnd > 0.5) {
			com = "홀";
		} else {
			com = "짝";
		}
		
		if (mine.equals(com)) {
			result += "승리 !";
		} else {
			result += "패배 !";
		}
		
		// 출력
		tfCom.setText(com);
		tfResult.setText(result);
		
	}
	
	public void getId() {
		tfMine = (TextField) scene.lookup("#tfMine");    
		tfCom = (TextField) scene.lookup("#tfCom");      
		tfResult = (TextField) scene.lookup("#tfResult");
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
