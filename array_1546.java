import java.util.*; //util 디렉토리 안에 있는 모든 클래스를 임포트

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); //과목의 개수 지정
        int A[] = new int[N]; //점수 배열 생성
        for(int i=0; i<N; i++){
            A[i] = sc.nextInt(); //배열에 점수 저장
        }
        long sum =0; //합계 변수 생성
        long max =0; //최대값 변수 생성
        
        for(int i=0; i<N; i++){
            if(A[i]>max) max = A[i]; //최대값 지정
            sum += A[i]; //총합 지정
        }
        System.out.print(sum*100.0/max/N); //결과 출력
    }
}