import javax.swing.*;
import java.awt.*;

public class MyFrame extends JFrame {
	
	MyPanel panel;
	
	// customize my panel
	MyFrame(){
		panel = new MyPanel();
		
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.add(panel);
		this.pack();
		this.setLocationRelativeTo(null);
		this.setVisible(true);
		
		//icon image
		ImageIcon image= new ImageIcon("pic/confettipic.png");
		this.setIconImage(image.getImage());
	}
}
