package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main4 extends Application {
	
	private Scene scene;
	private TextField tfMine;
	private TextField tfCom;
	private TextField tfResult;
	private Button btn;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main4.fxml"));
			scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			getId();
			
			btn.setOnMouseClicked(new EventHandler<Event>(){
				@Override
				public void handle(Event event) {
					playGame();
				}

			});
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void playGame() {

		String mine = tfMine.getText();
		String com = ""; 
		String result = "";
		
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
		btn = (Button) scene.lookup("#btn");
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
