$(document).ready(function() {

    const neighborhoodData = JSON.parse($('#neighborhood-data').attr('data-neighborhoods'));


    $('#district').change(function() {
        const selectedDistrict = $(this).val();
        updateNeighborhoods(selectedDistrict);
    });


    function updateNeighborhoods(district) {

        $('#neighborhood').empty();
        $('#neighborhood').append('<option value="">Mahalle Seçin</option>');


        if (district && neighborhoodData[district]) {
            const neighborhoods = neighborhoodData[district];


            neighborhoods.sort();


            $.each(neighborhoods, function(i, neighborhood) {
                $('#neighborhood').append(
                    $('<option></option>').val(neighborhood).text(neighborhood)
                );
            });
        }
    }


    $('#prediction-form').submit(function(e) {
        e.preventDefault();


        $('#result-card').addClass('d-none');
        $('#error-alert').addClass('d-none');


        const formData = $(this).serialize();


        $.ajax({
            type: 'POST',
            url: '/predict',
            data: formData,
            success: function(response) {
                if (response.success) {

                    $('#prediction-result').text(response.prediction);
                    $('#result-card').removeClass('d-none');


                    $('html, body').animate({
                        scrollTop: $('#result-card').offset().top - 20
                    }, 500);
                } else {

                    $('#error-alert').removeClass('d-none').text(response.error);
                }
            },
            error: function() {

                $('#error-alert').removeClass('d-none');
            }
        });
    });

    const initialDistrict = $('#district').val();
    if (initialDistrict) {
        updateNeighborhoods(initialDistrict);
    }
});