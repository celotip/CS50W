document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  document.querySelector("#compose-form").onsubmit = () => {
    const recipient = document.querySelector("#compose-recipients").value;
    const subject = document.querySelector("#compose-subject").value;
    const body = document.querySelector("#compose-body").value;
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: recipient,
          subject: subject,
          body: body,
          read: false,
          archived: false
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
    })
    .then(() => {
      load_mailbox('sent');
    })
  
    return false;
}

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-view').innerHTML = "";

  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails);

      // ... do something else with emails ...
      const head = document.createElement('div');
      head.innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
      document.querySelector('#emails-view').append(head);
      for (let i = 0; i < emails.length; i++) {
        const box = document.createElement('div');
        if (emails[i]["read"]) {
          box.className = 'boxread';
        }
        else {
          box.className = 'boxunread';
        }
        if (mailbox === "sent") {
          box.innerHTML = `<div class="adv">To: ${emails[i]["recipients"]}</div> ${emails[i]["subject"]} <span style="float:right; color:grey;">${emails[i]["timestamp"]}</span>`;
        }
        else {
          box.innerHTML = `<div class="adv"><b>${emails[i]["sender"]}</b></div> ${emails[i]["subject"]} <span style="float:right; color:grey;">${emails[i]["timestamp"]}</span>`;
        }
        box.addEventListener('click', function() {
          load_mail(Number(emails[i]["id"]));
        });
        document.querySelector('#emails-view').append(box);
      }
  });
}

function load_mail(mail_id) {
    const user = JSON.parse(document.getElementById('user').textContent);
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#emails-view').innerHTML = "";

    fetch(`/emails/${mail_id}`)
    .then(response => response.json())
    .then(emails => {
        // Print emails
        console.log(emails);

        const br1 = document.createElement('br');
        const br2 = document.createElement('br');
        const br3 = document.createElement('br');
        const time = document.createElement('div');
        time.innerHTML = `<b>Timestamp: </b>${emails["timestamp"]}`;
        const recipient = document.createElement('div');
        recipient.innerHTML = `<b>To: </b>${emails["recipients"]}`;
        const sender = document.createElement('div');
        sender.innerHTML = `<b>From: </b>${emails["sender"]}`;
        const subject = document.createElement('div');
        subject.innerHTML = `<b>Subject: </b>${emails["subject"]}`;
        const body = document.createElement('div');
        body.innerHTML = `<br> ${emails["body"]}`;
        const reply = document.createElement('div');
        reply.className = "btn btn-sm btn-outline-primary";
        reply.innerHTML = "Reply";
        reply.addEventListener('click', function() {
          compose_reply(emails["sender"], emails["subject"], emails["timestamp"], emails["body"]);
        });
        const arc = document.createElement('div');
        arc.className = "btn btn-sm btn-outline-primary";
        if (emails["archived"]) {
          arc.innerHTML = "Unarchive";
        }
        else {
          arc.innerHTML = "Archive";
        }
        arc.addEventListener('click', function() {
          if (emails["archived"]) {
            fetch(`/emails/${emails["id"]}`, {
              method: 'PUT',
              body: JSON.stringify({
                archived: false
              })
            })
            .then(() => {
              load_mailbox('inbox');
            })
          }
          else {
            fetch(`/emails/${emails["id"]}`, {
              method: 'PUT',
              body: JSON.stringify({
                archived: true
              })
            })
            .then(() => {
              load_mailbox('inbox');
            })
          }
        });
        document.querySelector('#emails-view').append(sender);
        document.querySelector('#emails-view').append(recipient);
        document.querySelector('#emails-view').append(subject);
        document.querySelector('#emails-view').append(time);
        document.querySelector('#emails-view').append(body);
        document.querySelector('#emails-view').append(br1);
        if (user !== emails["sender"]) {
          document.querySelector('#emails-view').append(reply);
          document.querySelector('#emails-view').append(br2);
          document.querySelector('#emails-view').append(br3);
          document.querySelector('#emails-view').append(arc); 
        }

        if (user !== emails["sender"]) {
          fetch(`/emails/${mail_id}`, {
            method: 'PUT',
            body: JSON.stringify({
                read: true
            })
          });
        }
    });
}

function compose_reply(sender, subject, time, body) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
  document.querySelector('#compose-recipients').value = sender;
  document.querySelector('#compose-subject').value = `Re: ${subject}`;
  document.querySelector('#compose-body').value = `On ${time} ${sender} wrote: ${body}`;
}
