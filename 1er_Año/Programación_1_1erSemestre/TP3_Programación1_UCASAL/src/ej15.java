import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ej15 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double suma = 0;
        double producto = 1;

        for (int i = 1; i <= 5; i++) {
            System.out.println("Ingrese número " + i + ":");
            double num = Double.parseDouble(br.readLine());
            suma += num;
            producto *= num;
        }

        System.out.println("Suma total: " + suma);
        System.out.println("Producto total: " + producto);
    }
}