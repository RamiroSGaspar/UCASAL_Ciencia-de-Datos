import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ej7 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Ingrese un número:");
        double numero = Double.parseDouble(br.readLine());
        numero = numero * 0.85;
        System.out.println("Resultado: " + numero);
    }
}