/*!
* surveyjs - Survey JavaScript library v0.9.11
* (c) Andrew Telnov - http://surveyjs.org/
* License: MIT (http://www.opensource.org/licenses/mit-license.php)
*/
function sendDataToServer(survey) {
  var resultAsString = JSON.stringify(survey.data);
  alert(resultAsString); //send Ajax request to your web server.
  $.post("http://127.0.0.1:3000", resultAsString, function(result){
    console.log("success!")
});

};

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

// var survey = new Survey.Survey({ questions: [
//     { type: "html", name: "info", html:"<table><body><row><td><img src='http://surveyjs.org/images/26178-20160417.jpg' width='100px' /></td><td style='padding:20px'>You may put here any html code. For example images, <b>text</b> or <a href='http://surveyjs.org/builder/index.html'  target='_blank'>links</a></td></row></body></table>" }
// ]});

var survey = new Survey.Survey(surveypool[getRandomInt(0, surveypool.length)], "surveyContainer");

window.onkeyup = function(e) {
   var key = e.keyCode ? e.keyCode : e.which;
   console.log(key);
   if (key == 49) {
     var flag=0
     $("*").each(function(){
        // console.log($(this))
         var g = $(this).find('input[type=radio]:first');
        //  console.log(g);
         if(flag==0){
          //  g.hide();
          g.click();
          // g.select();
           flag=1;
         }
     });
    }
      else if (key == 50) {
        var flag=0
        $("*").each(function(){
            var g = $(this).find('input[type=radio]:eq(1)');
            if(flag==0){
             g.click();
              flag=1;
            }
            // g = $(this).find('input[type=button]');
            // g.click();
        });

   }


}

// var survey = new Survey.Survey(surveyJSON, "surveyContainer");
//Use onComplete event to save the data
survey.onComplete.add(sendDataToServer);
