// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class HelloWorld {
    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.edad = 22;
        System.out.println(cliente.edad);
        cliente.nombre = "Gabriel";
        System.out.println(cliente.nombre);
        cliente.telefono = 123456789;
        System.out.println(cliente.telefono);
        cliente.credito = 10000;
        System.out.println(cliente.credito);
        
        Trabajador trabajador = new Trabajador();
        trabajador.edad = 23;
        System.out.println(trabajador.edad);
        trabajador.nombre = "Antonio";
        System.out.println(trabajador.nombre);
        trabajador.telefono = 987654321;
        System.out.println(trabajador.telefono);
        trabajador.salario = 20000;
        System.out.println(trabajador.salario);
        
    }
}

class Persona{
    int edad;
    String nombre;
    int telefono;
    
}

class Cliente extends Persona{
    int credito;
}

class Trabajador extends Persona{
    int salario;
}