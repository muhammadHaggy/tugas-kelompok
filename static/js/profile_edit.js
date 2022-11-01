function getFormData($form) {
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function (n, i) {
        indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
}

$('#edit-profile-form').submit(function (e) {
    e.preventDefault();
    var $form = $(this);
    var serializedData = $form.serializeArray();
    console.log(serializedData)
    $.ajax({
        url: "/user/profile/",
        type: 'POST',
        data: serializedData,
        dataType: 'text',
        success: function (data) {
            location.reload();
        }
    });
});

$('input').addClass('form-control')
$('textarea').addClass('form-control')

