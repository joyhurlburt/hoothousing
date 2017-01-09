/**
 * Created by alishakawaguchi on 4/4/15.
 */
$(document).ready(function(){


     $('.prop-rating').click(function(e){
            var value = $(this).attr("value");
            var num = parseInt(value);


        for(var i = 1; i < num+1; i++) {

             var selected = document.getElementById(i.toString());
             selected.src = "/static/images/star-full.png";

        }
        for(var j=num+1; j<6; j++){
             var unselected = document.getElementById(j.toString());
            unselected.src = "/static/images/star-empty.png";

        }



    });


     $('.mgmt-rating').click(function(e){
            var value = $(this).attr("value");
            var num = parseInt(value);


        for(var i = 1; i < num+1; i++) {

             var selected = document.getElementById("mgmt"+i.toString());
             selected.src = "/static/images/star-full.png";

        }
        for(var j=num+1; j<6; j++){
             var unselected = document.getElementById("mgmt"+j.toString());
            unselected.src = "/static/images/star-empty.png";

        }



    });



    //$( "#city" ).autocomplete({
    //  source: function( request, response ) {
    //      alert("here");
    //    $.ajax({
    //      url: "http://internsolutions.henkhaus.us/rest/",
    //      dataType: "jsonp",
    //      data: {
    //        q: request.term
    //      },
    //      success: function( data ) {
    //        response( data );
    //      }
    //    });
    //  },
    //  minLength: 3,
    //  select: function( event, ui ) {
    //    log( ui.item ?
    //      "Selected: " + ui.item.label :
    //      "Nothing selected, input was " + this.value);
    //  },
    //  open: function() {
    //    $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
    //  },
    //  close: function() {
    //    $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
    //  }
    //});

    //$("#city").click(function(e){
    //    $.ajax({
    //        url: 'http://internsolutions.henkhaus.us/rest/broadway',
    //        type: 'GET',
    //        dataType: 'jsonp',
    //        success: function(result){
    //            alert(result.responseText);
    //        },
    //        error: function(result){
    //            //alert(result.responseText);
    //        }
    //    });
    //
    //
    //
    //});

});