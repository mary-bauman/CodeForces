import java.util.Scanner;

public class D {
    public static void main(String[] args) throws Exception {
       Scanner input = new Scanner(System.in);
       int t = input.nextInt();
       for (int i = 0; i < t; i++){
        int n = input.nextInt();
        int k = 1;
        while (k<<1 <= n) k <<= 1;
        System.out.println(k-1);
       }
    }
}