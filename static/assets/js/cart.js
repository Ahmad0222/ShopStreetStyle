
console.log('working')
if(localStorage.getItem('cart') == null)
{
var cart={};
}
else{
cart= JSON.parse(localStorage.getItem('cart'));
}

$('.cart').click(function(){
var idstr= this.id.toString();
$('#pr'+idstr).attr("class", "bottom clicked");
if(cart[idstr]!== undefined) {

}
else{
        qty = document.getElementById('qty'+idstr).value;
        console.log(qty);
        name = document.getElementById('name'+idstr).innerHTML;
        prCode = document.getElementById('prCode'+idstr).innerHTML;
        prSize= $('input[type=radio]:checked').val();
        console.log(prSize);
        price = document.getElementById('price'+idstr).innerHTML;
        cart[idstr] = [name, prSize, prCode, qty, price];
    }
localStorage.setItem('cart', JSON.stringify(cart));
document.getElementById('cart').innerHTML = Object.keys(cart).length;
console.log(cart)
});

$('.add-to-cart-btn').click(function(){
var idstr= this.id.toString();
$('#'+idstr).attr("class", "add-to-cart-btn add_Cart").text('Added To Cart');
if(cart[idstr]!== undefined) {

}
else{
        qty = document.getElementById('qty'+idstr).value;
        console.log(qty);
        name = document.getElementById('name'+idstr).innerHTML;
        prCode = document.getElementById('prCode'+idstr).innerHTML;
        prSize= $('input[type=radio]:checked').val();
        console.log(prSize);
        price = document.getElementById('price'+idstr).innerHTML;
        cart[idstr] = [name, prSize, prCode, qty, price];
    }
localStorage.setItem('cart', JSON.stringify(cart));
document.getElementById('cart').innerHTML = Object.keys(cart).length;
});

window.onload = function () {
    for (var idstr in cart){
        $('#pr'+idstr).attr("class", "bottom clicked");
        document.getElementById('cart').innerHTML = Object.keys(cart).length;
    }
};

$('.removeCart').click(function(){
    console.log('clicked');
    var idrm = this.id.toString();
    cart= JSON.parse(localStorage.getItem('cart'));
    delete cart[idrm]
    $('#pr'+idrm).attr("class", "bottom");
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
    localStorage.setItem('cart', JSON.stringify(cart));
});


