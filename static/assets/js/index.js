let swiperTestimonial = new Swiper(".spotlight_container", {
    slidesPerView: 4,
    spaceBetween: 25,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      }, loop: true });


let swiperBrand = new Swiper(".brands_section", {
    slidesPerView: 5,
    spaceBetween: 25,
    autoplay: {
    delay: 2500,
    disableOnInteraction: false,
    }, loop: true });


let swiperProduct = new Swiper(".product_data", {
    cssMode: true, loop: true, navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" },
    pagination: {el: ".swiper-pagination", clickable:true},
    slidesPerView: 4,
    clickable:true,
    spaceBetween: 10});

let swiperProductNew = new Swiper(".new_arrival", {
    cssMode: true, loop: true,
    pagination: {el: ".swiper-pagination"},
    navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" },
    slidesPerView: 3,
    clickable:true,
    spaceBetween: 50});

let swiperProductfeatured = new Swiper(".featured_pro", {
    cssMode: true, loop: true,
    pagination: {el: ".swiper-pagination"},
    navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" },
    slidesPerView: 4,
    clickable:true,
    spaceBetween: 10});



        const tabs = document.querySelectorAll('[data-tab-target]');
        const tabsContents = document.querySelectorAll('[data-tab-content]');
        
        tabs.forEach(tab => {
            tab.addEventListener('click', (e) => {
                const target = document.querySelector(tab.dataset.tabTarget);
        
                tabsContents.forEach(tabContent => {
                    tabContent.classList.remove('product_active');
        
                })
                
                target.classList.add('product_active');
                //loop through 'li' items and remove 'active' class
                tabs.forEach(tab => {
                      tab.classList.remove('product_active');
                  });
               //add 'active' class to clicked 'li' item
                e.target.classList.add("active-link");
        
                //remove 'active' class from all other 'li' items
                tabs.forEach(tab => {
                    if (tab !== e.target) {
                        tab.classList.remove('active-link');
                    }
                });
            })
        })



const modalViews = document.querySelectorAll(".product_modal");
modalBtns = document.querySelectorAll(".modal_button");
modalCloses = document.querySelectorAll(".modal_close");
let modal = function (modalClick) {
    modalViews[modalClick].classList.add("active-modal");
};
modalBtns.forEach((modalBtn, i) => {
    modalBtn.addEventListener("click", () => {
        modal(i);
    });
});
modalCloses.forEach((modalClose) => {
    modalClose.addEventListener("click", () => {
        modalViews.forEach((modalView) => {
            modalView.classList.remove("active-modal");
        });
    });
});


(function () {
    "use strict";
    var jQueryPlugin = (window.jQueryPlugin = function (ident, func) {
      return function (arg) {
        if (this.length > 1) {
          this.each(function () {
            var $this = $(this);

            if (!$this.data(ident)) {
              $this.data(ident, func($this, arg));
            }
          });

          return this;
        } else if (this.length === 1) {
          if (!this.data(ident)) {
            this.data(ident, func(this, arg));
          }

          return this.data(ident);
        }
      };
    });
  })();
  (function () {
    "use strict";
    function Guantity($root) {
      // const element = $root;
      // const quantity = $root.first("data-quantity");
      const quantity_target = $root.find("[data-quantity-target]");
      const quantity_minus = $root.find("[data-quantity-minus]");
      const quantity_plus = $root.find("[data-quantity-plus]");

      let button = document.getElementById("button-minus")
      var quantity_ = quantity_target.val();


      $(quantity_minus).click(function () {
          quantity_target.val(--quantity_)
          if (quantity_===1){
              button.classList.add("disable_button");
          }
      });

      $(quantity_plus).click(function () {
        quantity_target.val(++quantity_);
        if (quantity_>=1){
              button.classList.remove("disable_button");
          }
      });
    }
    $.fn.Guantity = jQueryPlugin("Guantity", Guantity);
    $("[data-quantity]").Guantity();
  })();
    var price1 = $('.prices').text();
    var price2 = parseFloat(price1);
  function calcPlus() {
    var quantity1 = document.getElementsByName('quantity')[0].value;

    console.log(quantity1)
    var quantity = parseFloat(quantity1)+1;
  var total = price2 * quantity;
  $('.prices').html( total +".00" );
}

    function calcMinus() {
    var quantity1 = document.getElementsByName('quantity')[0].value;
    var quantity = parseFloat(quantity1)-1;

  var total = price2 * quantity;
  console.log(total)
  $('.prices').html( total +".00" );

}

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}

$(document).ready(function()
		{
			var sub_width = 0;
			var sub_height = 0;
		 	$(".large").css("background","url('" + $(".small").attr("src") + "') no-repeat");

			$(".zoom-area").mousemove(function(e){
				if(!sub_width && !sub_height)
				{
					var image_object = new Image();
					image_object.src = $(".small").attr("src");
					sub_width = image_object.width;
					sub_height = image_object.height;
				}
				else
				{
					var magnify_position = $(this).offset();

					var mx = e.pageX - magnify_position.left;
					var my = e.pageY - magnify_position.top;

					if(mx < $(this).width() && my < $(this).height() && mx > 0 && my > 0)
					{
						$(".large").fadeIn(100);
					}
					else
					{
						$(".large").fadeOut(100);
					}
					if($(".large").is(":visible"))
					{
						var rx = Math.round(mx/$(".small").width()*sub_width - $(".large").width()/2)*-1;
						var ry = Math.round(my/$(".small").height()*sub_height - $(".large").height()/2)*-1;

						var bgp = rx + "px " + ry + "px";

						var px = mx - $(".large").width()/2;
						var py = my - $(".large").height()/2;

						$(".large").css({left: px, top: py, backgroundPosition: bgp});
					}
				}
			})
		})

