class Main {
    public static void main(String[] args) {
    
    Persona human = new Persona();
    human.setEdad(32);
    human.setNombre("Jorge");
    human.setNumero(930172021);
    
    System.out.println("edad: " + human.getEdad());
    System.out.println("nombre:" + human.getNombre());
    System.out.println("numero: " + human.getNumero());
    }
}

class Persona{
    private int edad;
    private String nombre;
    private int numero;
    
    public void setEdad(int edad){
        this.edad = edad;
    }
    
    public int getEdad(){
        return this.edad;
    }
    
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    
    public String getNombre(){
        return this.nombre;
    }
    
    public void setNumero(int numero){
        this.numero = numero;
    }
    
    public int getNumero(){
        return this.numero;
    }
}