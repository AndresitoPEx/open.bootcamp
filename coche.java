public class Main {
    public static void main(String[] args) {
        Coche miCoche = new Coche();
        miCoche.AumentarPuertas();

        System.out.println("Mi coche tiene "+ miCoche.puertas +" puertas");
    }
    
}

class Coche{
    public int puertas = 4;
    
    public void AumentarPuertas(){
        this.puertas++;
    }
    
}