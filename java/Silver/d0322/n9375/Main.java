package d0322.n9375;

import java.io.*;
import java.util.*;
import java.util.Map.*;

public class Main {
	
	static int T, N;
	static HashSet<String> set;
	static HashMap<String,Integer> hm;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		T = Integer.parseInt(br.readLine());
		
		for(int t=0;t<T;t++) {
			N = Integer.parseInt(br.readLine());
			
			set = new HashSet<>();
			hm = new HashMap<>();
			
			for(int i=0;i<N;i++) {
				st = new StringTokenizer(br.readLine());
				String name = st.nextToken();
				String type = st.nextToken();
				
				if(set.contains(name)) continue;
				
				if(hm.containsKey(type)) hm.replace(type, hm.get(type)+1);
				else hm.put(type, 1);
			}
			
			int answer = 1;
			for(Entry<String, Integer> entry : hm.entrySet()) {
				answer*=(entry.getValue()+1);
			}
			answer--; // 모든 것을 선택하지 않을 경우의 수
			sb.append(answer).append("\n");
		}
		
		System.out.println(sb.toString());
	}

}
