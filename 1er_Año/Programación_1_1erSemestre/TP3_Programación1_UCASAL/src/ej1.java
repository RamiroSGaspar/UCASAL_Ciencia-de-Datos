import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ej1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Ingrese el primer número:");
        int num1 = Integer.parseInt(br.readLine());
        System.out.println("Ingrese el segundo número:");
        int num2 = Integer.parseInt(br.readLine());
        System.out.println("La suma es: " + (num1 + num2));
    }
}