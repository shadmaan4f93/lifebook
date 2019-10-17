$(document).ready(function() {
    
       $(".custom-tile li").click(function() {
           $(this).parent().find('li').removeAttr('class');
           $(this).addClass('active');
           var value = $(this).attr('data');
           var $id = $(this).parent().parent().parent().find('input')
           if (value && $id ) {
               var prev_value = $id.val();
               if(value == prev_value) {
                   $(this).removeClass('active');
                   $id.val('');  
               }
               else {
                   $id.val(value);
               }   
           }             
       });
   });