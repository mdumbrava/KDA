from KDA import create_app

app = create_app()


if __name__ == '__main__': #never change this "always main"
    app.run(host='127.0.0.1', port=80, debug=True)
