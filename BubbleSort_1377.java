import java.io.*;
import java.util.Arrays;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        B[] arr = new B[n];
        for (int i = 0; i < n; i++) {
            arr[i] = new B(Integer.parseInt(br.readLine()), i);
        }
        br.close();
        
        Arrays.sort(arr);
        int Max =0;
        
        for(int i=0; i<n; i++){
            if(Max < arr[i].idx-i)
                Max = arr[i].idx - i;
        }
        System.out.println(Max+1);
    }
}

class B implements Comparable<B>{
    int val;
    int idx;
    
    public B(int val, int idx){
        super();
        this.val = val;
        this.idx = idx;
    }
    @Override
    public int compareTo(B o){ //val 기준 오름차순 정렬하기
        return this.val - o.val;
    }
}
