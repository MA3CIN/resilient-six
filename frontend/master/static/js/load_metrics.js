$(document).ready(function() {
    let selectElement = $('#device');
    selectElement.change(function() {
        let selectedValue = $(this).val();
        let url = 'http://127.0.0.1:5000/metrics/device/' + selectedValue;
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                $('#metrics').empty();
                // datos recibidos
                $.each(data, function(index, item) {
                    let option = $('<option>');
                    option.val(item.id).text(item.name); 
                    $('#metrics').append(option); 
                });
            },
            error: function(xhr, status, error) {
                console.error('Error in aja xcall:', error);
            }
        });
    });
});