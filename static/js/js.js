// JavaScript Document

//display responsive menu
function screenMenu(){
    var w = $(document).width();
    var v = $("#categoryMenucontent").css("visibility")
    if (w < 769){
        if(v == "visible"){
            $("#categoryMenucontent").css("visibility","hidden")
            $("#categoryMenucontent").css("display","none")
            $(".menuItems").css("display","none")
        }else{
            $(".menuItems").css("-moz-transition","all 0.3s")
            $(".menuItems").css("-webkit-transition","all 0.3s")
            $(".menuItems").css("transition","all 0.3s")
            $("#categoryMenucontent").css("visibility","visible")
            $("#categoryMenucontent").css("display","block")
            $("#categoryMenucontent").css("z-index","9999")
            $(".menuItems").css("display","block")
            $(".menuItems").css("margin-bottom","22px")
            $(".menuItems").css("border-bottom","solid thin lightgray")
        }
    }
}


/***********slide show categories on tablettes page*************/
var arr = [];
arr[0]= new Image();
arr[0].src = "/theme_chocolat/static/images/1.png";

arr[1]= new Image();
arr[1].src = "/theme_chocolat/static/images/2.png";

arr[2]= new Image();
arr[2].src = "/theme_chocolat/static/images/3.png";

arr[3]= new Image();
arr[3].src = "/theme_chocolat/static/images/4.png";

arr[4]= new Image();
arr[4].src = "/theme_chocolat/static/images/tablettes.jpg";

var i=0;
var f = 0;

function slide(){
 

/*i++;
 document.getElementById("bann").src= arr[f].src;
 if(f==arr.length){
  i=0;
 }

 f+=1;*/

 document.getElementById("bann").src= arr[f].src;
 if(f==4){
      f=0;
     }
 f+=1;
//comment this to disable auto slideing
 //setTimeout(function(){slide()}, 5000)
}


function showAddr(){
    $('.shop_addr').css('visibility', 'visible')
}
function hideAddr(){
    $('.shop_addr').css('visibility', 'hidden')
}

//change background image banner for each categories
function changeBg() {
    var pathname = window.location.pathname; // Returns path only
    var url      = window.location.href;     // Returns full URL

    var sCategorie = '<div class="tablette-menu">'
    //sCategorie += '<div class="tab-trie">Filtrer par gamme</div>'
    sCategorie += '<div class="taBlette-gamme"> <a href="/shop/category/tablettes-authentique-18" id="auth"> Authentique </a></div>'
    sCategorie += '<div class="taBlette-gamme last-a"> <a href="/shop/category/tablettes-surfine-19" id="surf"> Surfine </a></div>'
    sCategorie += '<div class="taBlette-gamme"> <a href="/shop/category/tablettes-exclusive-22" id="exclu"> Exclusive </a></div>'
    sCategorie += '<div class="taBlette-gamme last-a"> <a href="/shop/category/tablettes-13"> Tous </a></div>'
    sCategorie += '</div>'

    var sPro = '<div class="tablette-menu">'
    sPro += '<div class="taBlette-gamme last-a"> <a href="/shop/category/matieres-premieres-surfine-24" id="surf"> Surfine </a></div>'
    sPro += '<div class="taBlette-gamme last-a"> <a href="/shop/category/tablettes-13"> Tous </a></div>'
    sPro += '</div>'

    var sPortal = '<div class="tablette-menu">'
    sPortal += '<div class="" style="display:inline;"> <a href="home" id="surf"> <span class="fa fa-home fa-2x"></span></a></div>'
        sPortal += '<div class="taBlette-gamme" style="width:240px;"> <a href="quotes" id="surf"> Vos devis </a></div>'
        sPortal += '<div class="taBlette-gamme" style="width:240px;"> <a href="orders" id="surf"> Vos commandes </a></div>'
        sPortal += '<div class="taBlette-gamme" style="width:240px;"> <a href="invoices" id="surf"> Vos factures et payements </a></div>'
        sPortal += '</div>'

    var cat1 = "tablettes-13"
    var cat2 = "confiseries-et-coffrets-14"
    var cat3 = "bio-15"
    var cat4 = "matieres-premieres-16"
    var cat5 = "aterlier-c-17"

    var cat7 = "tablettes-exclusive-22"
    var cat6 = "tablettes-authentique-18"
    var cat8 = "tablettes-surfine-19"
    
    var cat9 = "selections-23"  
    var cat10 = "confirmation"
    var cat11 = "aterlier-c"

    var cat14 = "quotes"
    var cat15 = "orders"
    var cat16 = "invoices"

    // find word on the url
    var c1 = url.search(cat1);
    var c2 = url.search(cat2);
    var c3 = url.search(cat3);
    var c4 = url.search(cat4);
    var c5 = url.search(cat5);

    var c6 = url.search(cat6);
    var c7 = url.search(cat7);
    var c8 = url.search(cat8);

    var c9 = url.search(cat9);
    var c10 = url.search(cat10);
    var c11 = url.search(cat11);

    var c14 = url.search(cat14);
    var c15 = url.search(cat15);
    var c16 = url.search(cat16);



    if(c1 > 3){
        //document.write('<a href="/shop/category/tablettes-13"> <img id=\"bann\" src=\"/theme_chocolat/static/images/tablettes--.jpg\"\></img> </a>')
        document.write(sCategorie)
        $('#tab .fa').css('color', '#924537')
        $('.slidePos').css('margin', '11.6% -1.6% 0px 0%') 
        $('.products_pager').css('margin-top', '-20%')
    }
    
    if(c2 > 3){
        //document.write('<img id=\"bann\" src=\"/theme_chocolat/static/images/confiserie.jpg\"\></img>')
        $('#confie .fa').css('color', 'rgb(4, 126, 175)')
    }


    if(c3 > 3){
        //document.write('<img id=\"bann\" src=\"/theme_chocolat/static/images/bio.jpg\"\></img>')
        //$('#bio').css('background-color', '#239B56')
        $('#bio .fa').css('color', '#8fc647')
    }

    if(c4 > 3){
        //document.write('<img id=\"bann\" src=\"/theme_chocolat/static/images/matiere-premieres.jpg\"\></img>')
        document.write(sPro)
        $('#matiere .fa').css('color', 'rgb(230, 142, 4)')
        $('.slidePos').css('margin', '11.6% -1.6% 0px 0%') 
        $('.products_pager').css('margin-top', '-20%')
    }

    if(c5 > 3)
        //document.write('<img id=\"bann\" src=\"/theme_chocolat/static/images/atelierC.jpg\"\></img>')
        ;



    if(c6 > 3){
            document.write(sCategorie)
            $('#auth').css('font-weight', 'bold')
            $('#tab .fa').css('color', '#924537')
            $('.slidePos').css('margin', '11.6% -1.6% 0px 0%')
    }
    if(c7 > 3){
            document.write(sCategorie)
            $('#exclu').css('font-weight', 'bold')
            $('#tab .fa').css('color', '#924537')
            $('.slidePos').css('margin', '11.6% -1.6% 0px 0%')
    }
    if(c8 > 3){
            document.write(sCategorie)
            $('#surf').css('font-weight', 'bold')
            $('#tab .fa').css('color', '#924537')
            $('.slidePos').css('margin', '11.6% -1.6% 0px 0%')
    }

    if(c9 > 3){
        ;
    }

    if(c10 > 3)
        $('#checker1').css('visibility', 'hidden')

    if (c11 > 3 )
        $('#atelierC .fa').css('color', '#968a74')

    if (c14 > 2 || c15 > 2 || c16 > 2)
        document.write(sPortal)
    
}


