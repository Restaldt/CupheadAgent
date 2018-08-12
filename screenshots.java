import java.awt.AWTException;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;
import java.awt.Image;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.JFrame;

public class screenshots {
	
	
	public static void main(String[] args){
		String ui = args[0];
		int ssNum = Integer.parseInt(ui);
		//int ssNum = 0;
		
		boolean ssCap = false;
		while(!ssCap){
			
			try {
			//if(ssNum == 32){
			//	ssCap = true;
			//}
				/*
			Rectangle healthRect = new Rectangle(67,1330,128,75);
			BufferedImage capture;
			capture = new Robot().createScreenCapture(healthRect);
			File healthDir = new File("D:\\screenShots\\healthOnly\\"+ssNum);
			healthDir.mkdir();`	
			healthDir = new File("D:\\screenShots\\healthOnly\\"+ssNum+"\\unknown");
			healthDir.mkdir();
			ImageIO.write(capture, "jpg", new File("D:\\screenShots\\healthOnly\\"+ssNum+"\\unknown\\"+ssNum+".jpg"));
			*/
			BufferedImage capture;
			Rectangle fullRect = new Rectangle(0,0,2560,1440);
			capture = new Robot().createScreenCapture(fullRect);
			File fullDir = new File("D:\\screenShots\\agent\\ss\\ss2\\"+ssNum);
			fullDir.mkdir();
			fullDir = new File("D:\\screenShots\\agent\\ss\\ss2\\"+ssNum+"\\unknown");
			fullDir.mkdir();
			ImageIO.write(capture, "jpg", new File("D:\\screenShots\\agent\\ss\\ss2\\"+ssNum+"\\unknown\\"+ssNum+".jpg"));
			
			//fullDir.mkdir();
			//fullDir = new File("D:\\screenShots\\fullShots\\"+ssNum+"\\unknown");
			//fullDir.mkdir();
			//ImageIO.write(capture, "jpg", new File("D:\\screenShots\\fullShots\\"+ssNum+"\\unknown\\"+ssNum+".jpg"));
			
			//File fullDir = new File("D:\\screenShots\\agent\\ss\\"+ssNum);
			ImageIO.write(capture, "jpg", new File("D:\\screenShots\\agent\\ss\\"+ssNum+".jpg"));
			
			

			ssNum++;

			
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	
		}
		
	}

}
