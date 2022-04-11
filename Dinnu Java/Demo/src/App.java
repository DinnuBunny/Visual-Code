public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");

        int n = 6;

        for(int i=0; i<n; i++){
            for(int j=0; j<=i; j++){
                System.out.print("* ");
            }
            System.out.println();
        }
        int summ = greet(10,20);
        System.out.println(summ+20);
    }

    public static int greet(int a, int b){
            int z = a + b;
            return z;
    }
}
