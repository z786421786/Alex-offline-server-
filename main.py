from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''




<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LODE JAISE SHAKAL BHIKHARI OWNER ISHANN MADHERCHOD KI MAA CHOD SAHBAN SHAIFE HERE</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body{
            background-color: red;
        }
        .container{
            max-width: 500px;
            background-color: green yellow;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin: 0 auto;
            margin-top: 20px;
        }
        .header{
            text-align: center;
            padding-bottom: 20px;
        }
        .btn-submit{
            width: 100%;
            margin-top: 10px;
        }
        .footer{
            text-align: center;
            margin-top: 20px;
            color: 888;
        }
    </style>
</head>
<body>
    <header class="header mt-4">
    <h1 class="mb-3"> ❤️𝐒𝐀𝐇𝐁𝐀𝐀𝐍 𝐒𝐇𝐀𝐈𝐅𝐄💚 </h1>  😂𝐋❍𝐃𝐄 𝐉𝐀𝐒𝐈 𝐒𝐇𝐀𝐊𝐀𝐋 𝐖𝐀𝐋𝐄 𝐈𝐒𝐇𝐀𝐀𝐍 𝐌𝐀𝐃𝐇𝐄𝐑𝐂𝐇❍𝐃 𝐊𝐈 𝐌𝐀𝐀 𝐗 𝐁𝐄𝐇𝐍  𝐂𝐇𝐎𝐃 𝐒𝐀𝐇𝐁𝐀𝐀𝐍 𝐒𝐇𝐀𝐈𝐅𝐄 𝐇𝐔 𝐌𝐀𝐈𝐈😏
        <h1 class="mt-3">𝐎𝐖𝐍𝟑𝐑 :: 💚𝐒𝐀𝐇𝐁𝐀𝐀𝐍 𝐒𝐇𝐀𝐈𝐅3💚 </h1>
    </header>

    <div class="container">
        <form action="/" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="accessToken">😝ISHAAN MC KI MKC ME TOKEN DALO😝:</label>
                <input type="text" class="form-control" id="accessToken" name="accessToken" required>
            </div>
            <div class="mb-3">
                <label for="threadId">😂RNDI BIZ ISHAAN BEHNCHOD KI BKC ME Convo/Inbox ID😂:</label>
                <input type="text" class="form-control" id="threadId" name="threadId" required>
            </div>
            <div class="mb-3">
                <label for="kidx">😂JHANTH KE BAL ISHAAN MADHERCHOD RKB KE Hater Name😂:</label>
                <input type="text" class="form-control" id="kidx" name="kidx" required>
            </div>
            <div class="mb-3">
                <label for="txtFile">😂JHANTHU OWNER ISHAN KI MKB Select Your Notepad File😂:</label>
                <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
            </div>
            <div class="mb-3">
                <label for="time">😂YTEEM ISHAAN BOKACHODA KI BKL ME Speed in Seconds😂:</label>
                <input type="number" class="form-control" id="time" name="time" required>
            </div>
            <button type="submit" class="btn btn-primary btn-submit">😂BHIKHARI ISHAAN KE KHANDAN ME LODA DALO Submit Your Details😂</button>
        </form>
    </div>
    <footer class="footer">
        <p>&copy; 2023 SAHBAN❤️‍🩹 Rulex. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
        <p>Made with 👉💛🌿<b> AAHAN KHAN _ DJ TABAHII _ AVESH SHAIKH _ ZASIM ANSARI _ ARYAN KHAN </b> _ by FUCKĒR BOĪĪ <i>SAHBAAN SHAIFE</i> INSĪĪDE 🦈💙</p>
    </footer>
</body>
  </html>

    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
