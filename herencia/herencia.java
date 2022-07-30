class HelloWorld {
    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.edad = 22;
        System.out.println(cliente.edad);
        cliente.nombre = "Gabriel";
        System.out.println(cliente.nombre);
        cliente.telefono = 123456789;
        System.out.println(cliente.telefono);
        
        Trabajador trabajador = new Trabajador();
        trabajador.edad = 23;
        System.out.println(trabajador.edad);
        trabajador.nombre = "Antonio";
        System.out.println(trabajador.nombre);
        trabajador.telefono = 987654321;
        System.out.println(trabajador.telefono);
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