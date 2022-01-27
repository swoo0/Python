package application;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class Main10 extends Application {

	Label lbl;

	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main10.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();

			lbl = (Label) scene.lookup("#lbl");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myTimer();

				}
			});

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void myTimer() {
		new Thread(new Runnable() {
			@Override
			public void run() {
				
				for (int i = 0; i < 9; i++) {
					try {
						Thread.sleep(1000);
					} catch (Exception e) {
						e.printStackTrace();
					}
				
					Platform.runLater(new Runnable() {
						@Override
						public void run() {
							String a = lbl.getText();
							int aa = Integer.parseInt(a);
							aa++;
							lbl.setText(aa + "");
						}
					});
				}
			}
		}).start();

	}

	public static void main(String[] args) {
		launch(args);
	}
}
