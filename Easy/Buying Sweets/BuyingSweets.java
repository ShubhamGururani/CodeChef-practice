import java.io.*;
import java.util.*;
class BuyingSweets{
	public static void main(String arg[]) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int x = Integer.parseInt(br.readLine());
		while(x > 0){
			String readLine = br.readLine();
        	String[] w = readLine.split(" ");
        	int notes = Integer.parseInt(w[0]);
        	int cost = Integer.parseInt(w[1]);
        	String a = br.readLine();
        	String[] ar = a.split(" ");
        	int min = 999999;
        	int sum = 0;
        	for (int i = 0; i < notes; i++) {
        		int number = Integer.parseInt(ar[i]);
        		sum += number;
        		if(number < min){
        			min = number;
        		}
       		}
       		if((sum - min)/cost == sum/cost){
       			System.out.println("-1");
       		}
       		else{
       			System.out.println(sum/cost);
       		}
       		x--;
		}
	}
}