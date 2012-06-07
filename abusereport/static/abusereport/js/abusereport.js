$(document).ready(function() {
 /* ajax submit form */
$('#reportf').live('submit', function() {
    form = $('#reportf');
    $.post(form.attr('action'), form.serialize(),
    function(data) {
        var stat = eval("(" + data + ")");
        if (stat.stat === "OK") {
            alert("zapisano");
            
        }
        else{
            alert("fail");
        }
    });
 
    return true;   

    });
    
});