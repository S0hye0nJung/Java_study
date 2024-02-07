package programmers;

import java.util.Scanner;

public class Pro24_02_07 {

	public static void main(String[] args) {
		///2024.02.07 문제풀이(Day3)- 기초 부분
		
		//1. 문자열 섞기
//		class Solution {
//		    public String solution(String str1, String str2) {
//		        String answer = "";
//		        for(int i =0; i< ((int) str1.length() +(int) str2.length() );i++){
//		            if(i==0){
//		                answer+= str1.charAt(i);
//		            }else if(i%2 !=0){ //홀수
//		                if(i==1){
//		                    answer+= str2.charAt(i-1);
//		                }else{
//		                int a =(i-1)/2 ;
//		                answer+= str2.charAt(a);
//		                }
//		            }else{ //짝수
//		                int b =i/2;
//		                answer+= str1.charAt(b);
//		                
//		            }
//		        }
//		        return answer;
//		    }
//		}
//		
//		
		
		
      
//		//2. 문자 리스트를 문자열로 변환하기
//		class Solution {
//		    public String solution(String[] arr) {
//		        String answer = "";
//		        for (int i=0; i< arr.length; i++){
//		            answer+= arr[i];
//		        }
//		        return answer;
//		    }
//		}
//		
		
		
		
//		//3. 문자열 곱하기
//		class Solution {
//		    public String solution(String my_string, int k) {
//		        String answer = "";
//		        for (int i=0; i<k; i++){
//		            answer +=my_string;
//		        }
//		        return answer;
//		    }
//		}
//		
		
		
		
//		//4. 더 크게 합치기
//		class Solution {
//		    public int solution(int a, int b) {
//		        int answer = 0;
//		        String str1 = a +""+b;
//		        String str2 =b+""+a;
//		        String result="";
//		        if(Integer.parseInt(str1) >  Integer.parseInt(str2)){
//		            answer =Integer.parseInt(str1);
//		        }else{
//		            answer =Integer.parseInt(str2);
//		            
//		        }
//		        return answer; 
//		    }
//		}
//		
		
		
		
		//5. 두 수의 연산값 비교하기
//		class Solution {
//		    public int solution(int a, int b) {
//		        int answer = 0;
//		    
//		        int plus =Integer.parseInt(a+""+b); 
//		        int multi = 2*a*b;
//		        if(plus > multi){
//		            answer = plus;
//		        }else{
//		            answer = multi;
//		        }
//		        return answer;
//		    }
//		}
//		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

	}//void메소드 end


	}//class end
