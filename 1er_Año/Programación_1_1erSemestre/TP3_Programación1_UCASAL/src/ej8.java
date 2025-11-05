import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ej8 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Ingrese un número entero:");
        int num = Integer.parseInt(br.readLine());
        System.out.println(num % 2 == 0 ? "Es par" : "No es par");
    }
}