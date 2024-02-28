initActions();
let currentRealtimeChatSocket = null;
let currentRealtimeChatBotSocket = null;
let messagesList = new Vue({
    el: '#messages-list',
    data: {
        items: []
    },
});

function initActions() {
    initMessageInputTextActions();
    initChatsActions();
}

function initChatsActions() {
    $('.chat_list').click(function () {
        let chatId = $(this).data('chat-id');
        let chatName = $(this).data('chat-name');

        messagesList.items = [];

        let chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + chatName + '/');
        let chatBotSocket = new WebSocket('ws://' + $('#MxOnline-bot').val() + '/ws/chat/bot/' + chatName + '/');

        if (currentRealtimeChatSocket) {
            currentRealtimeChatSocket.close();
        }

        if (currentRealtimeChatBotSocket) {
            currentRealtimeChatBotSocket.close();
        }

        currentRealtimeChatSocket = chatSocket;
        currentRealtimeChatBotSocket = chatBotSocket;

        initChatSocketActions(chatSocket,chatBotSocket);

        $(".chat_list").removeClass('active_chat');
        this.classList.add('active_chat');

        let messageTextDOM = $('#message-text');

        messageTextDOM.removeAttr('disabled');
        messageTextDOM.attr('placeholder', "Write a message");

        updateChatMsg(chatId);
    });
}

function updateChatMsg(chatId) {
    let userId = document.getElementById('user-id').value.toString();
    let newData = [];

    axios
        .get(`/chat/allfriends/${chatId}`)
        .then(response => {
            $.each(response.data, function (index, value) {
                newData.push({
                    text_msg: value.text_msg,
                    user_id: value.user_id,
                    created_at: value.created_at,
                    own: parseInt(userId) === parseInt(value.user_id),
                })
            });
        });

    messagesList.items = newData;

}

$('#messages-list').bind("DOMSubtreeModified", function () {
    try {
        document.getElementById("messages-list").lastChild.scrollIntoView();
    }
    catch (e) {
    }
});

document.addEventListener('DOMContentLoaded', function () {
    if (!Notification) {
        alert('请打开he!p通知.');
        return;
    }

    if (Notification.permission !== "granted") {
        Notification.requestPermission();
    }
});

