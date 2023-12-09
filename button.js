COUNT = 0
// Button to turn on camera
var button3 = $("#watch");
button3.click(function () {
    COUNT++;
    console.log(button3.text());

    // initial click to stream, generates iframe for livestream
    if (button3.text() === "Click to Stream" && COUNT < 2) {
        // setting attributes to display iframe also uses css
        var x = document.createElement("IFRAME");
        x.setAttribute("src", "http://[enter IP]:8000/index.html");
        x.setAttribute("class","m-5 pb-5");
        document.body.appendChild(x).height = "500";

        $.ajax({
            url: "/camera_on",
            type: "post",
            success: function (response) {
                console.log(response);
                button3.text("Stop Stream");
            }
        });

    }
    // debugged issues with initial click to stream this will get out of that and change button to stop stream
    else if (button3.text() === "Click to Stream" && COUNT ==2) {

        $.ajax({
            url: "/camera_on",
            type: "post",
            success: function (response) {
                console.log(response);
                button3.text("Stop Stream");
                COUNT++;
                
            }
        });

    } 
    // if button is stopped this will allow iframe to open again to start viewing
    else if (button3.text() === "Click to Stream" && COUNT>2) {
        // creating attributes to iframe for it to be displayed with css
        var x = document.createElement("IFRAME");
        x.setAttribute("src", "http://[Enter IP]:8000/index.html");
        x.setAttribute("class","m-5 pb-5");
        document.body.appendChild(x).height = "500";
        $.ajax({
            url: "/camera_on",
            type: "post",
            success: function (response) {
                console.log(response);
                button3.text("Stop Stream");
                
            }
        });

    } 
    // if button is stop stream iframe will be deleted from page
    else {
        // creating attriubutes to iframe to be able to delete
        const IFRAME = document.querySelector("IFRAME");
        IFRAME.setAttribute("id", "iframe1");
        IFRAME.setAttribute("class","border border-success");
        const element = document.getElementById("iframe1");
        element.remove()
        $.ajax({
            url: "/Stop_Stream",
            type: "post",
            success: function () {
                button3.text("Click to Stream");
            }
        })
    }
});

var button = $("#Dispense");
button.click(function () {
    console.log(button.text());
    if (button.text() === "Dispense Treats") {
        $.ajax({
            url: "/Dispense",
            type: "post",
            success: function (response) {
                console.log(response);
                button.text("Dispense Another");
            }
        });
    } else {
        $.ajax({
            url: "/Dispense_Another",
            type: "post",
            success: function () {
                button.text("Dispense Another");
            }
        })
    }
});


