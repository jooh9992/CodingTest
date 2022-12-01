import java.util.*; //util 디렉토리 안에 있는 모든 클래스를 임포트

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);//값 읽어는 scanner 생성
        int n = sc.nextInt(); //int형 값 읽어오기
        
        String num = sc.next();//string형 값 읽어오기
        char[] cnum = num.toCharArray(); //문자 배열로 변환
        int sum =0; //합 변수 선언
        
        for(int i =0; i<cnum.length; i++){
            sum += cnum[i] - '0'; //배열길이만큼 숫자형으로 변환해서 합하기
        }
        System.out.print(sum); //합 출력
    }
}