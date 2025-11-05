import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ej2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Ingrese el primer número:");
        double num1 = Double.parseDouble(br.readLine());
        System.out.println("Ingrese el segundo número:");
        double num2 = Double.parseDouble(br.readLine());
        System.out.println("El promedio es: " + ((num1 + num2) / 2));
    }
}