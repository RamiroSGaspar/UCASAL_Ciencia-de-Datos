import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ej20 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Ingrese N:");
        int N = Integer.parseInt(br.readLine());
        System.out.println("Ingrese P (mayor que N):");
        int P = Integer.parseInt(br.readLine());

        if (P > N) {
            while (P >= N) {
                System.out.println(P);
                P--;
            }
        } else {
            System.out.println("P debe ser mayor que N!");
        }
    }
}