import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ej3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Ingrese la base del triángulo:");
        double base = Double.parseDouble(br.readLine());
        System.out.println("Ingrese la altura del triángulo:");
        double altura = Double.parseDouble(br.readLine());
        System.out.println("El área es: " + (base * altura / 2));
    }
}