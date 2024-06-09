const form = document.getElementById('myForm');
    form.addEventListener('submit', async (event) => {
        // event.preventDefault(); // Prevenir el envío predeterminado del formulario

        // Obtener los valores de los campos del formulario
        const formData = new FormData(form);
        const data = {};
        for (const [key, value] of formData.entries()) {
            data[key] = value;
        }

        // Enviar los datos como JSON mediante fetch
        const response = await fetch('/models/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Manejar la respuesta del servidor
        // Redirigir a la página deseada después de enviar los datos correctamente
        // window.location.href = '/';
    });