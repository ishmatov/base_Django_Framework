window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function (evt) {
        let t_href = evt.target();
        // console.log(t_href);
        // console.log(t_href.name); //ID корзины
        // console.log(t_href.value); //Кол-во товаров
        $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        });
        evt.preventDefault();
    })
}