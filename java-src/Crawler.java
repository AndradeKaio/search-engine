import java.io.*;
import java.net.URL;



public class Crawler{

	public static void main(String [] args)throws Exception{
		URL url = new URL("https://www.google.com");
		File file = new File("teste.html");
		BufferedReader in = new BufferedReader(
        		new InputStreamReader(url.openStream()));
	
	}
}
