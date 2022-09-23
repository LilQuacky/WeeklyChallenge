import java.awt.*;
import java.awt.event.*;
import java.util.Random;
import java.util.Scanner;

import javax.swing.*;

public class MyPanel extends JPanel implements ActionListener{

	//Panel dimension
	final int PANEL_WIDTH = 1920;
	final int PANEL_HEIGHT= 1000;
	
	MyImage[] confetti;
	Image background;
	Timer timer;
	
	
	//create and generate the confetti
	MyPanel(){
	
		confetti=new MyImage[lengthArray()];
		
		this.setPreferredSize(new Dimension(PANEL_WIDTH,PANEL_HEIGHT));
		this.setBackground(Color.black);
		background=new ImageIcon("pic/bg.jpeg").getImage();
		
		for(int i=0; i<confetti.length; i++) {
			confetti[i] = new MyImage(new ImageIcon("pic/conf4.png"), randomNumber(), randomNumber(), randomNumber(), randomNumber());
		}

		timer = new Timer(1, this);
		timer.start();
	}
	
	//use 2d dimension
	public void paint(Graphics g) {
		
		super.paint(g);
		
		Graphics2D g2D = (Graphics2D) g;
		g2D.drawImage(background,0,0, null);
		
		for(int i=0; i<confetti.length; i++) {
		g2D.drawImage(confetti[i].image.getImage(),confetti[i].getX(),confetti[i].getY(), null);
		}

		
	}
	
	//move the coriandoli
	@Override
	public void actionPerformed(ActionEvent e) {
		
		for(int i=0; i<confetti.length; i++) {
			
			if(confetti[i].getX()>=PANEL_WIDTH-confetti[i].image.getImage().getWidth(null) || confetti[i].getX()<0) {
				confetti[i].xVelocity*=-1;
			}
			confetti[i].setX(confetti[i].xVelocity+confetti[i].getX()+delta());
			
			if(confetti[i].getY()>=PANEL_WIDTH-confetti[i].image.getImage().getWidth(null) || confetti[i].getY()<0) {
				confetti[i].yVelocity*=-1;
			}
			confetti[i].setY(confetti[i].yVelocity+confetti[i].getY() + delta());
		}
		repaint();
	}
		
	//generate a randomNumber	
	public int randomNumber() {
		double r=Math.random()*30+10;
		return (int) r;
	}
	
	//generate a negative or positive number
	public int delta() {
		return new Random().nextInt(10 + 10) - 10;
	}
	
	//generate the dimension of the Array
	public int lengthArray() {
		Scanner input=new Scanner(System.in);
		int n=-1;
		while(n<0 || n>100) {
			System.out.print("Clinton confetti shooter ready to use. Choose the power with a number between 1 and 100: ");
			n=input.nextInt();
		}
		return n;
	}
}
