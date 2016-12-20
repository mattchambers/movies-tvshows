// Animate in the movies when the page loads
        $(document).ready(function () {
          $('.content-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });