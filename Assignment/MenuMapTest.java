import java.util.Scanner;

public class MenuMapTest {

public static void displayMainMenu() {

	
	
		System.out.print(""" 
			MENU
			1. Phone book
			2. Messages
			3. Chat
			4. Call register
			5. Tones
			6. Settings
			7. Call divert
			8. Games
			9. Calculator
			10. Reminders
			11. Clock
			12. Profiles
			13. SIM services
			""");
		
	}

	public static void displayMenu(String menu) {
	
		System.out.print(menu);

	}


	public static void main (String[] args) {
		
		
		Scanner collectInput = new Scanner(System.in);
		
		displayMainMenu();
		
		


		System.out.println("Select menu number: ");
		int menuNumber = collectInput.nextInt();

	while(true) {
		switch (menuNumber) {
		case 1:
		   String caseOneMenu = """
					 PHONE BOOK
					 1. Search
					 2. Service Nos.
					 3. Add name
					 4. Erase
					 5. Edit
					 6. Assign tone
					 7. Send b'card
					 8. Options
					 9. Speed dials
					 10.Voice tags
					 0. Go back
					 """;

		   displayMenu(caseOneMenu);
		   
		   System.out.println("Select option: ");
		   int selectOption = collectInput.nextInt();
		   
		   if (selectOption == 8) {
		      System.out.print("""
					OPTIONS
					1. Type of view
					2. Memory status
					0. Go back
					""");

		      System.out.println("Select option: ");
		      selectOption = collectInput.nextInt();

			if (selectOption == 0) {
			displayMenu(caseOneMenu);

		   System.out.println("Select option: ");
		   selectOption = collectInput.nextInt();
			}
		   } 

		   if (selectOption == 0) {
		   displayMainMenu();

		   System.out.println("Select option: ");
		   selectOption = collectInput.nextInt();
		   }

		break;

		case 2:
		   String caseTwoMenu = """
					MESSAGES
					1. Write messages
					2. Inbox
					3. Outbox
					4. Picture messages
					5. Templates
					6. Smileys
					7. Message settings
					8. Info service
					9. Voice mailbox number
					10.Service command editor
					0. Go back
					""";

		   displayMenu(caseTwoMenu);

		   System.out.println("Select option: ");
		   selectOption = collectInput.nextInt();
		   
		   
		   if (selectOption == 0) {
		   displayMainMenu();

		   System.out.println("Select option: ");
		   selectOption = collectInput.nextInt();
		   }
		   
		   if (selectOption == 7) {
		     String messageSettings = """
					      MESSAGE SETTINGS
					      1. Set 1
					      2. Common
					      0. Go back
					      """;

		      displayMenu(messageSettings);

		      System.out.println("Select option: ");
		       selectOption = collectInput.nextInt();
     

		      if (selectOption == 1) {
		         String messageSettingsOptionOne = """
							   SET 1
							   1. Message centre number
							   2. Message sent as
							   3. Message validity
							   0. Go back
							   """;

		      displayMenu(messageSettingsOptionOne);

		      System.out.println("Select option: ");
		      selectOption = collectInput.nextInt();

			if (selectOption == 0) {
			displayMenu(messageSettings);

		   	System.out.println("Select option: ");
		   	selectOption = collectInput.nextInt();
		   	}
		     }

		         else if (selectOption == 2) {
		            String messageSettingsOptionTwo = """
							      COMMON
							      1. Delivery reports
							      2. Reply via same centre
							      3. Character support
							      0. Go back
							      """;
		      
		           displayMenu(messageSettingsOptionTwo);

		      	   System.out.println("Select option: ");
		      	   selectOption = collectInput.nextInt();

			   if (selectOption == 0) {
			      displayMenu(messageSettings);

		   	   System.out.println("Select option: ");
		   	   selectOption = collectInput.nextInt();
			   } 
		        }
		        else if (selectOption == 0) {
		              displayMenu(caseTwoMenu);

		   	      System.out.println("Select option: ");
		   	      selectOption = collectInput.nextInt();
		        }

		        else {
		              System.out.print("invalid number");
		              System.out.println("enter valid number: ");
			      } 
		   }
		   
		break;

		



		}
	}

		
	}
	
}

