// Change script for Reddit box
$(document).ready(function () {
    $('.reddit').hide();
    $('#reddit1').show();
    $('#selectField-reddit').change(function () {
        $('.reddit').hide();
        $('#'+$(this).val()).show();
    });
});

// Change script for TechCrunch box
$(document).ready(function () {
    $('.techcrunch').hide();
    $('#techcrunch1').show();
    $('#selectField-techcrunch').change(function () {
        $('.techcrunch').hide();
        $('#'+$(this).val()).show();
    });
});


