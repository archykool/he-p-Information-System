function initChatSocketActions(chatSocket, chatBotSocket) {
    let currentUserId = document.getElementById('user-id').value.toString();

    chatSocket.onmessage = function (e) {
        addNewMessage(e)
    };

    chatBotSocket.onmessage = function(e){
        addNewMessage()
    };

    // 点击发送时的一系列动作
    document.querySelector('#chat-message-submit').onclick = function (e) {
        let messageInputDom = $('#message-text');
        let text_msg = messageInputDom.val();
        if (text_msg) {
            if (text_msg === '/stock=APPL') {
                chatBotSocket.send(JSON.stringify({
                    'user_id': currentUserId,
                }))
            }
            else {
                chatSocket.send(JSON.stringify({
                    'text_msg': text_msg,
                }));
            }
            messageInputDom.val('');
        }
    };
}

function addNewMessage(e) {
    let data = JSON.parse(e.data);
    let currentUserId = document.getElementById('user-id').value.toString();

    let isOwn = parseInt(currentUserId) === parseInt(data['user_id']);

    messagesList.items.push({
        text_msg: data['text_msg'],
        user_id: data['user_id'],
        created_at: data['created_at'],
        publisher: data['username'],
        own: isOwn,
    });
    if (!isOwn) {
        sendNotification()
    }
}


function sendNotification() {
    console.log("Sending alert")

    if (Notification.permission !== "granted")
        Notification.requestPermission();
    else {
        console.log("sent alert")
        new Notification('Realtime Chat Notification', {
            icon: 'http://cdn.sstatic.net/stackexchange/img/logos/so/so-icon.png',
            body: "你在he！p有新消息哦",
        });
    }
}