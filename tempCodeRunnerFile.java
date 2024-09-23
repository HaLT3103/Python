import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        while (T-- > 0) {
            long n = scanner.nextLong();
            System.out.println(isFibonacci(n) ? "YES" : "NO");
        }
    }

    private static boolean isFibonacci(long n) {
        long a = 0, b = 1;
        while (a < n) {
            long temp = a + b;
            a = b;
            b = temp;
        }
        return a == n;
    }
}
