from flask import Flask
from routers import book_api


app = Flask(__name__)
app.register_blueprint(book_api)

# Kode di atas membuat instance dari Flask dengan nama variabel app. 
# Selanjutnya, kita menggunakan method register_blueprint() 
# untuk mendaftarkan blueprint yang telah kita definisikan sebelumnya 
# dengan nama book_api pada instance app. Hal ini berfungsi untuk menghubungkan 
# blueprint dengan aplikasi Flask sehingga dapat diakses melalui URL yang telah didefinisikan 
# di dalam blueprint tersebut. Dengan demikian, ketika aplikasi dijalankan, blueprint tersebut akan 
# terdaftar dan dapat digunakan oleh aplikasi Flask.

if __name__ == '__main__':
    app.run(debug=True)
