import java.io.*;
class LuckyLong{
	public static void main(String arg[]) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		while(n > 0){
			String s = br.readLine();
			int count = 0;
			for(int i = 0;i <s.length(); i++){
				if (s.charAt(i) !='4' && s.charAt(i) != '7'){
					count++;
				}
			}
			System.out.println(count);
			n--;
		}
	}
}