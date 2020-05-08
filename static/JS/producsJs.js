$(document).ready(function () {
    console.log('MAMMMMAaaaaaaaaaaaaaa');
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/?searchFilter='+searchText,
            type: 'GET',
            success: function (resp) {
                var newHtml = resp.data.map(d =>{
                    return `<div class="well product">
                              <a href="/"${d.id}>
                                    <img class="product-img" src="${d.image}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.name}</p>
                              </a>
                            </div>`

                });
                $('.content').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                // TODO: Show toster or better.
                console.error(error);

            }
        })
    });
});