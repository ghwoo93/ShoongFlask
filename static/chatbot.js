function sendMessage(message) {
        console.log('입력메시지:',message)


        $.ajax({url:"/message",data:{'message': message},type:'post',success:receiveResponse})

        //flask서버로부터 응답을 받으면 receiveResponse콜백함수가 호출됨
        function receiveResponse(data) {//data는 flask로부터 받은 응답 {'message':'다이얼로그플로우가 보내준값'}
          //chat-container에 bot의 응답 추가
          $('.chat-container').append(`
                <div class="chat-message col-md-5 bot-message">
                    ${data.message}
                </div>
          `)
          //스크롤바 아래로
          $(".chat-container").scrollTop($(".chat-container")[0].scrollHeight);

             console.log('받은 메시지:',data)
        }
    }
$("#query").on('keypress',function(e) {

    if (e.keyCode == 13){
        //e.preventDefault();
        var query = $(this).val()
        console.log(query)
        if (!query) {//텍스트를 입력하지 않는 경우
          return
        }
        //chat-container에 사용자의 응답 추가
        $('.chat-container').append(`
            <div class="chat-message col-md-5 offset-md-7 human-message">
                ${query}
            </div>
        `)
        // 입력창 클리어
        $('#query').val('')
        //스크롤바 아래로
        $(".chat-container").scrollTop($(".chat-container")[0].scrollHeight);
        //메시지 전송
        sendMessage(query)
    }
});