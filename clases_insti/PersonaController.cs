using Microsoft.AspNetCore.Mvc;
using apixd.Entities;

namespace demo1.Controllers
{

    [Route("/personas")]
    public class PersonController : ControllerBase
    {

        private List<Persona> personas = new List<Persona> {
            new Persona { id = 1,  nombres = "Joseph" , apellidos = "Ibn Alguien"},
            new Persona { id = 2, nombres = "Maria" , apellidos = "Ibn Alguien"},
            new Persona { id = 3, nombres = "Joshua" , apellidos = "Ibn Joseph" }

        };

        [HttpGet]
        [Route("")]
        public ActionResult GetPersonas()
        {.
            return Ok(this.personas); // HTTP status code 200ss
        }

        [HttpPost]
        [Route("")]
        public ActionResult CrearPersona([FromBody] Persona dato)
        {
            this.personas.Add(dato);
            return Ok(this.personas);
        }

        [HttpPut]
        [Route("{personaId}")]
        public ActionResult ActualizarPersona(
            [FromRoute] int personaId,
            [FromBody] Persona dato
        )
        {
            // lambda ** pra el crush
            Persona? persona = this.personas
                .Where(per => per.id == personaId).FirstOrDefault();
            if (persona == null)
            {
                return NotFound();
            }
            // actualizamos
            persona.nombres = dato.nombres;
            persona.apellidos = dato.apellidos;
            persona.numeroDocumento = dato.numeroDocumento;
            persona.fechaNacimiento = dato.fechaNacimiento;
            //retorno la persona modificada
            return Ok(persona);
        }

        [HttpDelete]
        [Route("{personaId}")]
        public ActionResult EliminarPersona(
            [FromRoute] int personaId
        )
        {
            // lambda ** pra el crush
            Persona? persona = this.personas
                .Where(per => per.id == personaId).FirstOrDefault();
            if (persona == null)
            {
                return NotFound();
            }
            // eliminamos
            int index = -1;
            for (int i = 0; i < this.personas.Count(); i++)
            {
                if (this.personas[i].id == personaId)
                {
                    index = 1;
                    break;
                }
            }
            this.personas.RemoveAt(index);
            //retorno la persona modificada
            return Ok(personas);
        }


    }

}