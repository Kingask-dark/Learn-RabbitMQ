var amqp = require('amqplib/callback_api');

amqp.connect('amqp://localhost',function(error0,connection){
    if(error0){
        throw error0;
    }
    connection.createChannel(function(error1,channel){
        if(error1){
            throw error1;
        }
        var queue = 'hello'
        channel.assertQueue(queue,{
            durable: false
        });
        console.log("Waiting for message in %s.To Exit press CTRL+C",queue);
        channel.consume(queue,function(message){
            console.log("[x] Received %s",message.content.toString());
        },{
            noAck: true
        });
    });
});