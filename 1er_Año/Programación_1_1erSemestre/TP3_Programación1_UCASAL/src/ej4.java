import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ej4 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Ingrese su edad:");
        int edad = Integer.parseInt(br.readLine());
        System.out.println(edad >= 18 ? "Eres mayor de edad" : "No eres mayor de edad");
    }
}