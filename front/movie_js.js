let MovieObject = {
    init: function(){
    },

    getall: function(){
       $.ajax({
       // 실행할 코드
          type: "GET",
          url: "http://localhost:8000/all",
       }).done(function(response){
       // 성공코드
            console.log(response)
            movielist = response.result

            topdiv = document.createElement("div")
            topdiv.style = "column-count:5"
            document.body.appendChild(topdiv)

            movielist.forEach( movie => {
                // 첫번째 영화이미지
                cmovie = document.createElement("div")
                cmovie.className = "card"
    
                mimg = document.createElement("img")
                mimg.className = "card-img-top"
                mimg.src = movie.poster_path
                mimg.onclick = function(){
                //    location.href = movie.url
                    window.open(movie.url);
                }
                mimg.style.cursor = "pointer"
                cmovie.appendChild(mimg)
                topdiv.appendChild(cmovie)
            });


       }).fail(function(error){
           // 실패코드
           console.log(error)
       });
    }
}

MovieObject.init();
MovieObject.getall();