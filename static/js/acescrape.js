// Change script for Reddit box
$(document).ready(function () {
    $('.reddit').hide();
    $('#option1').show();
    $('#selectField').change(function () {
        $('.reddit').hide();
        $('#'+$(this).val()).show();
    });
});