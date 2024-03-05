package programmers;

public class Day_5 {

	public static void main(String[] args) {
		// ///2024.02.13 문제풀이(Day5)- 기초 부분
		
		//1. 코드 처리하기 =>하다가 
		class Solution {
		    public String solution(String code) {
		        String answer = "";
		        int mode=0;
		     if(code.isEmpty()) {
		        	answer+= "EMPTY";
		    }else {
		    	 for(int i=0; i< code.length();i++){
			    	if(mode==0) {
			    		if(code.charAt(i)=='1') {
			    			mode=1;
			    			}else {if(i%2==0) {
			    				answer+= code.charAt(i);
			    			}}
			    	}else {
			    		if(code.charAt(i)=='1') {
			    			mode=0;
			    		}else {if(i%2==1) {
			    				answer+= code.charAt(i);
			    			}}}}//for end
		    		} 
		     return answer; 
		            }}
		    
		    
				
				


		
		
		
		

		//2. 등차수열의 특정한 항만 더하기
//		class Solution {
//		    public int solution(int a, int d, boolean[] included) {
//		        int answer=0;
//		        for(int i=0; i< included.length;i++){
//		            if(included[i]){
//		            answer+= a+ i*d;}
//		            
//		            }
//		        return answer;
//		    }
//		}
		
		
		
		
		
//		
//		//3. 주사위 게임 2
//		class Solution {
//		    public double solution(int a, int b, int c) {
//		        double answer = 0;
//		        
//		        if(a!=c && a!=b && b!=c){
//		            answer =a+b+c;
//		        }else if((a==b && a!=c && b!=c) || (a==c && a!=b && b!=c) ||(c==b && a!=c && b!=a)){
//		            answer =(a+b+c)*(Math.pow(a,2) +Math.pow(b,2) +Math.pow(c,2) );
//		        
//		    }else if(a==b && b==c && c==a){
//		           answer =(a+b+c)*(Math.pow(a,2) +Math.pow(b,2) +Math.pow(c,2))*( Math.pow(a,3) +Math.pow(b,3) +Math.pow(c,3));
//		        }return answer;
//		}}
//		
		
		
		
		
		
//		//4. 원소들의 곱과 합
//		class Solution {
//		    public int solution(int[] num_list) {
//		        int answer = 0;
//		        int mult =1;
//		        int sum=0;
//		        for(int i=0;i<num_list.length;i++){
//		            sum += num_list[i];
//		            mult*= num_list[i];
//		        }
//		        if(Math.pow(sum,2) >mult){
//		            answer= 1;
//		        }else{
//		            answer=0;
//		        }
//		        return answer;}}
		
		
		
		
		
//		//5.이어 붙인 수
//		class Solution {
//		    public int solution(int[] num_list) {
//		        String odd = "";
//		        String even = "";
//		        int answer=0;
//		        for(int i=0; i<num_list.length; i++){
//		            if((num_list[i])%2==0){
//		                even += num_list[i];
//		            }else{
//		            odd += num_list[i]; }}
//		        
//		        answer = Integer.parseInt(odd) +Integer.parseInt(even);
//		        return answer; 
//		    }
//		}
//		
		
		
		
		
	}//main end

}//class end
