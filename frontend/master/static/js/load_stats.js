document.getElementById('my-form').addEventListener('submit', function(event) {
    // Obtener el texto seleccionado de 'device'
    var deviceSelect = document.getElementById('device');
    var deviceText = deviceSelect.options[deviceSelect.selectedIndex].text;
    document.getElementById('device_text').value = deviceText;

    // Obtener el texto seleccionado de 'metrics'
    var metricsSelect = document.getElementById('metrics');
    var metricsText = metricsSelect.options[metricsSelect.selectedIndex].text;
    document.getElementById('metrics_text').value = metricsText;
});