import java.io.*;
class Malvika{
	public static void main(String arg[]) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int x = Integer.parseInt(br.readLine());
		while(x > 0){
			String s = br.readLine();
			int countA = 0;
			int countB = 0;
			for(int i = 0; i < s.length(); i++){
				char c = s.charAt(i);
				if (c == 'a')
					countA++;
				else
					countB++;
			}
			if (countA > countB)
				System.out.println(countB);
			else
				System.out.println(countA);
			x--;
		}
	}
}