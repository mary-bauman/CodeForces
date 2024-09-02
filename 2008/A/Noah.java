import java.util.Scanner;
import java.io.File;

public class Noah {
   public static void main(String[] args) throws Exception {
      Scanner input = new Scanner(System.in);
      // first int = number of test cases
      int cases = input.nextInt();
      int numOnes = 0; int numTwos = 0;
      boolean zeroesOut = false;
      // loop through input
      for (int i = 0; i < cases; i++) {
         // grab a (# of ones) and b (# of twos)
         numOnes = input.nextInt(); numTwos = input.nextInt();
         zeroesOut = cancels(numOnes, numTwos);
         if (zeroesOut) System.out.println("yes");
         else System.out.println("no");
      }
   }

   // returns true if ones and twos cancel, false if they don't
   public static boolean cancels(int ones, int twos) {
      if (ones % 2 != 0) return false; // odd number of ones
      else if (twos % 2 == 0) return true; // even number of twos
      int extraOnes = ones - (2 *(twos % 2)); // ones left after cancelling out twos
      if (extraOnes % 2 != 0 || extraOnes < 0) return false; // negative or odd # of ones after twos cancel
      else return true;
   }
}