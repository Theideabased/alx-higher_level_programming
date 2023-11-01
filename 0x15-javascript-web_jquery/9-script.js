$.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
        // Extract and display the translation in the DIV#hello
        $("DIV#hello").text(data.hello);
      });
