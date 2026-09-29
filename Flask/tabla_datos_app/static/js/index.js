document.addEventListener("DOMContentLoaded", function () {

    const filtroPais = document.getElementById("filtroPais");
    const ordenarPor = document.getElementById("ordenarPor");
    const direccion = document.getElementById("direccion");

    const tabla = document.getElementById("tablaPlataforma");
    const conteo = document.getElementById("conteoPlataforma");


    //CONVERTIR VALORES DEL DICCIONARIO

    function convertirUsuarios(valor) {

        if (valor.includes("B")) {
            return parseFloat(valor) * 1000000000;
        }

        if (valor.includes("M")) {
            return parseFloat(valor) * 1000000;
        }

        return parseFloat(valor);
    }


    function actualizarTabla() {

        const filas = Array.from(tabla.querySelectorAll("tr"));

        const pais = filtroPais.value;
        const orden = ordenarPor.value;
        const dir = direccion.value;


        // FILTRAR
        filas.forEach(fila => {

            if (
                pais === "all" ||
                fila.dataset.country === pais
            ) {
                fila.style.display = "";
            } else {
                fila.style.display = "none";
            }

        });


        // ORDENAR
        filas.sort((a, b) => {

            let valorA;
            let valorB;


            if (orden === "nombre") {

                valorA = a.dataset.name.toLowerCase();
                valorB = b.dataset.name.toLowerCase();

            }


            if (orden === "fundacion") {

                valorA = Number(a.dataset.year);
                valorB = Number(b.dataset.year);

            }


            if (orden === "pais") {

                valorA = a.dataset.country.toLowerCase();
                valorB = b.dataset.country.toLowerCase();

            }


            if (orden === "usuarios") {

                valorA = convertirUsuarios(a.dataset.users);
                valorB = convertirUsuarios(b.dataset.users);

            }


            if (valorA < valorB) {
                return dir === "asc" ? -1 : 1;
            }

            if (valorA > valorB) {
                return dir === "asc" ? 1 : -1;
            }

            return 0;
        });


        filas.forEach(fila => {
            tabla.appendChild(fila);
        });


        const visibles = filas.filter(
            fila => fila.style.display !== "none"
        );

        conteo.textContent = visibles.length;
    }


    filtroPais.addEventListener("change", actualizarTabla);
    ordenarPor.addEventListener("change", actualizarTabla);
    direccion.addEventListener("change", actualizarTabla);



    // DETALLES
    const botones = document.querySelectorAll(".botonDetalle");

    botones.forEach(boton => {

        boton.addEventListener("click", function () {

            document.getElementById("modalName").textContent =
                boton.dataset.name;

            document.getElementById("modalUsers").textContent =
                boton.dataset.users;

            document.getElementById("modalYear").textContent =
                boton.dataset.year;

            document.getElementById("modalCountry").textContent =
                boton.dataset.country;
        });

    });

});