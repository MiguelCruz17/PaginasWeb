   // FUNCION QUE ME CARGA LOS DATOS DEL API

   async function CargarDatos(url) {

       datos = await fetch(url)
           .then(res => res.json())
           .then((data) => {
               return data
           });


       return datos;
   }

   // FUNCION PARA GUARDAR DATOS EN EL API

   async function EnviarDatos(url, metodo, data) {


       await fetch(url, {

           method: metodo,
           body: JSON.stringify(data),
           headers: {
               'Content-Type': 'application/json'
           }
       }).then(r => r.text()).then(r => {

           console.log(r);

       });
       return false;
   }