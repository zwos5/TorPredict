import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

class Bot {
    
    public static void Chat() throws IOException {
        Scanner sc = new Scanner(System.in);
        Scanner cont = new Scanner(System.in);
        
        char run;
        String input;
        
        List<String> prompts = new ArrayList<String>();
        List<String> responses = new ArrayList<String>();
        
        BufferedReader file = new BufferedReader(new FileReader("prompts.txt"));
        BufferedReader file2 = new BufferedReader(new FileReader("responses.txt"));
        
        String line1 = file.readLine();
        String line2 = file2.readLine();
        
        while (line1 != null) {
            prompts.add(line1);
            line1 = file.readLine();
        }
        
        while (line2 != null) {
            responses.add(line2);
            line2 = file2.readLine();
        }
        
        file.close();
        file2.close();
        
        String array[] = new String[prompts.size()];
        String array2[] = new String[responses.size()];
        
        for(int j = 0; j < prompts.size(); j++) {
            array[j] = prompts.get(j);
            array2[j] = responses.get(j);
        }
        /*for(int j = 0; j < array.length; j++) {
            System.out.println(array[j]);
            System.out.println(array2[j]);
        }*/ //Testing input from file.
        
        //System.out.println(array.length);
        //System.out.println(array2.length); Checking length
        
        System.out.print("====================[TORNADICS.AI]====================\n");
		System.out.print("Enter a prompt to get started. \n");
		
		do {
		    System.out.print("");
		    input = sc.nextLine();
            
            for(int i = 0; i <= array.length; i++) {
                    if(input.equalsIgnoreCase(array[i])) {
                        System.out.println(array2[i]);
                        break;
                    }
                    else if(input.equalsIgnoreCase("Show me a tornado chart") || input.equalsIgnoreCase("Show me a tornado chart.") ||
                        input.equalsIgnoreCase("Tornado chart") || input.equalsIgnoreCase("Tornado chart.")) {
                        TornadoChart x = new TornadoChart();
                        x.printChart();
                        break;
                    }
            }
            
            System.out.println("Want to continue? (y for Yes, n for No) ");
		    run = cont.next().charAt(0);
		}while(run != 'n');
    }
}