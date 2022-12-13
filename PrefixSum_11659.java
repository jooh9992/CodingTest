import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int D = sc.nextInt();
        int Q = sc.nextInt();
        
        int arr[] = new int[D+1];
        arr[0] = 0;
        for(int i =1; i<=D; i++){
            arr[i] = arr[i-1] + sc.nextInt();
        }
        for(int j =0; j<Q; j++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            
            System.out.println(arr[b]-arr[a-1]);
        }
    }
}