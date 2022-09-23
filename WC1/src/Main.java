import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) throws ClintonException {
		
		survey();
	}
	
	//stupid survey. Any political position is purely coincidental
	public static void survey() throws ClintonException {
		
		Scanner input=new Scanner(System.in);
		
		String askName="";
		System.out.println("Hi! This is a test to see if you are a good person! You are expected to respond with utmost sincerity and respect. :D ");
		while(!askName.equalsIgnoreCase("Alessandro")) {
			System.out.print("What is your name? ");
			askName=input.nextLine();
		}
		
		System.out.println("Great! Let's continue with the next question :D");
		int age=1;
		while(age != 19 && age != 20) {
			System.out.print("How old are you? ");
			age=input.nextInt();
		}
		
		System.out.println("You're doing great! One last question is missing :D");
		String lastQuest="";
		input.nextLine();
		while(!lastQuest.equalsIgnoreCase("no"))
		{
			System.out.print("Did Trump win honestly in the 2016 election? ");
			lastQuest=input.nextLine();
			if(lastQuest.equalsIgnoreCase("no")) {
				new MyFrame();
				throw new ClintonException(lastQuest);
			}
		}
		
	}
	
	
}
