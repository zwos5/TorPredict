import java.io.IOException;
import java.util.*;

public class Main
{
	public static void main(String[] args) {
	try {
		Bot x = new Bot();
		x.Chat();
	}
	catch(IOException e) {
        e.printStackTrace();
    }
	}
}