//hide brand text on small screen device
function hideBrandText(){
    //alert(0)

    if(screen.width < 1000)
        document.getElementByClass("brandTxt").style.display = "none"

}   


/**************** the next func allow user to stay on the current url after clicking on addToCard icon on product************************/
function dinamycPurchase(){
    //get the current URL
    var pathname = window.location.pathname; // Returns path only
    var url      = window.location.href;     // Returns full URL

    alert(url)

}

/***********go to last page on product purchased checkout****************/
function goBack() {
    window.history.back();
}

/************************popUP express************************/
var popTxt;

// set popItems value
function getPop(obj_id){
    popTxt = '<li class="liPopUP"> <div style="width:60px; height:60px">' + pImage[obj_id] + '</div>Produits ajouté dans le panier</li>';
}

/**************get client browser type***************/
function detectIE() {
  var ua = window.navigator.userAgent;

  var msie = ua.indexOf('MSIE ');
  if (msie > 0) {
    // IE 10 or older => return version number
    return parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10);
  }

  var trident = ua.indexOf('Trident/');
  if (trident > 0) {
    // IE 11 => return version number
    var rv = ua.indexOf('rv:');
    return parseInt(ua.substring(rv + 3, ua.indexOf('.', rv)), 10);
  }

  var edge = ua.indexOf('Edge/');
  if (edge > 0) {
    // Edge (IE 12+) => return version number
    return parseInt(ua.substring(edge + 5, ua.indexOf('.', edge)), 10);
  }

  // other browser
  return false;
}

//adjusting footer for ie/edge browser
function getBrowse(obj){

    if (obj === false) {
        //ON OTHER BROWSER DO NOTHING
        ;
    } else if (obj >= 12) {
        // IF EDGE BROWSER
      $('footer').css('display', 'block')
    } else {
        //if IE BROWSER
      $('footer').css('display', 'block')
    }

}

/****************put mention legal script here************************/
function showMento(){
    $('#mentioLegalContainer').css('visibility', 'visible')
}

function showButs(){
    if(screen.width <= 800)
        $('#valideForm').css('visibility', 'visible')
    else
        $('#valideForm').css('visibility', 'hidden')
}  